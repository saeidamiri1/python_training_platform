#File: mp9.py
import os
import time
import numpy as np
import multiprocessing
from multiprocessing import shared_memory

def prod(x, shm_name, index):
    # Connect to the shared memory block
    shm = shared_memory.SharedMemory(name=shm_name)
    results = np.ndarray((10,), dtype=np.int64, buffer=shm.buf)  # shape must match main array
    # Compute sum of squares
    square = 0
    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Process {os.getpid()} is calculating square of {i}")
    # Write result to shared memory at given index
    results[index] = square
    shm.close()

if __name__ == "__main__":
    # Create shared array with 10 slots (adjust as needed)
    shm = shared_memory.SharedMemory(create=True, size=10 * np.int64().nbytes)
    results = np.ndarray((1,), dtype=np.int64, buffer=shm.buf)
    results[:] = 0  # Initialize
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    p = multiprocessing.Process(target=prod, args=(x, shm.name, 0))
    p.start()
    p.join()
  

    print("Final shared memory results:", results[:])

    shm.close()
    shm.unlink()  # Clean up shared memory
