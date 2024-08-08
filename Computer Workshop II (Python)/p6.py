import random
# Initialize the cups with a ball in one of them
cups = [' ', ' ', ' ']
ball_pos= random.randint(0, 2)
cups[ball_pos] = 'O'

# Define a function to display the cups
def display_cups():
    print('  1   2   3')
    print('-------------')
    print('-------------')
    print(f'|| {cups[0]} | {cups[1]} | {cups[2]} ||')
    print('-------------')
    print('-------------')

# Define a function to prompt the user to guess which cup the ball is in
def user_guess():
    while True:
        guess = input('Which cup is the ball in? (1-3): ')
        if guess in ('1', '2', '3'):
            return int(guess)
        print('Invalid input. Please enter 1, 2, or 3.')

# Define a function to check if the user's guess is correct
def check_guess(guess):
    if cups[guess-1] == 'O':
        print('Correct! You win!')
    else:
        print(f'Sorry, the ball was in cup {ball_pos+1}. You lose.')

# Display the cups and prompt the user for a guess
guess = user_guess()

# Check the user's guess and reveal the ball
check_guess(guess)
cups[ball_pos] = 'O'
display_cups()
