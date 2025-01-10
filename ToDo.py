import argparse
import json          
import os

TODO_FILE = 'todo_list.json' #To store user's task.

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    print(f"Added task: {task}")

def update_task(index, new_task):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['task'] = new_task
        save_tasks(tasks)
        print(f"Updated task {index} to: {new_task}")
    else:
        print(f"Task {index} does not exist.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print(f"Task {index} does not exist.")

def mark_task_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
        print(f"Marked task {index} as done: {tasks[index]['task']}")
    else:
        print(f"Task {index} does not exist.")

def list_tasks(show_all=True):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if show_all or not task['done']:
            status = "Done" if task['done'] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")

def main():
    parser = argparse.ArgumentParser(description="A simple CLI to-do list manager.")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add task command
    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument('task', help="The task to add")
    
    # Update task command
    update_parser = subparsers.add_parser('update', help="Update an existing task")
    update_parser.add_argument('index', type=int, help="The index of the task to update")
    update_parser.add_argument('new_task', help="The new task description")
    
    # Delete task command
    delete_parser = subparsers.add_parser('delete', help="Delete a task")
    delete_parser.add_argument('index', type=int, help="The index of the task to delete")
    
    # Mark task done command
    done_parser = subparsers.add_parser('done', help="Mark a task as done")
    done_parser.add_argument('index', type=int, help="The index of the task to mark as done")
    
    # List tasks command
    list_parser = subparsers.add_parser('list', help="List tasks")
    list_parser.add_argument('--all', action='store_true', help="Show all tasks, including completed ones")
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'update':
        update_task(args.index, args.new_task)
    elif args.command == 'delete':
        delete_task(args.index)
    elif args.command == 'done':
        mark_task_done(args.index)
    elif args.command == 'list':
        list_tasks(show_all=args.all)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()