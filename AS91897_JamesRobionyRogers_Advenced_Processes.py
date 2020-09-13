import random
import time
import sys
import os
# importing game settings
from AS91897_JamesRobionyRogers_Settings import *

# Setting Vairables
running = True


# Defining classes
class Characters():
    def __init__(self):
        # initiating the player vairables
        self.set_display_name = self.set_display_name()
        self.player_health = PLAYER_HEALTH
        self.all_weapons = ALL_WEAPONS  # dict with weapon name and damange
        self.available_weapons = {}
        self.player_selected_weapon = ""
        self.player_damage = 0
        # assigning default available weapons
        self.available_weapons = self.all_weapons

        # initiating the opponent vairables
        self.opponent_name = OPPONENT_NAME
        self.opponent_health = OPPONENT_HEALTH
        print("OPPONENT_HEALTH", self.opponent_health)
        self.opponent_damage = OPPONENT_DAMAGE
        self.opponent_attack_text = OPPONENT_ATTACK_TEXT

    def set_display_name(self):
        type("\nWhat is your display name: ", letter_pause=0.01)
        self.display_name = input()

    def select_weapon(self):
        # printing to player
        type("\n\nWeapons available: \n", enter_pause=0.2)

        # itterate through available weapons and assign random damage values
        for weapon in self.available_weapons:
            self.available_weapons[weapon] = random.randint(10, 18)
            # type(f"Weapon: {weapon}      Damage: {self.available_weapons[weapon]}\n")
            weapon_string = f"Weapon: {weapon}"
            damage_string = f"Damage: {self.available_weapons[weapon]}"
            type(formatted_print(weapon_string, damage_string))

        # selecting weapon
        while self.player_selected_weapon not in self.available_weapons:
            type("\nWeapon of choice: ")
            self.player_selected_weapon = input()

        # setting the remainder of the vairables for the turn
        self.player_damage = self.available_weapons[self.player_selected_weapon]

        # confirming to player what has been chosen
        type(f"\nChosen weapon: {self.player_selected_weapon} with a damage of {self.player_damage}\n")

    def player_attack(self):
        # attack message
        type(f"\n{self.display_name} swung the {self.player_selected_weapon} potentialy causing {self.player_damage} points of damage\n")

        # reduce the health of opponent unless dodged (8%)
        if random.randint(1, 100) <= 8:  # opponent dodged message
            type("Unfortunatly, the opponent managed to dodge. Your attack was ineffective this time...\n\n")
        else:
            self.opponent_health -= self.player_damage

    def opponent_attack(self):
        # attack message
        type(random.choice(self.opponent_attack_text))

        # reduce the health of opponent unless dodged (8%)
        if random.randint(1, 100) <= 8:  # opponent dodged message
            print(f"\nFortunatly you were able to dodge the {self.opponent_name}'s attack.    No damage was taken...\n")
        else:
            self.player_health -= self.opponent_damage


class Game:
    def __init__(self):

        # defining game constants
        self.TITLE = TITLE
        self.HOW_TO_PLAY = HOW_TO_PLAY

        # Defining game vairables
        self.running = True
        self.turn_count = 1

        # present player the intro to game
        self.intro()

        # initiate player and opponent class' after introduction
        self.character = Characters()

    def intro(self):
        type(f"Welcome to {self.TITLE} \n", letter_pause=0.01, enter_pause=0.3)
        type(self.HOW_TO_PLAY, letter_pause=0.008, enter_pause=0.2)

    def win_condition(self):
        # congratulation message
        type(f"\nWell done {self.character.display_name} you have managed to successfully eradicate the {self.character.opponent_name}\n")
        # game stats
        self.game_details()
        # game development credits
        self.credits()
        # exit game loop
        self.running = False

    def lose_condition(self):
        # losing message
        type(f"\nUnfortunatly {self.character.opponent_name} was able to defeat you :(")
        type(f"\nTry again and see if you have the courage to defeat the dential enemies\n")
        # game stats
        self.game_details()
        # game development cradits
        self.credits()
        # exit game loop
        self.running = False

    def turn(self):

        type(f"\nTurn: {self.turn_count}", enter_pause=0)
        # choose weapon
        self.character.select_weapon()
        # attack opponent
        self.character.player_attack()
        # NEED TO DO:  remove opponent health from player attack
        self.game_details()
        # recieve attack from opponent
        if self.character.opponent_health >= 0:  # if opponent is NOT dead
            self.character.opponent_attack()
            # NEED TO DO:  remove opponent health from player attack
            self.game_details()

        # proceed when player clicks enter
        self.pause()

        # update general game game stats
        self.turn_count += 1

        # reset needed vairables for next turn:
        self.character.player_selected_weapon = ''

    def credits(self):
        # title of the Game
        print(f"\nThank you for playing {self.TITLE}\n")
        print("This is a school project for the Advanced Processes Internal in Year 12 at Onslow College for the year of 2020\n\n")
        print("Game developed by: James Robiony-Rogers")

    def game_details(self):
        # current player stats
        type("------------------------------------------------------------\n", letter_pause=0.01, enter_pause=0)
        type(f"Current player health: {self.character.player_health}\n", letter_pause=0.01, enter_pause=0)
        # current opponent stats
        type(f"Current opponent health: {self.character.opponent_health}\n", letter_pause=0.01, enter_pause=0)
        # general stats of the game. E.g. turn count etc...
        type(f"Current turn: {self.turn_count}\n", letter_pause=0.01, enter_pause=0)
        type("------------------------------------------------------------\n", letter_pause=0.01, enter_pause=0)

    def pause(self):
        input()

    def run_game(self):

        # intro to game has already been executed

        type("\nWhat are we waiting for? Lets get right into it...")

        while self.running:
            self.turn()

            # when player dies
            if self.character.player_health <= 0:
                self.lose_condition()
            # when opponent dies
            if self.character.opponent_health <= 0:
                self.win_condition()


def type(string, letter_pause=0.015, enter_pause=0.5):  # sourced from: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == "\n":
            time.sleep(enter_pause)
        else:
            time.sleep(letter_pause)


def formatted_print(weapon, damage):  # sourced from: https://stackoverflow.com/questions/11245381/formatting-console-output
    return "%-25s %-15s\n" % (weapon, damage)  # "%-25s" corrisponds to the max width of the left hand width (Weapon text) "%-15s" corrisponds to the max width of the right hand width (Damage text)


def clear_screen():
    # Sourced from:
        # https://www.csestack.org/clear-python-interpreter-console/#:~:text=You%20can%20clear%20the%20Python,system%2C%20cls%20clear%20the%20console. and
        # https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
    # checking for opperating system in order to provide the right command
    if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':  # clear command for Lynicx and Mac opperating systems
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')

    # running code
game = Game()
game.run_game()

"""
NOTE:
lenency: if the word is in the users input then run, rather than only having to have to put the word in it

FEEDBACK:   REGAN MEYNELL
- Have different opponents. Be able to vs another one then run away when you dont want to vs any more
-
"""
