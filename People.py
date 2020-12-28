from player_class import Player

players = []
def add_players():
    """ Add players to the game """

    x = int(input('How many players do you wanna add to the game? '))
    num = 0
    while x != num:
        name = Player(input('Add a new player: '))
        players.append(name.name)
        num +=1
    print(len(players))