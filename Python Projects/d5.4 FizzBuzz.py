
for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print ("FizzBuzz") 
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print (number)


print(["FizzBuzz" if i%3 == 0 and i%5 == 0 else "Buzz" if i%5 == 0 else "Fizz" if i%3 == 0 else i for i in range(1,101)])


"""
The second code block works without using elif by leveraging a conditional expression (also known as a ternary operator). 
In Python, a conditional expression has the form x if condition else y, where x is the value to be returned if the condition is True, 
and y is the value to be returned if the condition is False.
"""