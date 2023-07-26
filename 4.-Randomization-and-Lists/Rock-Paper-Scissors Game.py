import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
'''
https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
Rules of Rock Paper Scissors
1. Rock wins against scissors.
2. Scissors win against paper.
3. Paper wins against rock.
'''

player_choice = input(
    "Please enter your choice of 'Rock', 'Paper', or 'Scissors'").lower()

if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":  # case of user entering invalid entry
    print("You need to choose a valid entry. 'Rock', 'Paper', or 'Scissors'")
    exit()

if player_choice == "scissor":  # Made code in case someone doesnt write plural "scissors"
    player_choice = "scissors"

if player_choice == "rock":
    print(f"You choose Rock {rock}")
elif player_choice == "paper":
    print(f"You choose Paper {paper}")
else:
    player_choice = 'scissors'
    print(f"You choose Scissors {scissors}")

computer_choice = random.randint(1, 3)
if computer_choice == 1:
    computer_choice = 'rock'
    print(f"The computer chooses Rock {rock}")
elif computer_choice == 2:
    computer_choice = 'paper'
    print(f"The computer chooses Paper {paper}")
else:
    computer_choice = 'scissors'
    print(f"The computer chooses Scissors {scissors}")

# Determine Winner
if (player_choice == computer_choice):
    print("The game is a Draw! Nobody is a winner.")
elif (player_choice == "rock"
      or computer_choice == "rock") and (player_choice == "scissors"
                                         or computer_choice == "scissors"):
    if player_choice == "rock":
        print("Rock beats Scissors! You win!")
    else:
        print("Rock beats Scissors! You Lose! :(")
elif (player_choice == "scissors"
      or computer_choice == "scissors") and (player_choice == "paper"
                                             or computer_choice == "paper"):
    if player_choice == "scissors":
        print("Scissors beat Paper! You Win!")
    else:
        print("Scissors beat Paper! You lose! :(")
else:
    if player_choice == "paper":
        print("Paper beats Rock! You win!")
    else:
        print("Paper beats Rock! You lose! :(")
