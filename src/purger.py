import sys
from removal.handler import removal_handler;

def main():
    arguments = sys.argv
    if len(arguments) > 1:
        arguments.pop(0)
        subcommand = arguments.pop(0) 
        match subcommand:
            case "delete":
                removal_handler(arguments)
            case _:
                purger_help()    
    else:
        purger_help()

def purger_help():
    print("Usage: delete u-\"url\" s-\"search query\" e-\"your email\" p-\"your password\"\nEmail and password are optional, you can also login using qr code")

if __name__ == "__main__":
    main()