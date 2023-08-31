# TodoList

## Video Demo
[Link to Video Demo](<URL HERE>)

## Description
TodoList is a simple command-line tool to help you manage your tasks. It allows you to keep track of tasks, their due dates, priorities, and completion status.

## Features
- Add tasks with descriptions, priorities, and optional due dates.
- List tasks in order of due dates and priorities.
- Mark tasks as completed.
- More features can be added and customized based on your needs.

## Installation
1. Clone the repository or download the project files.
2. Open a terminal and navigate to the project directory.

## Usage
1. Run the program by executing the following command in the terminal:
   ```
   python todo_list.py
   ```
2. The program will display a list of tasks sorted by due date and priority.
3. Follow the on-screen menu to add tasks, list tasks, mark tasks as completed, and more.

## Screenshots
![Screenshot](screenshot.png)

## Project Structure
- `todo_list.py`: The main Python script containing the TodoList class and the user interface.
- `tasks.json`: A JSON file used to store tasks data.

## Dependencies
The project uses the built-in `json` module for data storage.

## Future Improvements
- Allow tasks to be edited or deleted.
- Improve the user interface and display more task details.
- Generate calendar files with tasks' due dates.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

<!-- Object: Task -->
<details>
<summary><strong>Task Object</strong></summary>

### Properties
- `description`: Description of the task.
- `due_date`: Due date of the task.
- `priority`: Priority of the task (high, medium, low).
- `completed`: Completion status of the task.

### Methods
- `__init__(self, description, due_date, priority)`: Initialize a new Task object.
- `complete(self)`: Mark the task as completed.
- `__str__(self)`: Return a string representation of the task.

</details>

<!-- Function: add_task -->
<details>
<summary><strong>add_task Function</strong></summary>

### Description
Add a new task to the list of tasks.

### Parameters
- `tasks_list`: The list of tasks.
- `description`: Description of the task.
- `due_date`: Due date of the task.
- `priority`: Priority of the task.

### Usage
```python
add_task(tasks_list, description, due_date, priority)
```

</details>

<!-- Function: list_tasks -->
<details>
<summary><strong>list_tasks Function</strong></summary>

### Description
List all tasks in the order of due dates and priorities.

### Parameters
- `tasks_list`: The list of tasks.

### Usage
```python
list_tasks(tasks_list)
```

</details>

<!-- Function: mark_completed -->
<details>
<summary><strong>mark_completed Function</strong></summary>

### Description
Mark a task as completed.

### Parameters
- `tasks_list`: The list of tasks.
- `task_index`: Index of the task to mark as completed.

### Usage
```python
mark_completed(tasks_list, task_index)
```

</details>
