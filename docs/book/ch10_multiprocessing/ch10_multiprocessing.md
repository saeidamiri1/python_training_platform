---
title: Multiprocessing
---

# Multiprocessing
Python has the ability to handle multiple tasks simultaneously or in parallel, allowing it to take full advantage of multiple cores and processors. In this section, we briefly discuss how to perform parallel computation using Python.

In general, multiprocessing (or parallel processing) refers to the use of two or more processors by an application to perform tasks in parallel. Each process runs independently and has its own allocated resources. To enable communication between these separate processes, the concept of Inter-Process Communication (IPC) must be used.

Multiprocessing is particularly useful when tasks are: CPU-bound, Can be executed independently, Require minimal data sharing between them

Python provides two main ways to implement multiprocessing: the Pool class and the Process class. In the following sections, we will first explore the Pool method, and then examine how to use the Process class for parallel execution.


## Getting Started
To see how many CPUs are available on your computer, 
```python
import multiprocessing
multiprocessing.cpu_count()
```

## Pool method 
Pool.map() is the parallel equivalent of Python’s built-in map() function. To run computations in parallel, you first create a pool of worker processes—typically based on the number of available CPU cores. If the number of processes is not specified, Pool will use all available CPU cores by default.

<!-- os.chdir('/Volumes/F/python_training_platform0/python_training_platform/bookcompanion/chapter10/') -->

```python
#name mp1.py
from multiprocessing import Pool
import os
import time

def prod(x):
    print(f"Now Process {os.getpid()} | is calculating square {x}")
    return x * x

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with Pool(processes=4) as pool:
        result = pool.map(prod, x)
    
    print(f"Partial results: {result}")
    print(f"Total sum of squares: {sum(result)}")
    print('Done')
```
Here, os.getpid() prints the process ID, helping you see which worker handled which task. Alternative ways to use Pool.map()
You can also create the pool without specifying the number of processes (it defaults to all available CPUs):

```python
with Pool() as pool:
    result = pool.map(defs.sq, x)
```

Or by manually managing the pool:

```python
pl = Pool(4)
result = pl.map(defs.sq, x)
pl.close()
```

Limitation of Pool.map(): The Pool.map() function accepts only a single iterable, which means it supports only one argument per target function. To handle functions with multiple arguments, you can use Pool.starmap(), which we'll explore next.



### Multiple arguments
If your target function requires multiple arguments, you can use pool.starmap(), which allows unpacking argument tuples for parallel execution. In the below, we use Pool.starmap() with a Function that Takes Two Arguments
First, add the following code to a file named mp2.py

```python
#File: mp2.py
from multiprocessing import Pool
import os
import time

def prod(x,y):
    print(f"Now Process {os.getpid()} | is calculating  {x} times {y}")
    return x * y

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y=x[::-1]
    xy=zip(x,y)
    with Pool() as pool:
      result = pool.starmap(prod, xy)
    
    print(f"Partial results: {result}")
    print(f"Total sum of squares: {sum(result)}")
    print('Done')
```
```
# Output 
Now Process 47902 | is calculating  1 times 9
Now Process 47902 | is calculating  2 times 8
Now Process 47902 | is calculating  3 times 7
Now Process 47902 | is calculating  4 times 6
Now Process 47902 | is calculating  5 times 5
Now Process 47902 | is calculating  6 times 4
Now Process 47902 | is calculating  7 times 3
Now Process 47902 | is calculating  8 times 2
Now Process 47902 | is calculating  9 times 1
Partial results: [9, 16, 21, 24, 25, 24, 21, 16, 9]
Total sum of squares: 165
Done
```

Note on Blocking Behavior: A major limitation of Pool.map() and Pool.starmap() is that they are blocking operations — the main (master) process is paused until all results are returned.
To avoid blocking and run computations asynchronously, you can use map_async() or starmap_async(), which allow concurrent execution without halting the main process.

```python
xx=zip(x,x)
xy=zip(x,y)
with Pool() as pool:
    p1 = pool.map_async(prod, xx).get()
    p2 = pool.map_async(prod, xy).get()
```
.get() blocks until the results are ready, but you can omit it or delay it to keep the main process responsive.

### Parallel vs serial process
Let compare the parallel and serial  processing here: 
```python
#File: mp3.py
import time
from multiprocessing import Pool

import os
import time

def prod(x):
    print(f"Now Process {os.getpid()} | is calculating square {x}")
    time.sleep(2)
    return x * x

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with Pool(processes=4) as pool:
        start_parallel = time.time()
        result = pool.map(prod, x)
        end_parallel = time.time()
# Sequential processing
    start_sequential = time.time()
    result_sequential = list(map(prod, x))
    end_sequential = time.time()
    print("Time for Parallel Processing: {:.4f} seconds".format(end_parallel - start_parallel))
    print("Time for Sequential Processing: {:.4f} seconds".format(end_sequential - start_sequential))
```
```
Now Process 58957 | is calculating square 1
Now Process 58958 | is calculating square 2
Now Process 58959 | is calculating square 3
Now Process 58960 | is calculating square 4
Now Process 58959 | is calculating square 5
Now Process 58958 | is calculating square 6
Now Process 58957 | is calculating square 7
Now Process 58960 | is calculating square 8
Now Process 58959 | is calculating square 9
Now Process 58955 | is calculating square 1
Now Process 58955 | is calculating square 2
Now Process 58955 | is calculating square 3
Now Process 58955 | is calculating square 4
Now Process 58955 | is calculating square 5
Now Process 58955 | is calculating square 6
Now Process 58955 | is calculating square 7
Now Process 58955 | is calculating square 8
Now Process 58955 | is calculating square 9
Time for Parallel Processing: 6.0465 seconds
Time for Sequential Processing: 18.0376 seconds
```




## Process method
Another approach is to use the Process class directly from the multiprocessing module:
```python
#File: mp4.py
import multiprocessing
import os
import time

def prod(x, results, key):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()} | is calculating square {i}")
    results[key] = square

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y=x[::-1]
    results = {}
    p1 = multiprocessing.Process(target=prod, args=(x, results, "res1"))
    p2 = multiprocessing.Process(target=prod, args=(y, results, "res2"))
    # Start task execution
    p1.start()
    p2.start()
    # Wait for process to complete execution
    p1.join()
    p2.join()
    print('Done')
```
```
# Output
Now Process 62187 | is calculating square 1
Now Process 62188 | is calculating square 9
Now Process 62187 | is calculating square 2
Now Process 62188 | is calculating square 8
Now Process 62188 | is calculating square 7
Now Process 62187 | is calculating square 3
Now Process 62187 | is calculating square 4
Now Process 62188 | is calculating square 6
Now Process 62188 | is calculating square 5
Now Process 62187 | is calculating square 5
Now Process 62188 | is calculating square 4
Now Process 62187 | is calculating square 6
Now Process 62188 | is calculating square 3
Now Process 62187 | is calculating square 7
Now Process 62188 | is calculating square 2
Now Process 62187 | is calculating square 8
Now Process 62188 | is calculating square 1
Now Process 62187 | is calculating square 9
Done
```
In the example above: We define a function prod() to calculate the sum of squares of numbers in a list. We use a multiprocessing.Manager().dict() to share results between processes. We initiate Process objects with target function and arguments, start them with start(), and wait for completion using join(). Unlike the Pool method, the Process approach provides more granular control over individual processes. However, it does not automatically manage worker allocation or load balancing across CPU cores — this has to be handled manually. Let me know if you’d like a visual or table-based comparison of Process vs Pool.



## Sharing data 
Each process has its own memory and CPU, meaning that data stored in one process’s memory is not directly accessible to others. Therefore, to work with shared data across processes, a communication mechanism is needed — this is known as Inter-Process Communication (IPC). Sharing objects between processes requires explicitly passing data through such communication channels. The Python multiprocessing module provides several built-in methods for IPC, including Pipes, Queues, Managers, and shared memory. In this section, we will explore how to use these tools to enable efficient communication between processes.

### Queues
To pass data between processes, we can use a Queue from the multiprocessing module. In the following example, if a number is even, it is placed into the queue for further processing or communication.

```python
#File: mp5.py
import multiprocessing
import os
import time

def prod(x, q, results, key):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()} | is calculating square {i}")
        if i % 2 == 0:
            q.put(i)
    results[key] = square

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y=x[::-1]
    results = {}
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=prod, args=(x, q1, results, "res1"))
    p2 = multiprocessing.Process(target=prod, args=(y, q2, results, "res2"))
    # Start task execution
    p1.start()
    p2.start()
    # Wait for process to complete execution
    p1.join()
    p2.join()
    def printqueue(q):
        while not q.empty():
            print("Received:", q.get())
    printqueue(q1)
    printqueue(q2)
    print('Done')
```
```
Now Process 10493 | is calculating square 1
Now Process 10494 | is calculating square 9
Now Process 10493 | is calculating square 2
Now Process 10494 | is calculating square 8
Now Process 10493 | is calculating square 3
Now Process 10494 | is calculating square 7
Now Process 10493 | is calculating square 4
Now Process 10494 | is calculating square 6
Now Process 10493 | is calculating square 5
Now Process 10494 | is calculating square 5
Now Process 10493 | is calculating square 6
Now Process 10494 | is calculating square 4
Now Process 10494 | is calculating square 3
Now Process 10493 | is calculating square 7
Now Process 10493 | is calculating square 8
Now Process 10494 | is calculating square 2
Now Process 10493 | is calculating square 9
Now Process 10494 | is calculating square 1
Received: 2
Received: 4
Received: 6
Received: 8
Received: 8
Received: 6
Received: 4
Received: 2
```

### Pipes
In multiprocessing, Pipes are primarily used for communication between processes. A pipe consists of two connection objects, each with send() and recv() methods for sending and receiving data. Below is an example that demonstrates how to use a pipe:

```python 
#File: mp6.py
import time
import os
from multiprocessing import Process, Pipe

def prod(x, pipe_conn):
    square = 0
    even_numbers = []

    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Process {os.getpid()} is calculating square of {i}")
        if i % 2 == 0:
            even_numbers.append(i)

    # Send both results via pipe: even numbers + square sum
    pipe_conn.send((even_numbers, square))
    pipe_conn.close()

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent_conn, child_conn = Pipe()

    p = Process(target=prod, args=(x, child_conn))
    p.start()

    # Receive result
    even_numbers, total_square = parent_conn.recv()

    print("\nEven numbers:", even_numbers)
    print("Total sum of squares:", total_square)

    p.join()
```

```
#Output: 
Process 19746 is calculating square of 1
Process 19746 is calculating square of 2
Process 19746 is calculating square of 3
Process 19746 is calculating square of 4
Process 19746 is calculating square of 5
Process 19746 is calculating square of 6

Even numbers: [2, 4, 6]
Total sum of squares: 91
```

### Manager
The multiprocessing.Manager provides a safe way to share different types of objects—such as dictionaries, lists, and more—between processes. It works by running a separate server process that holds the shared objects and allows other processes to access and modify them through proxies.

```python 
#File: mp7.py
import time
import os
from multiprocessing import Process, Manager
def prod(x, results, key):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Process {os.getpid()} is calculating square of {i}")
    results[key] = square  # Shared dictionary gets updated
if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    manager = Manager()
    results = manager.dict()  # Shared dictionary
    p = Process(target=prod, args=(x, results, 'square_sum'))
    p.start()
    p.join()

    print("Total sum of squares:", results['square_sum'])
```
```
# Output
Process 25894 is calculating square of 1
Process 25894 is calculating square of 2
Process 25894 is calculating square of 3
Process 25894 is calculating square of 4
Process 25894 is calculating square of 5
Process 25894 is calculating square of 6
Process 25894 is calculating square of 7
Process 25894 is calculating square of 8
Process 25894 is calculating square of 9
Total sum of squares: 285
```

### shared_memory
Since Python 3.8, the multiprocessing.shared_memory module has been introduced, allowing data to be shared efficiently between processes—especially useful for large data structures like NumPy arrays. In the example below, we demonstrate how to define and use a shared array.

```python 
#File: mp8.py
import numpy as np
import multiprocessing
from multiprocessing import shared_memory

def read_data(shm_name):
    shm = shared_memory.SharedMemory(name=shm_name)
    data = np.ndarray((4,), dtype=np.float64, buffer=shm.buf)
    print("Data imported:", data[:])
    shm.close()

if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=4 * np.float64().nbytes)
    arr = np.ndarray((4,), dtype=np.float64, buffer=shm.buf)
    arr[:] = [1.1, 2.2, 3.3, 4.4]

    p = multiprocessing.Process(target=read_data, args=(shm.name,))
    p.start()
    p.join()

    shm.close()
    shm.unlink()
```
```
#Output
Data imported: [1.1 2.2 3.3 4.4]
```

Now let's define a more advanced function that saves the final result in shared memory.

```python 
#File: mp9.py
import os
import time
import numpy as np
import multiprocessing
from multiprocessing import shared_memory

def prod(x, shm_name, index):
    # Connect to the shared memory block
    shm = shared_memory.SharedMemory(name=shm_name)
    results = np.ndarray((10,), dtype=np.int64, buffer=shm.buf)  # shape must match main array
    # Compute sum of squares
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Process {os.getpid()} is calculating square of {i}")
    # Write result to shared memory at given index
    results[index] = square
    shm.close()

if __name__ == "__main__":
    # Create shared array with 10 slots (adjust as needed)
    shm = shared_memory.SharedMemory(create=True, size=10 * np.int64().nbytes)
    results = np.ndarray((1,), dtype=np.int64, buffer=shm.buf)
    results[:] = 0  # Initialize
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p = multiprocessing.Process(target=prod, args=(x, shm.name, 0))
    p.start()
    p.join()
    print("Final shared memory results:", results[:])
    shm.close()
    shm.unlink()  # Clean up shared memory

```
```
#Output
Process 46286 is calculating square of 1
Process 46286 is calculating square of 2
Process 46286 is calculating square of 3
Process 46286 is calculating square of 4
Process 46286 is calculating square of 5
Process 46286 is calculating square of 6
Process 46286 is calculating square of 7
Process 46286 is calculating square of 8
Process 46286 is calculating square of 9
Final shared memory results: [285]
```