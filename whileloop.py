# While loop
# A while loop is a way to repeat something again and again in Python as long as a certain condition is true.
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# Print i as long as i is less than 6:

# while
gender = 1
while gender < 16:
  print(gender)
  gender += 1

# breakstatement
  girl = 1
while girl < 6:
  print(girl)
  if girl == 3:
    break
  girl += 1

# continue statement
  boy = 0
while boy < 6:
  boy += 1
  if boy == 3:
    continue
  print(boy)

# else statement
  car = 1
while car < 6:
  print(car)
  car += 1
else:
  print("car is no longer less than 6")


