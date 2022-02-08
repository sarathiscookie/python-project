# Multithreading: Multithreading is a way of achieving multitasking. In multithreading the concept of threads is used.
# Thread: Thread is an entity within a process that can be scheduled for execution. (It is a subset of process).
# Thread Synchronization: Thread synchronization is defined as a mechanism which ensure that two or more concurrent threads do not simultaneously execute some particular program segment known as critical section.
# join(): The current program will first wait for the completion of t1 and then t2. Once, they are finished, the remaining statements of current program are executed.

import threading

def cube_func(num):
    print(f"Cube: {num * num * num}")

def square_func(num):
    print(f"Square: {num * num}") 

if __name__ == "__main__":

    thread_one = threading.Thread(target = cube_func, args = (10, ))

    thread_two = threading.Thread(target = square_func, args = (10, ))

    # starting thread 1
    thread_one.start()

    # starting thread 2
    thread_two.start()

    # wait until thread 1 is completely executed
    thread_one.join()

    # wait until thread 2 is completely executed
    thread_two.join()

    print("Done!")

"""
Cube: 1000
Square: 100
Done!
"""

