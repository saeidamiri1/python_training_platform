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
