#userHandler
from api import API


class UserHandler():

    def __init__(self, api : API):
        self.api = api 
        self.register_methods()

    def get_user(self, request, id):
        return f"User with id : {id}"
    
    def register_methods(self):
        with self.api.subroute("/users") as api: 
            api.route("/<id>", methods=["GET"])(self.get_user)