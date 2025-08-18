# Operators are words or symbols or characters that tell a computer(CPU) what to do with an operand.
# Operand is a value
# Arithemetic operators (Mathematical)
# Assignment operators
# COMPARISON OPERATORS
# Logical operators
# Bitwise operators
# Special operators

# Arithmetic operators
# Adition operator (+)
num1, num2 = 20, 30
print(num1 + num2)
# Subtraction operator (-)
print(num2 - num1)
# Multiplication operator (*)
print(num1 * num2)
# Division operator (/)
print(num2 / num1)
# Floor division operator (//)
print(num2 // num1)
# Power operator (**)
print(num1 ** num2)
# Modulus operator (%)
print(num1 % 2)
print(2 % num1)

#Assignment operators
my_num = 200
# += Addition Assignment
num3 = 10
num3 += 5 # num3 = num3 + 5
print(num3)
# -= Subtraction Assignment
num3 -= 5 # num3 = num3 - 5
# /= Division Assignment
num3 /= 5 # num3 = num3 / 5
# *= Multiplication Assignment
num3 *= 5 # num3 = num3 * 5
# %= Modulus Assignment
num3 %= 5 # num3 = num3 % 5


#Comparison operators
print(10 == 10)
print(10 =="10")
print(10 < 10)
print(10 > 10)
print(10 <= 10)
print(10 >= 10)
print(10 != 10)                        


#Logical operators
# and, or, not
num5, num6 = 5, 6 
print((num5 > 2) and (num6 >= 6))
print((num5 < 2) and (num6 >= 6))

# or 
print((num5 > 2) or (num6 >= 6))
print((num5 < 2) or (num6 >= 6))
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not True)
print(not False)


# Special operators

# Identity operators
# is, is not
print(True is True)
print(True is not True)
print(True is not False)
print(False is not False)

# Membership operators
# in, not in
print()
mynums = [10, 20, 30, 40, 50]
print(10 in mynums)
print(10 not in mynums)
print(100 in mynums)
print(100 not in mynums)

name = "Unity"
print("U" in name)
print("z" in name)

# Bitwise operators
