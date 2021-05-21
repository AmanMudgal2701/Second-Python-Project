#The computer will think of a random number from 1 to 10 as secret number.
import random
random_number=random.randint(1,10)

#Then ask you ( Player ) to guess the number and store as guess number.
guessed_number=input('Guess any number between 1 to 10: ')
guessed_number1=int(guessed_number)

#Compare the guess number with the secret number.
if (guessed_number1==random_number):
    #If the player guesses the right number he wins, so print player wins and computer lose.
    print('player wins and computer lose')
    print('Congrats!')

else:
    #If the player guesses the wrong number, then he loses so print player lose and computer wins.
    print('player lose and computer wins')
    print('Oh! Try Again.')
