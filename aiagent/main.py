import os
import sys
from functions.get_files_info import schema_get_files_info, get_files_info
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.call_function import call_function
def main():
    load_dotenv()
    system_prompt='''
    
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan.
You have access to the following tools:

- List files and directories
- Read the contents of a file
- Write to a file
- Run a Python file with optional args

All paths you provide should be relative to the working directory.
You should not use absolute paths.
If a request can be fulfilled using a function call, do so.
If it cannot, respond with a helpful explanation.


'''
    api_key = os.getenv("GEMINI_API_KEY")
    client= genai.Client(api_key=api_key)
    verbose_flag=False
    if len(sys.argv) < 2:
        print("Give an prompt as argument")
        exit(1)
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    prompt = sys.argv[1]
    print(sys.argv)
    messages=[
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    available_functions=types.Tool(
        function_declarations=[schema_get_files_info
                               ,schema_get_file_content,
                               schema_write_file,
                               schema_run_python_file],

    )
    config=types.GenerateContentConfig(
        tools=[available_functions],
             system_instruction=system_prompt)
    
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=config
        )
    
   
    if response is None or response.usage_metadata is None:
        print("No usage metadata available.")
        exit(1)
    
    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
    
    if response.function_calls:
        print(response.function_calls)
        for fc in response.function_calls:
           result = call_function(fc, verbose=verbose_flag)
           print(result)           
    else:
        print(response.text)
# print(get_files_info("calculator",'pkg'))
main()
