# Another way of how to create classes
class Animal:
# fuction__init__ is a special method we use as a special constructor
    """
     
The first parameter in the constructer, self, 
is used to identify/link the property, attribute,
 of a class to the parameters

    """
    def __init__(self,name,age,owner,colour,skintexture,taste):
        self.name = name
        self.age = age
        self.owner = owner
        self.colour = colour
        self.skintexture = skintexture
        self.taste = taste


animal1 = Animal("cow", 10, "Janet", "white", "smooth", "Delicious")

# Create 5 classes in this with atleast five properties and make it in a dynamice way

# class 1

class Shoes:
    def __init__(self,name,brand,colour):
        self.name = name
        self.brand = brand
        self.colour = colour
shoes1 = Shoes("sneakers","nike","pink")

# class 2

class Meat:
    def __init__(self,name,type,taste):
        self.name = name
        self.type = type
        self.taste = taste
meat1 = Meat("beef","red","delicious")

# class 3
class Cars:
    def __init__(self,name,brand,colour):
        self.name = name
        self.brand = brand
        self.colour = colour
car1 = Cars("G-Wagon","Mercedes","black")

# class 4







        





