# partial
functools is a module that includes higher-order functions. One of its useful is ```partial``` which allows write and maintain the existing functions to achieve new purpose.

```{python, echo = FALSE, message = FALSE}
from functools import partial
import numpy as np
import scipy
import scipy.stats
x, y = np.random.normal(0, 1, (100,2)).T
ttest_0=partial(scipy.stats.ttest_ind, equal_var=False)

def ttest_NE(x,y):
   return print("p-value=",ttest_0(x,y)[1])

ttest_NE(x,y)
```



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

hello_world()

print(f"Function Name: {hello_world.__name__}")

Function Name: hello_world

from functools import wraps
import time
def instrument(f):
   @wraps(f)
   def wrap(*args, **kw):
       ts = time.time()
       result = f(*args, **kw)
       te = time.time()
       print(f"function: {f.__name__}, args: [{args}, {kw}] took: {te-ts} sec")
       return result
   return wrap

@instrument
def lazy_work(x,y, sleep=2):
   """Sleeps then works"""
   time.sleep(sleep)
   return x+y

lazy_work(4,9)

