# functions by default do not share anything from themselves to other functions
def add():
    num1, num2 = 20, 30
    print(num1 + num2)

add()

print(add())

def multiply():
    num1, num2 = 45, 55
    return(num1 * num2)

multiply()

print(multiply())
number = multiply()
print(number + 100)


