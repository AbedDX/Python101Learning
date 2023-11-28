#FileNotFound Catching Exceptions: The try catch except finally Pattern and Raising your own Exceptions

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])

# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as erro_message:
#     print(f"The key{erro_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError


# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3  meters.")
# bmi = weight/ height ** 2
# print(bmi)