from typing import Optional
from klein import Klein
from werkzeug.routing import BaseConverter

class API ():
    def __init__(self, prefix : Optional[str] ):
        self.api = Klein()
        self.prefix = prefix or ''

    def run(self, host : str, port : int):
        self.api.run(host, port)

    def get_instance(self) -> Klein: 
        return self.api
    
    def route(self, method : str, path : str,f):
        url = f"{self.prefix}{path}"
        self.api.route(url, methods=[method])(f)
        print(f"Registering {url} into {f}")