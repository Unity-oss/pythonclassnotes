# Categories of static functions
# user_definned functions and pre_defined functions(language specific)
# pre-defined are functions that come with python such as type, insert, input, append, print

# An example of a static fuction (values won't change)
def my_func():
    num1 = 50
    num2 = 100
    print(num1 + num2)
# calling the function
my_func()

# An example of a dynamic function (values will change)
def my_func2(num1, num2):
    print(num1 + num2)
# calling the function
my_func2(80, 100)
my_func2(100, 200)
my_func2(1000, 2000)

# A parameter is a value put in a def parenthesis. 
# An argument is a value put in a def parenthesis when calling the function.
# An argument is a value to the parameter.
# parameter list is the number of paremetors to  function
# arguments must be full_filling to the parameter list

def addition(a, b):
    print(a + b)
addition(10,20)


def multiply(a, b):
    print(a * b)
multiply(10,20)


def division(a, b):
    print(a / b) 
division(10,20) 

def subtraction (a, b):
    print(a - b) 
subtraction(10,20)