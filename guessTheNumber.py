# guess the number mini game

# Import the random function
import random

# Set a variable to a random number between 1 and 20
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

# ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    # set the input to the guess variable
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low.')
    elif guess > secretNumber:
        print('your guess is too high.')
    else:
        break # this condition is the correct guess

if guess == secretNumber:
    print('Congrats! you guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number i was thinking of was ' + str(secretNumber))
