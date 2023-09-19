def main():
    greet()  # Calls the greet function to print a greeting.
    add(5, 10)  # Calls the add function to calculate and print the sum of 5 and 10.
    subtract(50, 25)  # Calls the subtract function to calculate and print the result of 50 - 25.


def greet():
    print("Hello World")  # Prints a simple greeting message.

def add(a, b):
    result = a + b  # Calculates the sum of two numbers.
    print("Sum is:", result)  # Prints the calculated sum.

def subtract(a=0, b=0):
    result = a - b  # Calculates the result of subtracting b from a.
    print("Result is:", result)  # Prints the calculated result.



if __name__ == "__main__":
    main()