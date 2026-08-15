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

    while player_score < WINNING_SCORE and computer_score < WINNING_SCORE:
        random_index = random.randint(0, len(COIN_OPTIONS) - 1)
        computer_choice = COIN_OPTIONS[random_index]

        player_guess = validate_user_guess()

        if player_guess == computer_choice:
            player_score += 1
            print(f"It was {computer_choice}, you guessed {player_guess}. You won that round.")
        else:
            computer_score += 1
            print(f"It was {computer_choice}. You guessed {player_guess}. You lost that round.")

        print(f"Score -> {player_name}: {player_score} | Computer: {computer_score}\n")

    if player_score == WINNING_SCORE:
        print(f"Congratulations {player_name}, you won the game!")
    else:
        print(f"Game over {player_name}, you lost the game.")
#------main routine-----