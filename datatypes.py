# Datatypes in python
# These are categories of values to be stored in a memory
# Grouping of values to be stored in a computer
# 1. Numeric
# 2. String
# 3. List
# 4. Tuple
# 5. Dictionary
# 6. Set
# 7. Boolean
# 8. None
# 9. Sequence
# 10. Mapping

# Numeric 
# 1. integers
# 2. Floats
# 3. complex

print(type(100))
print(type(100.0))
print(type("100"))
print(type(1+2j))

# String
# a value in quotes is a string
# we dont quote numerics or float
name = "Unity"
gender ="Female"
school = "Groundbreaker"
print(type(name))

#Sequence
 # list
 # tuple
 #range
#List 
#this is a collection of values put into square brackets separated by commas
my_country = ["UGANDA", "Kenya", "Tanzania", "Rwanda"]
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
my_stuff = [my_country, fruits, numbers]
print(my_stuff)
#values in a list are indexed starting from 0 from left to right and -1 from right to left
print(my_country[0])
print(my_country[2])
print(my_country[3])
print(numbers[2])
print(my_stuff[0][3])
print(my_stuff[2][4])
print(my_stuff[1][1])

numero = [10,[20,40,[60, 80,[[100],[200]]]]]
print(numero[1][2][2][1][0])

#Tuple
#identified by a pair of parenthesis()
numbers2 = (1, 2, 3, 4, 5)
print(numbers2[0])
print(numbers2[-2])
print(range(10))
print(numbers2[-4])
print(numbers2[-5])

numeral = [10,[20,40,[60, 80,[[100],[200]]]]]

