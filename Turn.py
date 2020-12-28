from People import players
from dice import roll_the_dice

def display_turn():
    """ Display next player """
    x = 0
    while True:
        print("It's", players[x], 'turn to roll:')
        roll_the_dice()
        x +=1
        if x == len(players):
            display_turn()


