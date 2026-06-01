import functools
import json
import os

def cache(filename, key_type='args'):
    def decorator(func):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    storage = json.load(f)
                except json.JSONDecodeError:
                    storage = {}
        else:
            storage = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if key_type == 'args':
                key = str(args)
            else:
                key = str(kwargs)

            if key not in storage:
                result = func(*args, **kwargs)
                storage[key] = result
                
                with open(filename, 'w') as f:
                    json.dump(storage, f)
            
            return storage[key]
        return wrapper
    return decorator
