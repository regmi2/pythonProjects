#Computer provides random number based on a user input of 
#range, then the user has to guess the number
#
#using the 'random' python library, loops, casting from string to int
#control flow/conditionals, inputs, f strings


import random

highestNum = int(input(f'Set the highest number that the random number can be: '))
def guess(x):
    randNumr = random.randint(1,x)
    guess = 0

    #while loop with control flow statements if guess 
    #does not equal randNumr
    while guess != randNumr:

        #cast the input as an integer since input receives string
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > x:
            print(f"Your guess cannot be greater than {x}")
        elif guess < 1:
            print(f'Your guess cannot be less than 1')
        elif guess < randNumr:
            print('Your guess is too low. Try again.')
        elif guess > randNumr:
            print('Your guess is too high. Try again.')
    
    print(f"Great job! Your guess = {guess} = {randNumr}. You win! ")


#call the guess function with the highest num received from 
#player
guess(highestNum)
