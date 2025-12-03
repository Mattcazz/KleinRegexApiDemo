from api import API
import inspect

def route(path, method):
    def decorator(func):
        # We attach a custom attribute to the function object
        func._is_route = True
        func._path = path
        func._method = method
        return func
    return decorator



class UserHandler():
        
    def __init__(self, api : API):
        self.api = api
        self.register_routes()
        

    def register_routes(self):
        @self.api.route("/users/<id>", methods=["GET"])
        def get_user(request, id):
            return f"User with id : {id}"
