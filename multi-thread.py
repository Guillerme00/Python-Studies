import threading
import time

#Multi-Threading

#Creating two functions

def square(numbers):
    for numb in numbers:
        time.sleep(2)
        print(f'{numb * numb} square')

def cube(numbers):
    for numb in numbers:
        time.sleep(2)
        print(f'{numb ** numb} cube')


if __name__ == '__main__':
    ## Creating a list of numbers to be passed as arguments to the functions
    numbers=[2,3,4,2,3,4]

    ## Defining the functions as threads and passing the list as an argument
    t1 = threading.Thread(target=square, args=(numbers,))
    t2 = threading.Thread(target=cube, args=(numbers,))

    #First, we have to start the functions with 'start()'
    t1.start()
    t2.start()

    # After starting the threads, we call join() to make the program wait
    # until the threads finish their execution
    t1.join()
    t2.join()

    # The threads run concurrently and may alternate execution
    # t1, t2
    # t2, t1
    # t1, t2
    # t2, t1

    print("Finish")

    # This program demonstrates concurrency using Python threads.
    # Although the threads run concurrently, with GIL (Python's Global Interpreter Lock)
    # allows only one thread to execute Python at a time.

    # However, when a thread performs a blocking operation such as time.sleep(),
    # the GIL is released, allowing another thread to continue execution.

