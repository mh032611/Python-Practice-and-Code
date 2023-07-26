#For Loop and the Range Function

for number in range (1, 11, 3):
  print(number)
# 3 is a step-into number. counts by 3
# 1, 4, 7, 10 

total = 0
for number in range(1, 101):
  total += number
print(total)

####################################################################################################

total = 0 

for number in range(2, 101, 2):
  total += number

print (total)

#Alternate way using modulo to get even numbers

total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number

print (total)

#############################################################################################################################################

#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

#For Loop with Range

for number in range(1, 100):
  print(number)

for number in range(1, 101):
  print(number)

for number in range(1, 11, 3):
  print(number)

#Calculating the sum of all the numbers from 1 to 100.
total = 0
for number in range(1, 101):
  total += number
print(total)

##############################################################################################################################################

# My FizzBuzz Code 

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print ("FizzBuzz") 
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print (number)