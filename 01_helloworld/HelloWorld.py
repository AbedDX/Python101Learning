print("Hello World!")

def main():
    number = 0
    if number > 0:
        print("Number is positive")
    elif number == 0:
        print("Number is Zero")
    else:
        print("Number is negative")
    for x in "pyhton":
        print(x)
    values = range(4)
    for i in values:
        print(i)
    numbers =[0,1,2,3,4,5]

    for j in numbers:
        print(j)
    else:
        print("Done")
    i = 1
    n = 5
    while i <= n:
        print(i)
        i = i + 1

    counter = 0
    while counter < 3:
        if counter == 1:
            break
        print("Inside loop")
        counter = counter + 1
    else:
        print("Done")    
   
    a = 0
    if a == 0:
        pass
    a = 100
    b = 200
    if a<b:
        print("B is great")


if __name__ == "__main__":
    main()

from flask import Flask
app = Flask(__name__)
