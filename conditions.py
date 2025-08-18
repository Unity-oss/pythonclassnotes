# Conditions
# if, else, elif 
number = 10 
if number > 0:
    print(number)
if number < 0:
    print("Hello, World!")

animals = ["goats", "cat", "dog"]
if "goats" in animals:
    print("goats")

if "rabbits" in animals:
    print("rabbit")
else: 
    print("Rabbits is not part of the animal list")

# Below, we are inputing a value from the keyboard directly to the variable my_input
# NOTE: input() takes everything as strings by default
# int(input()) converts a value from a string to an input.


my_input = int(input("please input your number: "))
if my_input < 0:
    print("the number you input is negative")
else:
    print("the number you have input is positive")

if my_input % 2 == 0:
    print("the number input is an even number")
else:
    print("the number is an odd number")


