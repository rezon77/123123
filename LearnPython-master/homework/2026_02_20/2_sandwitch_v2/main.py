import functools

def bread(func):
    @functools.wraps(func)
    def wrapper():
        return f"Bread\n{func()}\nBread".strip()
    return wrapper

def salat(func):
    @functools.wraps(func)
    def wrapper():
        return f"Salat\n{func()}".strip()
    return wrapper

def tomato(func):
    @functools.wraps(func)
    def wrapper():
        return f"Tomato\n{func()}".strip()
    return wrapper

def meat(func):
    @functools.wraps(func)
    def wrapper():
        return f"Meat\n{func()}".strip()
    return wrapper

@bread
@salat
@tomato
@meat
def make_sandwich():
    return ''

def main():
    print(make_sandwich())

if __name__ == '__main__':
    main()
