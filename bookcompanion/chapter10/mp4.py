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
