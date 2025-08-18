num = int(input("Enter a number: "))

if num % 2 != 0:
    print("Weird")
elif num % 2 == 0 and num in  range(3,15):
    print("not weird")
elif num % 2 == 0 and num in range(5,30):
    print("weird")
elif num > 50:
    print("not weird")
    
