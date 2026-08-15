'''
   Author: Frank Zhang
   Date:15/08/2026
   Version: 3.0
   Despcripition: Heads and tails programs
'''

#-----libraries------
import random
#-----constants------
WINNING_SCORE = 2
MIN_AGE = 5
MAX_AGE = 120
COIN_OPTIONS = ["Heads", "Tails"]

#-----functions-------
def validate_name():
    while True:
        name_input = input("Enter your name: ").strip()
        if len(name_input) > 0 and name_input.isalpha():
            return name_input.capitalize()
        else:
            print("Invalid input! Name must contain letters only and cannot be empty.\n")

def validate_user_guess():
    while True:
        guess_input = input("Heads or Tails? ").strip().capitalize()
        if guess_input in COIN_OPTIONS:
            return guess_input
        else:
            print("Invalid choice! Please type 'Heads' or 'Tails'.\n")

def heads_tails(player_name):
    player_score = 0
    computer_score = 0

    print(f"\n--- Game Started! First to {WINNING_SCORE} points wins. ---")
#------main routine-----