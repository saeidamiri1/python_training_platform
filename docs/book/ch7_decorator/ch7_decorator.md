---
title: Decorators
---

# Decorators
Decorators in Python allow you to enhance or modify the behavior of a function without changing its original structure. They work by "wrapping" one function with another. Decorators are a powerful and clean way to add functionality such as logging, access control, timing, or caching.

The following example shows how to add a message before and after an existing function runs:

```Python
def wrapper(func):
   def inner_fun():
       print("Before calling function.")
       print("-" *10)
       func()
       print("-" *10)
       print("After calling function.")
   return inner_fun

def print_me():
    print('ThAnKs')

print_me()
print_me = wrapper(print_me)
print_me()   
```

Decorators are often used in a simplified form with the `@decorator_name` syntax placed above the function definition.

```python
@wrapper
def print_me2():
    print('ThAnKs')

print_me2()
```

##  Function's arguments
If your function takes arguments, you can pass them using `*args` in the decorator.

```Python
def wrapper(func):
   def inner_fun(*arg):
       print("Before calling function.")
       func(*arg)
       print("After calling function.")
   return inner_fun

def square(x):
    print(x*x)

square(4)
square = wrapper(square)
square(4)   

# OR user simplifier
@my_decor
def square(x):
    print(x*x)
square(4)
```

In this function, `*args` is used to pass positional arguments from the original function to the inner wrapper function.

To explore how `*args` works, let's define a decorator that measures the execution time of a function:

```python
import time
start_time = time.time()

def timestamp_Check(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args) # calls the addition function
        print('Total running time')
        print(time.time()-start_time)
        return result
    return wrapper

@timestamp_Check
def pow(a, b):
    return(a**b)
    
pow(10, 10)
```

Alternatively, you can write it as shown below, where `*args` and `**kwargs` are used to support the positional and keyword arguments of the function being decorated.

```python
def timeit(fn): 
    def get_time(*args, **kwargs): 
        start = time.time() 
        output = fn(*args, **kwargs)
        print(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn
    return get_time

@timeit
def pow(a, b):
    return(a**b)

pow(10, 10)
```

## Chaining Decorators
We can apply multiple decorators to a single function by placing them one after the other, with the innermost decorator (the one closest to the function) being applied first.

This allows you to layer functionality by using multiple decorators on a single function.

``` python
def wrapper (fn): 
    def inner_print(*args, **kwargs): 
        print("------------")
        output = fn(*args, **kwargs)
        print("------------")
        return output  # make sure that the decorator returns the output of fn
    return inner_print

@wrapper
@timeit
def pow(a, b):
    return(a**b)

pow(10, 10)
```

## Defining Decorators With Arguments
Sometimes, it’s useful to pass arguments to decorators. For example, the `@do_twice` decorator could be extended to a `@repeat(num_times)` decorator, where the number of times to execute the decorated function is given as an argument.

To define a `@repeat` decorator, you could implement it like this: You can pass arguments to decorators in a similar manner.


``` python 
def repeat(num_times):
    def wrapper(func):
        def inner(*args, **kwargs):
            print("#-*" * num_times)
            value = func(*args, **kwargs)
            return value
        return inner
    return wrapper

@repeat(num_times=5)
def print_me(x):
    print(f"Hey {x}")

print_me("Friend")
```

## Optional Arguments
The following example shows how to define a decorator that ignores the argument if it is not provided.

``` python
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat
def print_me1():
      print("ThAnKs")


@repeat(num_times=3)
def print_me2(name):
    print(f"ThAnKs {name}")

say_whee()
greet("SAM")
```

## Tracking State
Sometimes, you can keep track of the state within the decorator. In the following example, `inner` is the inner function, and `inner.num` keeps track of the number of times the function has been called.


```python 
def count_runs(func):
    def inner(*args, **kwargs):
        inner.num += 1
        print(f"count {wrapper.num} of {func.__name__}()")
        return func(*args, **kwargs)
    inner.num = 0
    return wrapper

@count_runs
def print_me():
     print("ThAnKs")
```
