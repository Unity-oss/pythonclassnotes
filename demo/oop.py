# OOP: this is a programming structure or arrangement/paradigm/a way of writing computer instructions basing on real world classes or objects.
# A class is a blue print of an object
# An object is an instance of a class

class Food():
    name = "matooke"
    price = 20000
    market = "owino"
    owner = "mercy"

# A class should always start with a capital letter
# create another instance of food 
irish_potatoes = Food()
irish_potatoes.name = "irish_potatoes"
irish_potatoes.price = 15000
irish_potatoes.market = "Owino"
irish_potatoes.owner = "Alinda"

chicken = Food()
chicken.name = "chicken"
chicken.price = 35000
chicken.market = "KFC"
chicken.owner = "Tracy"

print(irish_potatoes.name)

