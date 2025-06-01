---
title: functools
---

# functools 

functools is a module that provides tools for working with functions and other callable objects.

## partial
One of its useful is ```partial``` which allows write and maintain the existing functions to achieve new purpose.
The following function shows how to rewrite the t-test in a way just calculate the p-value.. 

```python
from functools import partial
import numpy as np
import scipy.stats
x, y = np.random.normal(0, 1, (100,2)).T
ttest_0=partial(scipy.stats.ttest_ind, equal_var=False)

def ttest_NE(x,y):
   return print("p-value=",ttest_0(x,y)[1])

ttest_NE(x,y)
```


## wraps

`wraps` can be used to write a decorators in Python, by using @wraps, you can preserves that metadata by copying it from the original function to the wrapper function.


``` python 
from functools import wraps

def do_nothing_decorator(f):
   @wraps(f)
   def wrapper(*args, **kwds):
          print('INSIDE DECORATOR: This is called before function')
          return f(*args, **kwds)
   return wrapper

@do_nothing_decorator
def hello_world():
  """This is a hello world function"""
  print("AAA")

```

Let run this function 
``` python 
>>> hello_world()
INSIDE DECORATOR: This is called before function
AAA
>>> print(f"Function Name: {hello_world.__name__}")
Function Name: hello_world
>>> print(hello_world.__doc__)
This is a hello world function
```

Now let run without the wrape

``` python 
def do_nothing_decorator(f):
   def wrapper(*args, **kwds):
          print('INSIDE DECORATOR: This is called before function')
          return f(*args, **kwds)
   return wrapper

@do_nothing_decorator
def hello_world():
  """This is a hello world function"""
  print("AAA")
```

``` python 
>>> hello_world()
INSIDE DECORATOR: This is called before function
AAA
>>> print(f"Function Name: {hello_world.__name__}")
Function Name: wrapper
>>> print(hello_world.__doc__)
None
```

So, wraps ensures the decorated function retains its original identity. 


