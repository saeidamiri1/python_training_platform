#name mp2.py
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

