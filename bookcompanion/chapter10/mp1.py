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