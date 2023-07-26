# Import the random module here

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


x = random.randint(0,(len(names)-1))

print(f"{names[x]} is going to buy the meal today!")

#You can also use the .choice method. The above code was used to learn that lists start at zero and how to use randomization using numerical values

person_who_will_pay_choice = random.choice(names)
print(person_who_will_pay_choice + " is going to buy the meal today!")
