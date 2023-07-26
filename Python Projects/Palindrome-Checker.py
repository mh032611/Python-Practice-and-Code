def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()

    # Reverse the string
    reversed_str = input_str[::-1]

    # Check if the reversed string is equal to the original string
    if input_str == reversed_str:
        return True
    else:
        return False

# Prompt the user for input
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
