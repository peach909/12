from functools import wraps

def tag(t):
    def decorator_func(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            value = func(*args, **kwargs)
            return f'<{t}>{value}<{t}>'
        return wrapped
    return decorator_func

print("Введите строку: ")
str = input()

@tag('div')
def decrease(s):
    return s.lower()

print(decrease(str))
