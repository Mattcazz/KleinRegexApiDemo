from api import API
from userHandler import UserHandler          

def main():
    api = API("")
    userHandler = UserHandler(api)
    api.run("localhost", 8080)

if __name__ == "__main__":
    main()