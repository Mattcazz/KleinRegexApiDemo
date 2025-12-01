from klein import Klein

class UserHandler():
    def __init__(self, api : Klein):
        self.api = api
        self.register_routes()
    
    def get_user(self, request, id):
        return f"User with id : {id}"
    
    def register_routes(self):
       self.api.route('/users/<regex("[0-9]{3}"):id>', methods=['GET'])(self.get_user)
