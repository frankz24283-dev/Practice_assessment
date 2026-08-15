'''
   Author: Frank Zhang
   Date:15/08/2026
   Version: 2.0
   Despcripition: Heads and tails programs
'''

#-----libraries-------
import random
#-----functions--------

# Keep score inside the function
def heads_tails(player_name):
    player_score = 0
    opponent_score = 0
    coin_options = ["Heads", "Tails"]

    while player_score != 2 and opponent_score != 2:
        random_index = random.randint(0,1)
        computer_choice = coin_options[random_index]
#-----main routine-----