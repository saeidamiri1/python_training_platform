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