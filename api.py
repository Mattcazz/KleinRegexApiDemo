from klein import Klein
from typing import Optional


class NotFound(Exception):
    pass

class API:
    def __init__(self, prefix : Optional[str] ):
        self.api = Klein()
        self.prefix = prefix or ''
        self.handle_error()

    def run(self, host: str, port: int):
        self.api.run(host, port)

    def get_instance(self) -> Klein:
        return self.api

    def route(self, path: str, *args, **kwargs):
        def decorator(func):
            self.api.route(path, *args, **kwargs)(func)
            return func
        return decorator
    
    def notfound(self, request, failure):
        request.setResponseCode(404)
        request.setHeader(b"Content-Type", b"application/json")
        return b'{"error": "Not Found"}'
    
    def handle_error(self):
        self.api.handle_errors(NotFound)(self.notfound)

    def subroute(self, path : str):
        prefix = f"{self.prefix}{path}"
        return self.api.subroute(prefix)