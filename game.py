# game.py

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

print("this is the end of our game.  please play again")
