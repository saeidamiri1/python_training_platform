#File: mp6.py
import time
import os
from multiprocessing import Process, Pipe

def prod(x, pipe_conn):
    square = 0
    even_numbers = []

    for i in x:
        time.sleep(1)
        square += i * i
        print(f"Process {os.getpid()} is calculating square of {i}")
        if i % 2 == 0:
            even_numbers.append(i)

    # Send both results via pipe: even numbers + square sum
    pipe_conn.send((even_numbers, square))
    pipe_conn.close()

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent_conn, child_conn = Pipe()

    p = Process(target=prod, args=(x, child_conn))
    p.start()

    # Receive result
    even_numbers, total_square = parent_conn.recv()

    print("\nEven numbers:", even_numbers)
    print("Total sum of squares:", total_square)

    p.join()