
# JOSN
# Loding LOSN

import json
from json import JSONDecodeError
from json import JSONEncoder

jsonstring = '{"a": "apple", "b": "bear", "c": "cat"}'
print(json.loads(jsonstring))


# jsonstring = '{"a": "apple", "b": "bear", "c": "cat"}'
# try:
#     json.loads(jsonstring)
# except JSONDecodeError:
#     print('could not parse JSON:')


# Dumping JSON

pythonDict = {"a": "apple", "b": "bear", "c": "cat"}
print(json.dumps(pythonDict))



# Custom JSON Decoders

class animal:
    def __init__(self,name):
        self.name = name

class animalencoder(JSONEncoder):
    def default(self,o):
        if type(o) == animal:
            return o.name
        return super().default(o)

pythonDict = {'a': animal('aardvark'), 'b': animal('bear'), 'c': animal('cat')}
print(json.dumps(pythonDict , cls = animalencoder))
