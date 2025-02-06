# Task Manager

This Python script implements a simple task manager. It allows users to add, remove, and view their tasks.  The tasks are stored in a dictionary, and the program provides a command-line interface for interacting with the task list.

## Features

* **Add:** Add a new task to the list.
* **Remove:** Remove an existing task from the list.
* **View:** View all current tasks.
* **Exit:** Exit the program.

## How to Use

1.  **Clone the repository:** (You'll need to create the repository first and then clone it locally)
    ```bash
    git clone <repository_url>
    ```
2.  **Run the script:**
    ```bash
    python task_manager.py  # Assuming the script is named task_manager.py
    ```
3.  **Follow the prompts:** The script will display a list of available commands. Enter the command you want to execute.

## Example

choose your command

{'Add': 'Add a new task', 'Remove': 'Remove a task', 'View': 'View all tasks', 'Exist': 'Exit the program'}

Entre your command : Add

Entre your task : Learn Python

Task is added

{'Task 1': 'Learn Python'}

choose your command

{'Add': 'Add a new task', 'Remove': 'Remove a task', 'View': 'View all tasks', 'Exist': 'Exit the program'}

Entre your command : View

{'Task 1': 'Learn Python'}

choose your command

{'Add': 'Add a new task', 'Remove': 'Remove a task', 'View': 'View all tasks', 'Exist': 'Exit the program'}

Entre your command : Remove

Entre the task want to remove : Task 1

{'Task 2': 'Learn Python'} # If a Task 2 existed.  Otherwise, it would be empty.

choose your command

{'Add': 'Add a new task', 'Remove': 'Remove a task', 'View': 'View all tasks', 'Exist': 'Exit the program'}

Entre your command : Exist

Exist the program .
