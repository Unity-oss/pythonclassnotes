# function to handle numbers
def number_handler(num_list):
# get input from the user
    number1 = input("please enter your number ")
#append to list 
    num_list.append(number1)


def menu_option():
    print("please select your desired operation")
    print("1. Enter number")
    print("2. Enter string")
    print("3. Quit")

def main():
# show menu to the user
    menu_option()
    # initial num_list variable
    number_list = []
    while True:
        user_choise = input("enter your desired choice")
        if user_choise == 1:
            number_handler(number_list)
        else:
            break
    print(number_list)
main()
