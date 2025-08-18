# using a static function
print("Welcome maria! Below is your net salary calculated")
gross, tax, nssf = 500000, 0.3, 0.115
tax = 500000 * 0.3
nssf = 500000 * 0.115
deduction = tax + nssf
netpay = gross - deduction
print("Your net pay is: ", netpay)

# using dynamic functions
def netpay(gross, tax, nssf):
        print("Welcome maria! Below is your net salary calculated")
        tax = gross * tax
        nssf = gross * nssf
        deduction = tax + nssf
        net = gross - deduction
        print("Your net pay is: ", net)
netpay(500000,0.30,0.115)

# using interactive function


def netpay(gross, tax, nssf):
        print("Welcome maria! Below is your net salary calculated")
        gross = int(input("Enter your gross salary "))
        nssf = float(input("Enter your nssf:"))
        tax = float(input("Enter your tax: "))
        tax = gross * tax
        nssf = gross * nssf
        deduction = tax + nssf
        net = gross - deduction
        print("Your net pay is: ", net)
netpay(500000,0.30,0.115)


# if someone is earning 300000 and below, -----> no tax
# 300001 to 700000-----> nssf
# 700001 and a local -----> 30% + nssf
# 700000 and non local-----> 35% tax 