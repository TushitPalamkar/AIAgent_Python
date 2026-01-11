from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.get_files_info import schema_get_files_info, get_files_info
from google.genai import types
working_directory="calculator"
def call_function(function_call_part, verbose=False):
    if verbose:
        print("Function call part received:", function_call_part)
    else:
        print("Function call part received.")
    result=""
    if function_call_part.name == "get_files_info":
       result= get_files_info(working_directory=working_directory,**function_call_part.args)
    if function_call_part.name == "get_file_content":
       result= get_file_content(working_directory=working_directory,**function_call_part.args)
    if function_call_part.name == "write_file":
       result= write_file(working_directory=working_directory,**function_call_part.args)   
    if function_call_part.name == "run_python_file":
       result= run_python_file(working_directory=working_directory,**function_call_part.args)  
    if result=="":   
        return types.Content(
        role="tool",
        parts=[types.Part.from_function_response(
            name=function_call_part.name,
            response={"error": f"Unknown function {function_call_part.name}"}
        )]
    )
    return types.Content(
        role="tool",
        parts=[types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": result}
        )]
    )