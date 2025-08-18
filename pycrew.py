#Using dynamic,static and an interactive function,write a 
# python code to demonstrate employees net pay after tax and nssf
def static():
    print("Welcome Alpha to your Employee_netpay")
    gross, tax, nssf = 300000, 0.3, 0.11
    taxrate = gross * tax
    nssf_rate = gross * nssf
    expense = taxrate + nssf_rate
    netpay = gross - expense
    print("Dear employee, this is your netpay: ", netpay)
static()

# dynamic function
def dynamic(gross, tax, nssf):
    print("Welcome Alpha to your Employee_netpay")
    tax_amount = gross * tax
    nssf_amount = gross * nssf
    deduction = tax_amount + nssf_amount
    netsalary = gross - deduction
    print(netsalary)
dynamic(800000, 0.3, 0.11)

# interactive functions
def interactive():
    print("Welcome Alpha to your Employee_netpay")
    gross = int(input("Enter your grosspay: "))
    tax = float(input("Enter your tax: "))
    nssf = float(input("Enter your nssf: "))
    tax_amount = gross * tax
    nssf_amount = gross * nssf
    deduction = tax_amount + nssf_amount
    netsalary = gross - deduction
    print(netsalary)
interactive()

