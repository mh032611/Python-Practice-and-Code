# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: \n").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# matched_letters = []
# unmatched_letters = []

# For reference: https://developers.google.com/edu/python/lists#for-and-in

for letter in chosen_word:
    if guess == letter:
        print("Right")
        # matched_letters.append(guess)
    else:
        print("Wrong")
        # unmatched_letters.append(letter)

# print ("matched letters:", matched_letters)
# print ("unmatched letters", unmatched_letters)

########################################################################################################################

# Step 2


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

display = list(len(chosen_word) * """_""")

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = letter
    # else statement is not necessary because it keeps the original underscore

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

########################################################################################################################

# Step 2 (Alternate version) (used in practice)


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

display = list(len(chosen_word) * """_""")

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = letter
    # else statement is not necessary because it keeps the original underscore

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)
