import json
import sys
import os
from typing import Literal
import datetime

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


def validate_file_path():  
    file_path = "tasks.json"
    if not os.path.exists(file_path):
        with open('tasks.json', 'w') as f:
            json.dump([], f)
    return file_path

def load_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Welp if the file is empty this would return []
        return []
    
def save_file(file_path, tasks):
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=4, default=str)

def create_task(task_id:int, description:str, status:Literal["todo", "pending", "done"] = "todo") -> dict:
    if status not in {"todo", "pending", "done"}:
        raise ValueError(
            "Invalid status. Available statuses: todo, pending, done"
        )
    now = datetime.datetime.now().isoformat()

    return {
        "id": task_id,
        "description":description,
        "status":status,
        "createdAt":now,
        "updatedAt":now
    }

def get_next_id(tasks: list[dict]) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task():
    file_path = validate_file_path()
    task_file = load_file(file_path=file_path)
    task_id = get_next_id(task_file)
    description = input("Enter task description: ")
    # status = input("Enter the status of the task [todo pending done] default: todo: ")
    task = create_task(task_id, description)
    task_file.append(task)
    save_file(file_path, task_file)

def view_task():
    file_path = validate_file_path()
    task_file = load_file(file_path=file_path)

    if not task_file:
        print("No tasks found.")
        return

    for task in task_file:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def update_task():
    file_path = validate_file_path()
    task_file = load_file(file_path)
    task_id = int(input("Enter task id: "))
    updated_description = input("Enter the updated description: ")
    
    for task in task_file:
        if task["id"] == task_id:
            task["description"] = updated_description
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_file(file_path, task_file)
            print("Updated Successfully")
            return
        print("Task nmot ofund idiot")
    


print("""============================
    Welcome to TaskTracker
      
      Choose Below To Proceed:
      1: View Tasks
      2. Add task
      3. Update Task
      4. Update status
      5. Delete a task
      6. Exit

==============================
      """)
# add_task()
view_task()
update_task()