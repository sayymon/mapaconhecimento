import datetime
import json
import copy
 
from datetime import date
from datetime import time

from bson.objectid import ObjectId

def obj_to_json(objeto):
    json_to_str = json.dumps(objeto,default=serialize,ensure_ascii=False)
    return json.loads(str(json_to_str)
               .replace("b\'","")
               .replace("{\'","{")
               .replace("}\'","}")
               .replace("]\'","]"))

def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""
    objCopy = copy.copy(obj)
    
    if isinstance(obj, date):
        serial = objCopy.isoformat()
        return serial

    if isinstance(objCopy, time):
        serial = objCopy.isoformat()
        return serial
    
    if isinstance(objCopy, ObjectId):
        return str(objCopy)

    if objCopy.__class__.__name__ == 'mappingproxy':
        return None
    
    print(objCopy.__class__.__name__)

    if isinstance(objCopy,set):
        for objCopyItem in objCopy:
            serialize(objCopyItem)
        
        return list(objCopy)

    if hasattr(objCopy,"__dict__") and objCopy.__dict__:
        for key in list(objCopy.__dict__):
            try:
                if key in 'objclass':
                    del objCopy.__dict__[key]
                    continue 
                
                if objCopy.__dict__[key] is None or not objCopy.__dict__[key] :
                    del objCopy.__dict__[key]
                    continue

                if key.startswith('_') :
                    objCopy.__dict__[key[1:len(key)]] = objCopy.__dict__.pop(key)
                    key = key[1:len(key)]

                if key.endswith('_') :
                    objCopy.__dict__[key[0:len(key) - 1]] = objCopy.__dict__.pop(key)

            except AttributeError as identifier:
                continue
    
        return objCopy.__dict__
    return None