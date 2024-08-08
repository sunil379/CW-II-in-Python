def validate_input(user_input):
    valid_characters = set("9876543210")
    if set(user_input).issubset(valid_characters):
        return True
    else:
        return False

input_str = input("Enter a string: ")
if validate_input(input_str):
    print("Valid input!")
else:
    print("Invalid input!")
