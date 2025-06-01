---
title: Class as Decorator
---

# Class as Decorator
You can write a class as a decorator, a technique where a class is used to modify the behavior of a function, similar to how a regular function decorator works. In this case, you need to take the function as an argument in `__init__`. Let’s write a class that counts the number of times the class method is executed.

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