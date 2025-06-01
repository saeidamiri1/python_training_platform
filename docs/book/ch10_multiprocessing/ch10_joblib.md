---
title: Joblib
---

# Joblib

`joblib` provides a simple way to write parallel computation,  which can be used to to efficently serialized the large data. 

## Parallel Processing
Here we look how to used joblib to do parallel process: 

```python
#name joblib1.py
import os
import time
from joblib import Parallel, delayed

def prod(x):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()}  | is calculating square {i}")
    return square

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Split list into chunks for parallel processing
chunks = [x[0:5],x[6:8] ]  # split into 4 chunks

import multiprocessing as mp
num_cores = mp.cpu_count()

results = Parallel(n_jobs=num_cores-1,verbose=1)(delayed(prod)(chunk) for chunk in chunks)

print("Partial results:", results)
print("Total sum of squares:", sum(results))
```
```
[Parallel(n_jobs=11)]: Using backend LokyBackend with 11 concurrent workers.
Now Process 8249  | is calculating square 1
Now Process 8254  | is calculating square 7
Now Process 8249  | is calculating square 2
Now Process 8254  | is calculating square 8
Now Process 8249  | is calculating square 3
Now Process 8249  | is calculating square 4
Now Process 8249  | is calculating square 5
[Parallel(n_jobs=11)]: Done   2 out of   2 | elapsed:    5.1s finished
Partial results: [55, 113]
Total sum of squares: 168
```
delayed is used to capture the arguments of the target function, in this case, the prod. We run the above code (with num_cores-1) CPUs, if you want to use all of computational power on your machine. You can use all CPUs on your machine by setting n_jobs=-1. If you set it to -2, all CPUs but one are used. Here, we turn on the verbose argument (verbose=1) to output the status messages
The function can be done using pool workers

```python
with Parallel(n_jobs=num_cores-1) as parallel:
  results = parallel(n_jobs=num_cores-1,verbose=1)(delayed(prod)(chunk) for chunk in chunks)
```


There are multiple backends in joblib, which provides different ways to do the parallel computing. If you set the backend as multiprocessing, it creates a multiprocessing pool that uses separate Python woker processes to execute tasks concurrently on separate CPUs. 

```python
import os
import time
from joblib import Parallel, delayed
import multiprocessing

def prod(x):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()}  | is calculating square {i}")
    return square

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Split list into chunks for parallel processing
    chunks = [x[0:5],x[6:8] ]  # split into 4 chunks
    import multiprocessing as mp
    num_cores = mp.cpu_count()
    results = Parallel(n_jobs=num_cores-1,backend='multiprocessing',verbose=1)(delayed(prod)(chunk) for chunk in chunks)
    print("Partial results:", results)
    print("Total sum of squares:", sum(results))
```

This function will run each function in isolated process, so the parallel function needs the shared memory semantics of threads, it can be done via require='sharedmem': 

```python
results = Parallel(n_jobs=num_cores-1, require='sharedmem',verbose=1)(delayed(prod)(chunk) for chunk in chunks)
```

## Serializing object
In this chapter, we review how to use Pickle-like tools to store data. When working with large objects or machine learning models, the joblib library offers an efficient and convenient way to serialize and save them to disk. This is especially useful for storing models after training or for caching intermediate results. Here’s a simple example using joblib:

```python
from joblib import dump, load
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dump(weights, 'x.joblib')  # Save model
weights = load('x.joblib') # Load model
```


## Caching Computations
One can use  Memory to get rid of repition of computation, 

```python
from joblib import Memory
mem = Memory(location='cachedir', verbose=0)
@mem.cache
def func_time(x):
    time.sleep(4)
    return x ** 2

@mem.cache
def prod(x):
    square = 0
    start_parallel = time.time()
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()}  | is calculating square {i}")
    end_parallel = time.time()
    print(f"Total time:  {end_parallel-start_parallel}")
    return square


prod(x)
prod(x)
```
```
#Output: 
>>> prod(x)
Now Process 79813  | is calculating square 1
Now Process 79813  | is calculating square 2
Now Process 79813  | is calculating square 3
Now Process 79813  | is calculating square 4
Now Process 79813  | is calculating square 5
Now Process 79813  | is calculating square 6
Now Process 79813  | is calculating square 7
Now Process 79813  | is calculating square 8
Now Process 79813  | is calculating square 9
Total time:  9.02702784538269
285
>>> prod(x)
285
```

## Share data 
When working with multiprocessing, it's important to use memory-efficient techniques. By default, when data is passed to child processes, it gets copied—this can lead to high memory usage, especially with large datasets.

To avoid this, joblib provides support for shared memory when using NumPy arrays and similar data structures. This allows multiple processes or threads to access the same data without duplication, improving both performance and efficiency.

Let’s review how to use joblib with sharedmem to compute row-wise means on a NumPy array:
```python
import numpy as np
from joblib import Parallel, delayed

# Create a random dataset
data = np.random.rand(100, 1000)

# Function to compute the mean of a specific row
def mean_row(i):
    return np.mean(data[i])

# Use joblib with shared memory to avoid copying large arrays between processes
result = Parallel(n_jobs=4, require='sharedmem')(
    delayed(mean_row)(i) for i in range(data.shape[0])
)

print(result)
```

Note: require='sharedmem' ensures that data is not copied between processes, and instead is shared efficiently. This technique works best when using threads (n_jobs > 1 with require='sharedmem') and is especially helpful with large NumPy arrays. Make sure your function only reads from the shared data (no in-place modifications) to avoid race conditions.
