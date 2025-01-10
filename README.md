# To-Do List Manager

A **simple command-line tool** written in Python to help you manage your to-do tasks effortlessly. With this tool, you can add, update, delete, mark tasks as done, and list tasks with options to filter by their status.

---

## Features

- **Add Tasks**: Quickly add new tasks to your to-do list.
- **Update Tasks**: Modify the details of an existing task.
- **Delete Tasks**: Remove tasks you no longer need.
- **Mark as Done**: Mark tasks as completed.
- **View Tasks**: List all tasks or filter to see only pending tasks.

---


## Dependencies

The tool uses the following Python modules:

- **argparse**: For handling command-line arguments.

- **json**: For saving and loading tasks.

- **os**: For file management operations.

Make sure these modules are available in your Python environment (they are included in the Python standard library).



## Requirements

- **Python 3.x**: Ensure Python is installed on your system. [Download Python here](https://www.python.org/).

---

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Jeevan9971/To-Do-list-manager.git
    cd todo-cli-tool
    ```

2. Verify Python installation by running:
    ```bash
    python --version
    ```

---

## Usage

Run the `todo.py` script using Python with the following commands:

### **1. Add a Task**
Add a new task to your to-do list.
```bash
python todo.py add "get fruits"
```

### **2. Update a Task**
Update the details of an existing task.
```bash
python todo.py update <index> "get fruits and vegetables"
```
Replace `<index>` with the index number of the task you want to update.

### **3. Delete a Task**
Remove a task from the list.
```bash
python todo.py delete <index>
```
Replace `<index>` with the index number of the task you want to delete.

### **4. Mark a Task as Done**
Mark a specific task as completed.
```bash
python todo.py done <index>
```
Replace `<index>` with the index number of the task you want to mark as done.

### **5. List All Tasks**
Display all tasks in your to-do list.
```bash
python todo.py list
```

### **6. List Only Incomplete Tasks**
Show only the tasks that are still pending.
```bash
python todo.py list --all
```

---

## Example

### Add a Task
```bash
python todo.py add "Complete Assignments."
```

### Update a Task
```bash
python todo.py update 0 "Complete Assignments and Submit it to college."
```

### Delete a Task
```bash
python todo.py delete 1
```

### Mark a Task as Done
```bash
python todo.py done 0
```

### List All Tasks
```bash
python todo.py list
```

### List Only Incomplete Tasks
```bash
python todo.py list --all
```


