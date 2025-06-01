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

