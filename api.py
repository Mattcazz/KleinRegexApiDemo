from klein import Klein
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

class API ():
    def __init__(self):
        self.api = Klein()
        self.api.url_map.converters["regex"] = RegexConverter 
        

    def run(self, host : str, port : int):
        self.api.run(host, port)

    def get_instance(self) -> Klein: 
        return self.api