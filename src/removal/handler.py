from removal.url_deleter import messages_url_deleter
from removal.user_data import UserData

def delete_handler(arguments: list[str]):
    delete_arguments = get_neccesary_data(arguments)
    print(f"URL: {delete_arguments.url} | Search query: {delete_arguments.search}")
    messages_url_deleter(delete_arguments)

def get_neccesary_data(arguments: list[str]):
    data = UserData()
    for argument in arguments:
        if(argument.count("u-")):
            data.url = argument[2:]
        elif(argument.count("s-")):
            data.search = argument[2:]
        elif(argument.count("e-")):
            data.email = argument[2:]
        elif(argument.count("p-")):
            data.password = argument[2:]
        else:
            raise BaseException("Unknown argument. u- is for url | s- is for search. example: u-https://example.com/ s-\"from: username\"")
    
    if(data.search != None and data.url != None):
        return data
    else:
        raise BaseException("Missing arguments search and or url")