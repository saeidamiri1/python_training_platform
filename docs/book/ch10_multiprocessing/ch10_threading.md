---
title: Multithreading
---

# Multithreading
Unlike multiprocessing, multithreading executes multiple threads concurrently within the same process. These threads share the same memory space, allowing for efficient communication and data sharing. Multithreading is especially useful for I/O-bound tasks, such as reading files from a network or querying a database, as it allows multiple threads to handle I/O operations simultaneously without blocking each other. In contrast, multiprocessing is more suitable for CPU-bound tasks, as it leverages multiple processors to perform parallel computations—similar to how multicore systems outperform single-core systems for intensive computations.

## threading
Python has a built-in module called threading that is used to implement multithreading. The following example demonstrates how to use the threading module to run code concurrently.

```python
#name thr1.py
import threading
import os
import time

def prod(x, results, key):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()} | Thread Name {threading.current_thread().name} | is calculating square {i}")
    results[key] = square
        
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x1 = x[0:5]  
    x2 = x[5:9]  
    results = {}
    p1 = threading.Thread(target=prod, name="p1", args=(x1, results, "res1"))
    p2 = threading.Thread(target=prod, name="p2", args=(x2, results, "res2"))

    # Start task execution
    p1.start()
    p2.start()

    # Wait for threads to complete
    p1.join()
    p2.join()

    total = results["res1"] + results["res2"]
    print(f"Partial results: {results}")
    print(f"Total sum of squares: {total}")
    print('Done')


# result 1:  running python3 thr1.py
Now Process 14075 | Thread Name p1 | is calculating square 1
Now Process 14075 | Thread Name p2 | is calculating square 6
Now Process 14075 | Thread Name p1 | is calculating square 2
Now Process 14075 | Thread Name p2 | is calculating square 7
Now Process 14075 | Thread Name p1 | is calculating square 3
Now Process 14075 | Thread Name p2 | is calculating square 8
Now Process 14075 | Thread Name p1 | is calculating square 4
Now Process 14075 | Thread Name p2 | is calculating square 9
Now Process 14075 | Thread Name p1 | is calculating square 5
Partial results: {'res2': 230, 'res1': 55}
Total sum of squares: 285
Done

# result 2: running python3 thr1.py
Now Process 13794 | Thread Name p1 | is calculating square 1
Now Process 13794 | Thread Name p2 | is calculating square 6
Now Process 13794 | Thread Name p2 | is calculating square 7
Now Process 13794 | Thread Name p1 | is calculating square 2
Now Process 13794 | Thread Name p2 | is calculating square 8
Now Process 13794 | Thread Name p1 | is calculating square 3
Now Process 13794 | Thread Name p1 | is calculating square 4
Now Process 13794 | Thread Name p2 | is calculating square 9
Now Process 13794 | Thread Name p1 | is calculating square 5
Partial results: {'res2': 230, 'res1': 55}
Total sum of squares: 285
Done

```

You can see that both threads share the same process ID, which confirms that they are part of the same process. Additionally, the output is not generated in a strict sequential order. For example, the first line might be produced by thread1, while the second and third lines are from thread2, followed again by output from thread1, and so on.

In Result 2, a rerun of the code shows that the order of thread execution has changed, highlighting the non-deterministic nature of thread scheduling.

It's important to note that concurrency does not necessarily mean parallel execution. In the case of multithreading in Python (especially due to the Global Interpreter Lock, or GIL), only one thread runs at a time. As a result, it doesn’t actually reduce the total execution time compared to sequential execution. Instead, the CPU switches between threads—pausing one, starting another, and later returning to resume the previous thread from where it left off. This thread switching is what gives the appearance of concurrency but does not achieve true parallelism.

## Daemon Threads
A daemon thread is a background thread that runs alongside the main thread but does not block the main thread’s execution. It runs continuously in the background and is automatically terminated when the main thread finishes, even if the daemon thread is still running or hasn't completed its task.

In Python, daemon threads are often used for background tasks such as garbage collection or housekeeping operations that should not prevent the program from exiting. When the main thread ends, all daemon threads are stopped abruptly.

To create a daemon thread in Python, you can set the daemon property to True, either using p1.setDaemon(True) (for backward compatibility) or more commonly:

```python
#name thr1.py
import threading
import os
import time

def prod(x, results, key):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()} | Thread Name {threading.current_thread().name} | is calculating square {i}")
    results[key] = square


        
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x1 = x[0:5]  
    x2 = x[5:9]  
    results = {}
    p1 = threading.Thread(target=prod, name="p1", args=(x1, results, "res1"))
    p1.daemon = True  # Set as daemon thread
    # Start task execution
    p1.start()

# result :  running python3 thr2.py
Main thread will sleep for 3 seconds.
Now Process 20890 | Thread Name p1 | is calculating square 1
Daemon thread is running...
Now Process 20890 | Thread Name p1 | is calculating square 2
Daemon thread is running...
Main thread exiting... Daemon thread will be killed.
```

## Threading in joblib
Let’s use threading with joblib.

```python
#name thr2.py
import threading
import os
import time
from joblib import Parallel, delayed

def prod(x):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()} | Thread Name {threading.current_thread().name} | is calculating square {i}")
    return square

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Split list into chunks for parallel processing
chunks = [x[0:5],x[6:8] ]  # split into 4 chunks

results = Parallel(n_jobs=4, backend='threading')(delayed(prod)(chunk) for chunk in chunks)

print("Partial results:", results)
print("Total sum of squares:", sum(results))

# result : running python3 thr2.py
Now Process 10956 | Thread Name Thread-2 (worker) | is calculating square 7
Now Process 10956 | Thread Name Thread-1 (worker) | is calculating square 1
Now Process 10956 | Thread Name Thread-2 (worker) | is calculating square 8
Now Process 10956 | Thread Name Thread-1 (worker) | is calculating square 2
Now Process 10956 | Thread Name Thread-1 (worker) | is calculating square 3
Now Process 10956 | Thread Name Thread-1 (worker) | is calculating square 4
Now Process 10956 | Thread Name Thread-1 (worker) | is calculating square 5
```

Now, let's consider the multiprocessing case—you'll notice that the process IDs have changed.

```python
results = Parallel(n_jobs=4)(delayed(prod)(chunk) for chunk in chunks)
# result :
Now Process 15654 | Thread Name MainThread | is calculating square 1
Now Process 15657 | Thread Name MainThread | is calculating square 7
Now Process 15654 | Thread Name MainThread | is calculating square 2
Now Process 15657 | Thread Name MainThread | is calculating square 8
Now Process 15654 | Thread Name MainThread | is calculating square 3
Now Process 15654 | Thread Name MainThread | is calculating square 4
Now Process 15654 | Thread Name MainThread | is calculating square 5
```
