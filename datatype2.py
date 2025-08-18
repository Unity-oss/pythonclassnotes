animals = ["rabbit", "cow", "Dog", "goat", "Cat"]
animals.append("donkey")
print(animals)
animals.pop()
print(animals)

cars = []
cars.append("toyota")
print(cars)
# A list is mutable 
# The tuple is immutable
numbers = ()
# numbers.append()
animals.insert(1,"lion")
print(animals)

# Mapping
# dictionary/dict {} :
student = {"name": "Unity", "age": 45, "location": "Mukono"}
print(student["age"])
print(student.keys())
print(student.values())

# Set: this is an unordered collection of unique items {} 
student_ids = {112, 114, 116, 116, 118, 118, 115}
print(student_ids)