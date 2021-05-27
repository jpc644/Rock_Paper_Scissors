# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")
print(user_choice)

#  validate the input such that only if it is one of the expected values
#....will we continue with the rest of the program
#...otherwise we'll stop the program before it tries to do anything else
#...and we'll ask the user to run the program again

#if user_choice = "rock" or "paper" or "scissors":

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("valid. please continue")
else:
    print("oops, invalid input.  please try again")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("computer_choice:", computer_choice)

if (user_choice == "rock") and (computer_choice == "scissors"):
    print("USER WINS")
elif (user_choice == "paper") and (computer_choice == "rock"):
    print("USER WINS")
elif(user_choice == "scissors") and (computer_choice == "paper"):
    print("USER WINS")
elif (user_choice == computer_choice):
    print("TIE")
else:
    print("COMPUTER WINS")




print("this is the end of our game.  please play again")
