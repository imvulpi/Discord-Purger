import sys
from removal.handler import delete_handler;

def main():
    arguments = sys.argv
    if len(arguments) > 1:
        arguments.pop(0)
        subcommand = arguments.pop(0) 
        match subcommand:
            case "delete":
                delete_handler(arguments);    
    else:
        purger_help()

def purger_help():
    print("Usage: delete u-url s-search_query e-youremail p-yourpassword")

if __name__ == "__main__":
    main()
