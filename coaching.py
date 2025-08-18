def user_menu():
    print("please select your desired operation")
    print("1. Enter number")
    print("2. Enter string")
    print("3. quit")

#capture user option
# if the user option is a number, add it to the list of numbers that you created
# if the user input is a string, add it to the list of strings
# if the user input is quit, print out the list of string and numbers to show what the user entered
#NOTE: the user should be able to continuosly interact with the system unless they quit

def unity():
    user = 1
    number_list = []
    string_list = []
    while user == 1:
        choose = input("Enter options(1, 2, 3):")

        if choose =="1":
            num = int(input("Enter a number"))
            number_list.append(num)
            
        elif choose =="2":
            str = int(input("Enter string"))
            string_list.append(str)
        elif choose =="3":
            print("Enjoy the weekend, bye")
            break 
        else:
            print("Invalid option please select 1, 2, 3")

    print("this is your list of numbers", number_list)
    print("this is your list of strings", string_list)

unity()
     
    



