def print_square():
    while True:
        try:
            num = int(input("Enter an integer: "))
            square = num ** 2
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            print(f"The square of {num} is: {square}")
            break

print_square()