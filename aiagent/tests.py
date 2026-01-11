from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
def main():
    working_directory="calculator"
    # print(get_file_content(working_directory,"lorem.txt"))
    # print(get_file_content(working_directory,'main.py'))
    # print(get_file_content(working_directory,'xyz.py'))
    # print(write_file(working_directory,'lorem.txt',"This is a new file created for testing."))
    # print(write_file(working_directory,'subdir/newfile.txt',"This is a new file in a new subdirectory."))
    print(run_python_file(working_directory,'main.py',args=["45 - 8 + 11"]))
main()

# MAKE SURE TO USE SPACES WHEN RUNNING THE CALC APPLICATION