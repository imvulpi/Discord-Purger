class UserData:
    def __init__(self, url=None, search=None, email=None, password=None) -> None:
        self.url = url
        self.search = search
        self.email = email
        self.password = password

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
            raise BaseException(f"Unknown argument: {argument}. Please surround values in \"\" if there are any spaces")
    
    if(data.search != None or data.url != None):
        return data
    else:
        if(data.search != None and data.url != None):
            raise BaseException("Search and URL arguments are missing. add u- and s- arguments")
        elif(data.search != None):
            raise BaseException("Search argument is missing. s- argument")
        elif(data.url != None):
            raise BaseException("URL argument is missing. u- argument")