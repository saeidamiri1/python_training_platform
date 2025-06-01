#File: mp8.py
import numpy as np
import multiprocessing
from multiprocessing import shared_memory

def read_data(shm_name):
    shm = shared_memory.SharedMemory(name=shm_name)
    data = np.ndarray((4,), dtype=np.float64, buffer=shm.buf)
    print("Data imported:", data[:])
    shm.close()

if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=4 * np.float64().nbytes)
    arr = np.ndarray((4,), dtype=np.float64, buffer=shm.buf)
    arr[:] = [1.1, 2.2, 3.3, 4.4]

    p = multiprocessing.Process(target=read_data, args=(shm.name,))
    p.start()
    p.join()

    shm.close()
    shm.unlink()
