

- [Contents]
- [Getting Started]
  - [map]
  - [Parallel in joblib]
- [References](#references)

## Getting Started
To see how many CPUs are available on your computer, 
```{python, echo = FALSE, message = FALSE}
import multiprocessing
multiprocessing.cpu_count()
```

### map 
`Pool.map` is equvalent to `map`function, to run the computation parallely, 
first create a pool of workers for a given number of CPU.  If the number of processes is defined, it use all cpu.  First create ca file and save you function,

```python
# def.py
def sq(x):
    return x * x
```


```python
from multiprocessing import Pool
x = [1, 2, 3, 4, 5, 6]

import defs
with Pool(processes=4) as pool:
    result = pool.map(defs.f, x)

with Pool() as pool:
    result = pool.map(defs.sq, x)
```

If your argument has multiple arguments, one can consider `pool.starmap`, 

```python
x1 = [1, 2, 3, 4]
x2 = [2, 3, 4, 5]
xx=zip(x1,x2)

with Pool() as pool:
    result = pool.starmap(defs.sq2, xx)
```

A major problem is in blocking the process until finishing the computation, multiprocessing has asynchronous function that block the master process until the function is done.  

```python
x1 = [1, 2, 3, 4]
x2 = [2, 3, 4, 5]

def sqb(x):
   return x * x

with Pool() as pool:
    r1 = pool.map_async(defs.sq, x1).get()
    r2 = pool.map_async(defs.sq, x2).get()
```



### Parallel in joblib
joblib provides a simple way to write parallel computation, 

```python
def sq2(x,y):
   return x * y

import  multiprocessing
num_cores = multiprocessing.cpu_count()
from joblib import Parallel, delayed
xx=list(x)
ab=Parallel(n_jobs=num_cores-1)(delayed(sq2)(xx[i],xx[i]) for i in range(5))
```



The function can be done using pool workers

```{python, echo = FALSE, message = FALSE}
with Parallel(n_jobs=num_cores-1) as parallel:
  ab=parallel(delayed(sq2)() for x11,x12 in xx)
```


This function will run each function in isolated process. so the parallel function needs the shared memory semantics of threads, it can be done via require='sharedmem': 

```{python, echo = FALSE, message = FALSE}
xx=zip(x1,x2)
shared_set = []
def collect(x,y):
    shared_set.append(x*y)

Parallel(n_jobs=2, require='sharedmem')(delayed(collect)(x11,x12) for x11,x12 in xx)
shared_set
```



# https://superfastpython.com/multiprocessing-pool-starmap/#How_to_Use_Poolstarmap
from random import random
from time import sleep
from multiprocessing.pool import Pool
 
def task(identifier, value):
    print(f'Task {identifier} executing with {value}', flush=True)
    sleep(value)
    return (identifier, value)

with Pool() as pool:
    # prepare arguments
    items = [(i, random()) for i in range(10)]
    # execute tasks and process results in order
    for result in pool.starmap(task, items): 
        print(f'Got result: {result}', flush=True)
    # process pool is closed automatically


if item is big use  chunksize=2
with Pool() as pool:
    # prepare arguments
    items = [(i, random()) for i in range(10)]
    # execute tasks and process results in order
    for result in pool.starmap(task, items, chunksize=2): 
        print(f'Got result: {result}', flush=True)
    # process pool is closed automatically

#####
http://pymotw.com/2/multiprocessing/basics.html
discussed about .join, daemon, and terminate(). 

We can explicitly wait for the new process to finish executing by calling the join() function.

https://superfastpython.com/multiprocessing-in-python/


##################################### how return value 
from random import random
from time import sleep
from multiprocessing import Queue
from multiprocessing import Process


def print_func(continent,queue):
    print('The name of continent is : ', continent)
    data = random()
    # block, to simulate computational effort
    print(f'Generated {data}', flush=True)
    sleep(data)
    queue.put(data)

names = ['America', 'Europe', 'Africa']
procs = []
value=[]
for name in names:
    # print(name)
    queue = Queue()
    proc = Process(target=print_func, args=(name,queue,))
    procs.append(proc)
    proc.start()
    # wait for the return value
    value0 = queue.get()
    value.append(value0)
    print(f'Returned: {value}')

for proc in procs:
    proc.join()
    


## References