import os
import subprocess
from google.genai import types
def run_python_file(working_directory, file_path,args=[]):
    abs_working_directory=os.path.abspath(working_directory)
    abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: File {file_path} is outside the working directory {working_directory}." 
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a valid file."
    if not file_path.endswith('.py'):
        return f"Error: {file_path} is not a Python (.py) file."
    try:
        final_args=['python', abs_file_path]
        if args:
            final_args.extend(args)
        result=subprocess.run(final_args, cwd=abs_working_directory, timeout=25, capture_output=True, text=True)
        if result.returncode !=0:
            return f"Error executing file {file_path}:\n{result.stderr}"
        return f"Output of file {file_path}:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Error executing file {file_path}: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file with python interpreter accepts additional cli arguments as an optional array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run, relative to the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command line arguments to pass to the Python file.",
                items=types.Schema(type=types.Type.STRING)
            ),
        },
        required=["file_path"],
    ),
)