import json
import sys
import os

current_directory = os.getcwd()
print(current_directory)

def set_working_directory_to_script_location():
    # Get the absolute path of the currently executing script
    script_path = os.path.abspath(sys.argv[0])
    
    # Extract the directory name from the script path
    script_dir = os.path.dirname(script_path)
    
    # Change the current working directory to the script's directory
    os.chdir(script_dir)
    
    print(f"Current working directory changed to: {os.getcwd()}")

# Call the function at the beginning of your script
set_working_directory_to_script_location()


json_file = 'tasks.json'

def validate_file_path(file_path):  
    if not os.path.exists(file_path):
        with open('tasks.json', 'w') as f:
            json.dump([], f)

def load_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

validate_file_path(file_path=json_file)
tasks = load_file(file_path=json_file)
print(tasks)