# we print out a welcoming note to the employee
# get a variable to store the gross salary of the employee
# get a variable to store the PAYE rate 
# get a varible to keep the calculation of net pay vs grosspay (tax rate multiplied by the grosspay)
# get a variable that will store the netpay after the tax from the variable above is deducted from the grosspay
# end with a message that will print out the nt pay from the abvove to an employee

print("Welcome maria! Below is your net salary calculated")
gross, tax = 500000, 0.3
tax = 500000*0.3
print(tax)
netpay = gross - tax
print(netpay)
print("Your net pay is: ", netpay)


def netpay():
    print("Welcome maria! Below is your net salary calculated")
    gross, tax = 500000, 0.3
    tax = 500000*0.3
    net = gross - tax
    print("Your net pay is: ", net)
netpay()


def netpay(gross, tax):
        print("Welcome maria! Below is your net salary calculated")
        tax = gross * tax
        net = gross - tax
        print("Your net pay is: ", net)
netpay(500000,0.30)



    
