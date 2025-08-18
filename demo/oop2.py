# Class Methods
# This is a function in a class

class Woman():
    name = "Maria"
    age = 20
    colour = "Brown"
    def cook():
        return f"{Woman.name} cooks nicely!"
        return (Woman.name,"cooks nicely")
# a method is a function of a class that describes what an object does to itself or to others
# it descibes the behaviour of a class
# statements within a method of a class is a behaviour
# A behaviour describes how an object does something/acts
# any other statements below return are ignored or considered as comments
print(Woman.cook())

# creating new instance of a woman 
woman2 = Woman()
woman2.name = "Martha"
woman2.age = 21
woman2.colour = "dark"
# print(woman2.cook())  This statement will result in an error because the method cook only applies to Maria



