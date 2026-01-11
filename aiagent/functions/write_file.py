import os
from google.genai import types
def write_file(working_directory, file_path, content):
   

    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: File {file_path} is outside the working directory {working_directory}."
    parent_dir=os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Error creating directories for {file_path}: {e}"
    if not os.path.isfile(abs_file_path):
        pass

    try:
        with open(abs_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"Successfully wrote to file {file_path}."
    except Exception as e:
        return f"Error writing to file {file_path}: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites or Writes content to a specified file within the working directory, creating required parent directories safely if needed.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write to, relative to the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file."
            ),
        },
        required=["file_path", "content"],
    ),
)