import functools

def cache(func):
    storage = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in storage:
            storage[args] = func(*args)
        
        return storage[args]
    
    return wrapper

@cache
def my_sum(a, b):
    return a + b

if __name__ == '__main__':
    print(my_sum(2, 3))
    print(my_sum(2, 3))
