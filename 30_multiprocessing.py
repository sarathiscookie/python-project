# Multiprocessing: Multiprocessing refers to the ability of a system to support more than one processor at the same time.
# Note: Multiprocessor library is for dividing work between multiple processes.
# Multiprocessor: i.e. a computer with more than one central processor.

import multiprocessing

def cube_function(num):
    print(f"Cube: {num * num * num}")

def square_function(num):
    print(f"Square: {num * num}")

if __name__ == "__main__":

    process_one = multiprocessing.Process(target = cube_function, args = (10, ))

    process_two = multiprocessing.Process(target = square_function, args = (10, ))

    # starting process 1
    process_one.start()

    # starting process 2
    process_two.start()

    # wait until process 1 is finished
    process_one.join()

    # wait until process 2 is finished
    process_two.join()

    # both processes finished
    print("Done!")

    """
    Cube: 1000
    Square: 100
    Done!
    """
