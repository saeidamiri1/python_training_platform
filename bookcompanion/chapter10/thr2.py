import threading
import os
import time

def prod(x, results, key):
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Now Process {os.getpid()} | Thread Name {threading.current_thread().name} | is calculating square {i}")
        print("Daemon thread is running...")
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
    print("Main thread will sleep for 3 seconds.")
    time.sleep(3)
    print("Main thread exiting... Daemon thread will be killed.")