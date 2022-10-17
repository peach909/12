from functools import wraps
>>> def tag(t):
...     def decorator_func(func):
...         @wraps(func)
...         def wrapped(*args, **kwargs):
...             value = func(*args, **kwargs)
...             return f'<{t}>{value}<{t}>'
...         return wrapped
...     return decorator_func
...
>>> tag('h1')
... def to_lower(s):
...     return s.lower()
...
>>>
>>> to_lower('PYTHON')
'<h1>python<h1>'
>>>
>>> tag('div')
... def to_lower(s):
...     return s.lower()
...
>>>
>>> to_lower('PYTHON')
'<div>python<div>'