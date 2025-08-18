def modify():
    name = input("Enter your name")
    print(f"{name}, Below is your net salary calculated")
    gross = int(input("Enter your gross salary "))
    is_local = input("Are you a local employee? (yes/no): ")
    if gross <= 300000:
        tax = 0
        nssf = 0
    elif gross <= 700000:
        tax = 0
        nssf = 0.11
    else:
        if is_local == "yes":
            tax = 0.30
            nssf = 0.11
        else:
            tax = 0.35
            nssf = 0.11
    tax = gross * tax
    nssf = gross * nssf
    deduction = tax + nssf
    net = gross - deduction
    print("Your net pay is: ", net)
modify()

    
