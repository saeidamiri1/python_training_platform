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