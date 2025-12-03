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
        self._register_routes()
        

    @route("/users/<id>", "GET")
    def get_user(self, request, id):
        return f"User with id : {id}"


    def _register_routes(self):
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if getattr(method, "_is_route", False):
                self.api.route(method._method, method._path, method)