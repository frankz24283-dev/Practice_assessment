'''
   Author: Frank Zhang
   Date:15/08/2026
   Version: 1.0
   Despcripition: Heads and tails programs
'''

#-----libraries-----
import random
#-----functions------

#-----main routine-----
print("Welcome to Heads & Tails game! ")
name = str(input("Enter you name: "))
age = int(input("Enter you age: "))
options = ["Heads", "Tails"]

# Keep score inside the function
def heads_tails():
    user_score = 0
    computer_score = 0

#Keep playing until computer or user reaches 2 points
while user_score != 2 and computer_score != 2:
    random_choice = random.randint(0,1)
    computer_guess = options[random.choice]