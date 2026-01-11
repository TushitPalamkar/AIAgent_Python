import os
from google.genai import types
def get_files_info(working_directory,directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory=os.path.abspath(os.path.join(working_directory,directory))
    
    if not abs_directory.startswith(abs_working_directory):
        return f"Error: Directory {directory} is outside the working directory {working_directory}."
    
    contents=os.listdir(abs_directory)
    final_response=""
    for content in contents:
        is_dir=os.path.isdir(os.path.join(abs_directory,content))
        size=os.path.getsize(os.path.join(abs_directory,content))
        final_response+= f"-{content}:file-size={size} bytes; is_directory={is_dir}\n"
    return final_response

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory."
            ),
        },
        required=["directory"],
    ),
)
