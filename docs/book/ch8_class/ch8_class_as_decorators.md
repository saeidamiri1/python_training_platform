---
title: Class as Decorator
---



# Class as Decorator

https://realpython.com/primer-on-python-decorators/#using-classes-as-decorators


You can write the class as decorator, in this case you need take the function as an argumnet in `_init_`. Let 
write a class that count the number of time that the class executed.

```python
class count_run:
    def __init__(self, func):
        self.func = func
        self.num = 0
    def __call__(self, *args, **kwargs):
        self.num += 1
        print(f"Execute # {self.num} of {self.func.__name__}()")
        return self.func(*args, **kwargs)


@count_run
def print_me():
    print("ThAnKs")

print_me()
```