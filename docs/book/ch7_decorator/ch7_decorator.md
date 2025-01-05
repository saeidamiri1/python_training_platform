

# Decorators
Decoreators in Python allows you to take a function and add additional uses without modifying its structure (to wrap one function with another function), the following example show how add meesage befor and after exsiting function

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


# Decorators with function's arguments
If your function needs any argument, you can pass it using `*arg`" 
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
```
 `*args` allows you to pass the arguments of function to the inner wrapper function. 


The decorator often simplify using`@name of decorator`

```python
@my_decor
def square(x):
    print(x*x)
```


Let define a function to check the time running a function: 

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
Or you can do it as below where  `*args` and `**kwargs` are to support positional and named arguments of fn. 
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
we can apply multiple decorators to a single function by placing them one after the other, with the most inner decorator being applied first.
You use the apply multiple decorators on a single function. 

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

Sometimes, it’s useful to pass arguments to your decorators. For instance, @do_twice could be extended to a @repeat(num_times) decorator. The number of times to execute the decorated function could then be given as an argument.

If you define @repeat, you could do something like this:

You can pass arguments to the decorators as well
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

# Creating Decorators With Optional Arguments

The following example show how to run a decorator in a way that 
if the argument is no given, ignore it.  

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

# Tracking State in Decorators
Some times, you can keep the track of state in the decorator,  the following the  `inner` is the inner function  and `inner.num` keep
the track of run


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


