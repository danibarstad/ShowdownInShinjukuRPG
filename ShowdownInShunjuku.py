# ********************************************* #
#                                               #
# SHOWDOWN IN SHINJUKU is a simple, short       #
# text-based adventure game. Character names,   #
# attack names, locations, flavor text, etc     #
# are lifted or adapted from the psycadelic     #
# surf-rock band, Daikaiju!                     #
# https://daikaiju.bandcamp.com/                #
#                                               #
# ********************************************* #



from character import Character
from attack import Attack
import random


# global variable for each character's hit points
HEALTH = 10

def main():

    fist = get_attack('Double Fist Attack', 7)
    serpent = get_attack('Spiral Serpent Strike', 4)

    main = get_character('Secret-Man', HEALTH, fist, '\'You cannot defeat me!\'', '\'I have been defeated!\'')
    villain = get_character('Sharkakhan', HEALTH, serpent, '\'Daikaiju Die!\'', '\'Farewell, Monster Island\'')

    story(main, villain)


    turn = True
    while main.hp > 0 and villain.hp > 0:
        # turn = True

        hitPoints(main, villain)                        # display hit points

        while turn:
            playerTurn = menu(main, villain)            # show menu
            if playerTurn == 1:
                turn = fight(main, villain, turn)       # call fight function
            elif playerTurn == 2:
                turn = tauntFun(main, villain, turn)    # call taunt function
            print('*------------------------------*')
            print()

        hitPoints(main, villain)

        while turn == False:
            # creates a random integer of either 1 or 2 for the villain to take its turn
            villainTurn = random.randint(1, 2)
            print(villain.name, '\'s turn!', sep='')
            if villainTurn == 1:
                turn = fight(villain, main, turn)
            elif villainTurn == 2:
                turn = tauntFun(villain, main, turn)
            print('*------------------------------*')
            print()

    winner(main, villain)



def get_attack(name, hit):
    # Create attack
    return Attack(name, hit)



def get_character(name, health, attack, taunt, defeat):
    # Create characters
    return Character(name, health, attack, taunt, defeat)



def story(main, villain):
    # displays the text telling the story of the game
    print()
    print(main.name, 'was attempting to escape from Nebula M Spacehunter!')
    print('But he was stopped by the evil ', villain.name, '!', sep='')
    print('This is... SHOWDOWN IN SHINJUKU!')
    print('<------------------------------>')
    print()



# menu function for the player to choose their move
def menu(m, v):
    print('Press 1 to attack!\nPress 2 to taunt!\n')

    try:
        move = int(input('Your turn!: '))

        # asks to reenter input if value is below 1 or above 2
        while move != 1 and move != 2:
            print('YOU MUST ENTER 1 or 2!')
            move = int(input('Press 1 to attack!\nPress 2 to taunt!\n'))

    # throws exception if value is not an integer
    except ValueError:
        print('ERROR: YOU MUST ENTER A VALID NUMBER!')
    
    return move



# displays each character and their current health
def hitPoints(m, v):
    print('You:', m.name, 'HP:', m.hp)
    print('Villain:', v.name, 'HP:', v.hp)
    print()



# funtion for when a player taunts
def tauntFun(taunting, defending, turn):
    print(taunting.name, ': ', taunting.taunt, sep='')
    print()

    r = random.randint(1, 2)    # create a random number of either 1 or 2
    if r == 1:  # if 1, opponent skips their next turn
        print(defending.name, 'was intimidated!')
        print('TURN SKIPPED')
        print()

        return turn
    elif r == 2:    # if 2, turns continue as normal
        print(defending.name, 'felt nothing!')
        print()

        if turn == False:
            return True
        else:
            return False



# fight function for when a player attacks
def fight(attacking, defending, turn):
    print(attacking.name, 'attacked!')
    defending.hp -= attacking.atk.damage
    print()

    # change turns
    if turn:
        return False
    else:
        return True

    

# function that displays if the player has won or lost
def winner(m, v):
    if m.hp > v.hp:
        print('YOU WON!')
    elif m.hp < v.hp:
        print('YOU LOST!')



main()