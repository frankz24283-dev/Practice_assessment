'''
   Author: Frank Zhang
   Date:15/08/2026
   Version: 1.0
   Despcripition: Heads and tails programs
'''

#-----libraries-----
import random
#-----functions------

# Keep score inside the function
def heads_tails():
    user_score = 0
    computer_score = 0

#Keep playing until computer or user reaches 2 points
    while user_score != 2 and computer_score != 2:
        random_choice = random.randint(0,1)
        computer_guess = options[random_choice]

# Ask for options of users
        user_guess = input("Heads or Tails? ")

# Compared both answers(User and computer)
        if user_guess == computer_guess:
            user_score += 1
            print(f"It was {computer_guess}, you guessed{user_guess}. You won the game. ")
        else:
            computer_score += 1
            print(f"It was {computer_guess}. You guessed {user_guess}. You lost game. ")

# Display each score
        print(f" Your score: {user_score}")
        print(f"Computer score: {computer_score}\n")

#Decide who won the game
    if user_score == 2:
        print(f"Congratulation {name}, you won the game")
    else:
        print(f" Game over{name}, you lost the game")


#-----main routine-----
print("Welcome to Heads & Tails game! ")
name = str(input("Enter you name: "))
age = int(input("Enter you age: "))
options = ["Heads", "Tails"]
heads_tails()
