# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = []

# for letter in range (0, nr_letters):
#   password.append(random.choice(letters))

# for symbol in range (0, nr_symbols):
#   password.append(random.choice(symbols))

# for number in range (0, nr_numbers):
#   password.append(random.choice(numbers))

# password = "".join(password) #This joins elements of list or array without any spaces. https://www.pythonmorsels.com/turn-a-list-into-a-string/

# print(password)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# #There is a function shuffle in the random module. Note that it shuffles in-place so you first have to convert your string to a list of characters, shuffle it, then join the result again.(https://stackoverflow.com/questions/2668312/shuffle-string-in-python)

# password_as_list = list(password) #in order to use random.shuffle() you need to convert the string back to a list 

# random.shuffle(password_as_list)


# scrambled_password_string = ''.join(password_as_list)

# print(scrambled_password_string)

###########################################################################################################################

#Practice

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(0, nr_letters):
    # password.append(random.choice(letters))
    password += random.choice(letters)

for number in range(0, nr_numbers):
    password.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    password.append(random.choice(symbols))

password = "".join(password)

print(password)

