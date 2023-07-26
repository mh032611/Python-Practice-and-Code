# Basic Programming notes

# https://www.youtube.com/watch?v=_uQrJ0TkZlc&
# Strings

name = 'Jennifer'

print(name[1:-1]) # output: ennife

################################################################################

# formatted strings (f-strings)

first = 'John'
last = 'Smith'

message = first + ' [' + last + '] ' + "is a coder."

print(message)

msg = f"{first} [{last}] is a coder."

print(msg)

################################################################################
#                                   String Methods 

course = 'Python for Beginners'
print(len(course)) # output: 20
# can also use len function to calculate numbers of items in a list
# note that print and len are general functions so they dont belong to anything, 
# therefore they are built-in functions and NOT methods


# String Methods 
## When a function is belongs to something else or is specific to some kind of object
## we call it a "method".
# course.upper() # for example this method .upper() is specific to strings

print(course.upper()) # output: PYTHON FOR BEGINNERS 
# note that this does not permanently change the course variable.
# instead it creates a new version that is uppercase. 

print(course.lower()) # output: python for beginners

print(course) # output: Python for Beginners (output is the original, unchanged)

# find and replace
 
# Find allows you to find the index of what you're searching for
print(course.find('P')) # output: 0 (meaning that the first instance of charcter 'P' occurs at index 0)
print(course.find('o')) # output: 4 (because index 4 is the first instance of lowercase o)
print(course.find('O')) # output: -1 (there are no instances of letter uppercase "O")
print(course.find('n')) # output: 5 (because index 5 is the first instance of lowercase n)



print(course.find('Beginners')) # output: 11 (because it starts at index 11)

print(course.replace('Beginners', 'Absolute Beginners')) # output: Python for Absolute Beginners

print(course.replace('P', 'J')) # output: jython for Beginners

# if you want to know if there is a string in the variable use the 'in' operator 

print('Python' in course) #output: True 
#the difference between in operator and find method returns the index but in operator returns a boolean value


#augmented assignment opperator

x = 10
# x = x + 3
# print (x)
# augmented assignment opporator 
x += 3 
print (x)

# Opperator precidence 

# paranthesis
# exponents 2**3
# multiplication or division
# addition or subtraction 

################################################################################

# Math Functions
x = 2.9
print(round(x)) # outcome: 3

print(abs(-1)) # outcome: 1 you will always get the positive representation of the value using the "absolute" value of this function

import math #import the math module to use all the different methods available in the math object

print(math.floor(2.9)) #outcome: 2

# search python 3 math module for more mathematical functions and their explanations 

################################################################################

#                                if statements 

is_hot = True
is_cold = False

if is_hot:
   print("hot day")
   print(f"drink plenty of water because it is a {is_hot}ly hot day.")
elif is_cold:
   print("cold day")
else: 
   print("beautiful day")

house_price = 1_000_000 #remember that underscores on not recognized in naming python variables 

print (f"${house_price}")
good_credit = True

if good_credit == True:
    down_payment = (house_price * 0.10)
else:
    down_payment = (house_price * 0.20)

down_payment_formatted = "{:.2f}".format(down_payment) # output: 100000.00 ensures that 2 decimals show 

print (f"Your down payment is: ${down_payment_formatted}")


################################################################################

#                                Logical Operators


#if an applicant has high income and good credit is Eligible for a loan
has_high_income = True
has_good_credit = True

if has_high_income == True and has_good_credit == True:
   print("You're eligible for a loan")

#if an applicant has high income OR good credit is Eligible for a loan

if has_high_income == True or has_good_credit == True:
   print("You're eligible for a loan")

# AND: Both
# OR: at least one
# NOT (inverses any boolean value that you give)

# and not operator
# if applicant has good_credit AND doesn't have a criminal record, they're eligible for a loan. 

has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Approved for a loan")
else:
    print("You don't meet the criteria for a loan")

################################################################################

#                           comparison operators
# if temperature is greater than 30, its a hot day. otherwise if its less than 10, 
# its a cold day. otherwise its neither hot nor cold. 

temperature = 30

if temperature > 30:
   print ("It's a hot day")
elif temperature < 10:
   print ("It's a cold day")
else:
   print("It's neither hot nor cold today.")

# if name is less than 3 characters long name, name must be at least 3 characters. 
# otherwise if it's more than 50 characters long, name can be a maximum of 50 characters.
# otherwise, name looks good.

name = input("What is your name?")
name_length = len(name)

if name_length < 3:
   print("Name must be at least 3 characters long")
elif name_length > 50:
   print("Name can be a maximum of 50 characters")
else:
   print("Name looks good.")

################################################################################


################################################################################


################################################################################


################################################################################


################################################################################





################################################################################




################################################################################





################################################################################
