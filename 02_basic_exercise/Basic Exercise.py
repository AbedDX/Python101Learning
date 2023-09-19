# Exercise 1: Calculation
def Multi(a, b):
    # Multiplies the numbers a and b
    result = a * b
    return result

def Sum(a, b):
    # Sums up the numbers a and b
    result = a + b
    return result

# Exercise 2: Range
def currentnum():
    print("Printing current and previous number and their sum in a range(10)")
    previous_num = 0

    # Loop from 1 to 10
    for i in range(1, 11):
        x_sum = previous_num + i
        print("Current Number", i, "Previous Number", previous_num, "Sum:", x_sum)
        # Modify previous number by setting it to the current number
        previous_num = i

# Exercise 3: Print characters from a string that are present at an even index number
def word0():
    word = "pynative"
    x = list(word)
    for i in x[0::2]:
        print(i)

# Exercise 4: Remove first n characters from a string
def word1():
    word = "pynative"
    x = list(word)
    for i in x[4::]:
        print(i)

# Exercise 5: Check if the first and last number of a list is the same
def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("Result is", first_last_same(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print("Result is", first_last_same(numbers_y))

# Exercise 6: Display numbers divisible by 5 from a list








def main():
    print("Result of Multi:", Multi(20, 30))
    print("Result of Sum:", Sum(40, 30))
    currentnum()
    word0()
    word1()
    result_x = first_last_same(numbers_x)
    print("Result for numbers_x:", result_x)
    result_y = first_last_same(numbers_y)
    print("Result for numbers_y:", result_y)

if __name__ == "__main__":
    main()
