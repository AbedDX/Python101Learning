# Import the threading module to work with threads
import threading

# Define a function to print the square of a given number
def print_square(num):
    print("Square:{}",format(num*num))

# Define a function to print the cube of a given number
def print_cube(num):
    print("Cube:{}",format(num*num*num))

# Define the main function
def main():
    # Create two thread objects, one for printing squares and the other for printing cubes
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # Start both threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    # Print "Done" when both threads are finished
    print("Done")

# Check if this script is the main program being run
if __name__ == "__main__":
    # If it is, call the main function
    main()
