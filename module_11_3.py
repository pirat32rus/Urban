import inspect
import types

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    
    module = getattr(obj, '__module__', '__main__')

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }
    
    if isinstance(obj, (list, dict, set, str)):
        info['length'] = len(obj)
    
    return info
number_info = introspection_info(42)
print(number_info)