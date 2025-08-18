for number in range(10):
    # Below means if a number is divided by 2 and you get 0, print that number.
    if number % 2 == 0:
        print(number)

for number in range(10):
    # if a number is divided by 2 and the reminder is not 0 , print number.
    if number % 2 != 0:
        print(number)

for number in range(10):
    if number % 2 == 1:
        print(number)

# here we are inputing range from user
my_num = int(input("please input your range of numbers:"))
for number in range(my_num):
    if number % 2 == 0:
        print(number)

for number in range(my_num):
    if number % 2 != 0:
        print(number)

# my list with loops
my_list = [10, 20, 30,40, 50, 60,70, 80, 90, 100]
for number in my_list:
        print(number)




