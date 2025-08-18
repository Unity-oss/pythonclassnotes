def netpay():
    print("welcome maria! Below is your netpay")
gross, tax, nssf = 500000, 0.3, 0.115
tax = tax = 500000 * 0.3
nssf = 500000 * 0.115
deduction = tax + nssf
netpay = gross - deduction
gross = input("Enter your gross salary ")
nssf = input("Enter your nssf:")
tax = input("Enter your tax: ")
print(netpay)
netpay()