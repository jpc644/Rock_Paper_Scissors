# game.py

import random

import os

import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("Player_Name")
print(PLAYER_NAME)

print ("-------------------")
#print ("Welcome" + PLAYER_NAME +"to Rock, Paper, Scissors, Shoot!")


print("Welcome to Rock, Paper, Scissors, Shoot,", PLAYER_NAME)

user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")
print(PLAYER_NAME, "selected:", user_choice)

#  validate the input such that only if it is one of the expected values
#....will we continue with the rest of the program
#...otherwise we'll stop the program before it tries to do anything else
#...and we'll ask the user to run the program again

#if user_choice = "rock" or "paper" or "scissors":

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Good choice!")
else:
    print("OOPS, invalid input.  Please try again", PLAYER_NAME)
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("The Computer selected:", computer_choice)

if (user_choice == "rock") and (computer_choice == "scissors"):
    print(PLAYER_NAME, "Wins, Congratulations!")
elif (user_choice == "paper") and (computer_choice == "rock"):
    print(PLAYER_NAME, "Wins, Congratulations!")
elif(user_choice == "scissors") and (computer_choice == "paper"):
    print(PLAYER_NAME, "Wins, Congratulations!")
elif (user_choice == computer_choice):
    print("Game is a Tie!  Why not play again?!")
else:
    print("The Computer wins!  Sorry, better luck next time", PLAYER_NAME)




print("This is the end of our game, thank you for playing!  Please play again soon!")
