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