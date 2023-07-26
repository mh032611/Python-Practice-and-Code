print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age < 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 18 and age < 45:
    bill = 12
    print("Adult tickets are $12.")
  elif age >= 45 and age <= 55:
    print("Midlife tickets are $0.")
    bill = 0
  else:
    bill = 12
  want_photos = input("Do you want photos? Enter 'Y' or 'N'.")
  if want_photos == "Y":
    bill += 3
else:
  print("You Cant Ride, need to be at least 120 cm Tall")

statement = f"The total bill is ${bill}"

print(statement)