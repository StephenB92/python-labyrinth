"""
Module containing Game Functions
"""

from random import randint
from characters import hero
from characters import tutorial_enemy
from characters import undead_soldier
from characters import undead_knight
from characters import boss_1
from characters import boss_2
from characters import final_boss

# Player Choice

# Battle Function

# Player battle input

# Damage Calculation


def take_potion():
    """
    Player uses potion to increase health.
    """
    if hero['potion'] != 0:
        print("You avoid the enemy's attack to create space.")
        print("You take a potion from your belt and chug it down...")
        hero['health'] += 50
        hero['potion'] -= 1
        return hero['health']
    else:
        print("No potion held!!")


def use_assist():
    """
    Player calls in the Stranger character to assist in battle.
    """
    if hero['assist'] == True:
        print("The stranger leaps from the shadows, slashing at your foe")
        print("and earning it's full attention.")
        print("The stranger gave his foe a challenge but")
        print("sadly has succumbed to his wounds....")
        hero['assist'] == False
        enemy['health'] -= 60
        return hero['assist']
        return enemy['health']
    else:
        print("You call for help, but nothing happens...")



def take_dmg(attacker, defender):
    """
    Calculates damage in game battles and checks
    if a character has been defeated.
    """
    dmg = randint(attacker['attack'][0], attacker['attack'][1])
    defender['health'] -= dmg
    if defender['health'] <= 0:
        print(f"{defender['name']} fell beneath your blade")
    else:
        print(f"{defender['name']} takes {dmg} damage!")


def commands(player, enemy):
    while True:
        print('------------------------')
        print("Your health is {hero['health]}. Your foe's is {enemy['health]}")
        print("What will you do?")
        command = input("Type 1 to Attack. Type 2 to Heal. Type 3 for assist.")
        if '1' in command:
            take_dmg(player, enemy)
        elif '2' in command:
            take_potion()
        elif '3' in command:
            use_assist()
        else: 
            print ("You stumble and hesitate, your foe takes advantage of the opening and slashes at you!!!!")
            return hero['health'] -= 10
            pass


# Game Over

# Ending
