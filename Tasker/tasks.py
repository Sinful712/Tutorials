import json
import csv
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"desc": description, "done": False})
    save_tasks(tasks)
    print(f"\033[92mAdded:\033[0m {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\033[93mNo tasks found.\033[0m")
        return
    for idx, task in enumerate(tasks, 1):
        status = "X" if task["done"] else " "
        if task["done"]:
            print(f"\033[92m{idx}. [{status}] {task['desc']}\033[0m")
        else:
            print(f"\033[93m{idx}. [{status}] {task['desc']}\033[0m")

def complete_task(index):
    tasks = load_tasks()
    try:
        index = int(index)
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"\033[92mMarked task {index} as complete.\033[0m")
    except IndexError:
        print("\033[91mInvalid task index.\033[0m")
    except ValueError:
        print("\033[91mInvalid value. Please specify a task index as a number.\033[0m")


def delete_task(index):
    tasks = load_tasks()
    try:
        index = int(index)
        task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"\033[92mDeleted:\033[0m {task['desc']}")
    except IndexError:
        print("\033[91mInvalid task index.\033[0m")
    except ValueError:
        print("\033[91mInvalid value. Please specify a task index as a number.\033[0m")
        
def edit_task(index):
    tasks = load_tasks()
    try:
        index = int(index)
        task = tasks[index - 1]
        new_desc = input(f"\033[96mEnter new description for task {index}: \033[0m")
        task["desc"] = new_desc
        save_tasks(tasks)
        print(f"\033[92mUpdated:\033[0m {task['desc']}")
    except IndexError:
        print("\033[91mInvalid task index.\033[0m")
    except ValueError:
        print("\033[91mInvalid value. Please specify a task index as a number.\033[0m")

def export_to_csv(filename="tasks.csv"):
    tasks = load_tasks()
    try:
        if not tasks:
            print("\033[93mNo tasks to export.\033[0m")
            return
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Index", "Description", "Completed"])
            for idx, task in enumerate(tasks, 1):
                writer.writerow([idx, task["desc"], "Yes" if task["done"] else "No"])
        print(f"\033[92mTasks exported to {filename}\033[0m")
    except:
        print("\033[91mFilename not valid please specify a valid filename\033[0m")



def interactive_mode():
    print("\033[96m== Task Tracker ==\033[0m")
    print("\033[96mCommands: add, list, complete, delete, edit, export, quit\033[0m")
    while True:
        cmd = input("\033[96m> \033[0m").strip().lower()
        if cmd == "add":
            desc = input("\033[96mTask description: \033[0m").strip()
            add_task(desc)
        elif cmd == "list":
            list_tasks()
        elif cmd == "complete":
            idx = input("\033[96mTask number to complete: \033[0m")
            complete_task(idx)
        elif cmd == "delete":
            idx = input("\033[96mTask number to delete: \033[0m")
            delete_task(idx)
        elif cmd == "edit":
            idx = input("\033[96mTask number to edit: \033[0m")
            edit_task(idx)
        elif cmd == "export":
            fln = input("\033[96mFilename you want to export to: \033[0m").strip()
            if fln == "":
                export_to_csv()
            else:
                export_to_csv(fln)
        elif cmd == "quit":
            break
        else:
            print("\033[91mUnknown command.\033[0m")
