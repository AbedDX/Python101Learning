# Import the sleep function from the time module to introduce delays
from time import sleep

# Import the randint function from the random module to generate random values
from random import randint

# Import the Thread class from the threading module to work with threads
from threading import Thread

# Import the Lock class from the threading module to create a lock for synchronization
from threading import Lock

# Define a function 'task' that simulates some work with synchronization
def task(lock, id, value):
    # Acquire the lock to ensure only one thread can enter this block at a time
    with lock:
        print("{} thread acquiring lock".format(id))
        print("Will sleep for {} seconds".format(value))
    
    # Simulate some work by sleeping for 'value' seconds
    sleep(value)

# Define the main function
def main():
    # Create a Lock object to be used for synchronization
    lock = Lock()

    # Create 10 threads, each with a unique 'id' and a random 'value' for sleep
    for i in range(10):
        # Start a new thread, passing the 'lock', 'id', and 'value' as arguments to the 'task' function
        Thread(target=task, args=(lock, i, randint(0, 5))).start()

# Check if this script is the main program being run
if __name__ == "__main__":
    # If it is, call the main function to start the threads
    main()
