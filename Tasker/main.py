import argparse
import colorama
from tasks import *
colorama.init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="CLI Task Tracker")
    parser.add_argument("command", nargs='?', help="Command to run (add/list/complete/delete/edit/export)")
    parser.add_argument("param", nargs='?', help="Parameter (e.g. task description or index)")

    args = parser.parse_args()

    if args.command:
        if args.command == "add" and args.param:
            add_task(args.param)
        elif args.command == "list":
            list_tasks()
        elif args.command == "complete" and args.param:
            complete_task(int(args.param))
        elif args.command == "delete" and args.param:
            delete_task(int(args.param))
        elif args.command == "edit" and args.param:
            edit_task(int(args.param))
        elif args.command == "export" and args.param:
            export_to_csv(args.param)
        elif args.command == "export":
            export_to_csv()
        else:
            print("Invalid command or missing parameter.")
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
