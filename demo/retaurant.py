# Design a simple restaurant now
# should be able to add different foods and their prices
# should be able to add different drinks and their prices
# should be able to allow differnt editing different foods and items
# this should be done by only a logged in user 
# should be able to register the user who is going to use the system

# what do we need to be able to solve this?

class newuser:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
name = input("Enter your name")
email = input("Enter your email")
password = input("Enter your password")
user1 = input(newuser(name,email,password))
print("user1")

        
