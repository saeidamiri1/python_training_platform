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