from random import randint
from presents import list_of_package

def roll_the_dice():
    """Roll the dice and get a number, 6 means you can pick a package, else next player"""

    input('Press any button to roll the dice: ')
    random_number = randint(1, 6)
    print('You got a:', random_number)

    if random_number == 6:
        print(list_of_package)
        choice = int(input('Pick a package number: '))
        list_of_package.pop(choice)
        #add removed package to player


        if list_of_package == []:
            print('Now starts the real game, "pick from each other"')



