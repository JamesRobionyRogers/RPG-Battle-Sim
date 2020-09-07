import random
import time
import sys

# Setting Constants

# Setting Vairables
running = True

# Defining classes


class Opponent:
    def __init__(self):
        self.OPPONENT_NAME = random.choice(['Blazehound', 'Shadetooth', 'Blightfigure', 'Hauntbug'])
        self.health = 100
        self.damage = 0
        self.attack_text = [f"{self.OPPONENT_NAME} swung potentialy causing {self.damage} points of damage",
                            f"{self.OPPONENT_NAME} swung potentialy causing {self.damage} points of damage"]
        # self.player_health = Player().health

    def attack(self):
        # set vairables
        self.damage = random.randint(5, 16)  # random.randint(1, 20)
        self.message = 'Hello'  # random.choice(self.reponses)

        # attack message
        print(random.choice(self.attack_text))

        # reduce the health of opponent unless dodged (8%)
        if random.randint(1, 100) <= 8:  # opponent dodged message
            print(f"Fortunatly you were able to dodge the {self.OPPONENT_NAME}'s attack'. No damage was taken...\n")
        else:
            self.player.health -= self.damage

        print(f"opponent: {self.health}, player: {self.player.health}")


class Player():
    def __init__(self):
        self.set_display_name = self.set_display_name()
        self.health = 100
        self.weapon = {'Sword': random.randint(10, 15), 'Toothbrush': random.randint(12, 18)}  # dict with weapon name and damange
        self.selected_weapon = ""
        self.damage = 0
        self.opponant = Opponent()

    def set_display_name(self):
        type("\nWhat is your display name: ", letter_pause=0.01)
        self.display_name = input()

    def select_weapon(self):
        # printing to player
        print("\nWeapons available: \n")

        # itterate through available weapons
        for weapon in self.weapon:
            print(f"Weapon: {weapon}      Damage: {self.weapon[weapon]}")

        # selecting weapon
        while self.selected_weapon not in self.weapon:
            self.selected_weapon = input("\nWeapon of choice: ")
            print(self.selected_weapon)

        # setting the remainder of the vairables for the turn
        self.damage = self.weapon[self.selected_weapon]

        # confirming to player what has been chosen
        print(f"\nChosen weapon: {self.selected_weapon} with a damage of {self.damage}")

    def attack(self):
        # attack message
        print(f"{self.display_name} swung the {self.selected_weapon} potentialy causing {self.damage} points of damage")

        # reduce the health of opponent unless dodged (8%)
        if random.randint(1, 100) <= 8:  # opponent dodged message
            print("Unfortunatly, the opponent managed to dodge. Your attack was ineffective this time...\n")
        else:
            self.opponant.health -= self.damage

        print(f"opponent: {self.opponant.health}, player: {self.health}")


class Game:
    def __init__(self):

        # defining game constants
        self.TITLE = "RPG Battle Sim"
        self.HOW_TO_PLAY = f"""
        How To Play:

        {self.TITLE} is a turn based text game programmed in python.
        The simulator will allow the player to battle a computer opponent.

        The format of the battle will be turn based with random elements
        included. The battle will continue until either the player's or computer's
        character is defeated.\n
        """

        # Defining game vairables
        self.running = True
        self.turn_count = 1

        # present player the intro to game
        self.intro()

        # initiate player and opponent class' after introduction
        self.player = Player()
        # self.player.set_display_name()
        self.opponent = Opponent()

    def intro(self):
        type(f"Welcome to {self.TITLE} \n", letter_pause=0.01, enter_pause=0.3)
        type(self.HOW_TO_PLAY, letter_pause=0.008, enter_pause=0.2)

    def win_condition(self):
        # congratulation message

        # game stats

        # game development credits
        self.credits()
        pass

    def lose_condition(self):
        # losing message

        # game stats

        # game development cradits
        self.credits()
        pass

    def turn(self):
        # choose weapon
        self.player.select_weapon()
        # attack opponent
        self.player.attack()
        # self.game_details()
        # recieve attack from opponent

        # update general game game stats
        self.turn_count += 1

        # repeat the turn again
        pass

    def credits(self):
        # title of the Game
        print(f"\nThank you for playing {self.TITLE}\n")
        print("This is a school project for the Advanced Processes Internal in Year 12 at Onslow College for the year of 2020\n\n")
        print("Game developed by: James Robiony-Rogers")

    def game_details(self):
        # current player stats
        print(f"Current player health: {self.player.health}")
        # current opponent stats
        print(f"Current opponant health: {self.opponant.health}")
        # general stats of the game. E.g. turn count etc...
        print(f"Current turn: {self.turn_count}")

    def run_game(self):

        # intro to game has already been executed

        print("What are we waiting for? Lets get right into it...")

        while self.running:
            self.turn()

            # when player dies
            if self.player.health <= 0:
                self.lose_condition()
            # when opponent dies
            if self.opponent.health <= 0:
                self.win_condition()

            self.running = False


# sourced from: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def type(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.25)


# running code
game = Game()
game.run_game()
# game.run_game()

# while running:

#
# game = Game()

# player = Player()
# opponent = Opponent()


# opponent = Opponent()
# opponent.attack()


"""
NOTE:

Have the text itterate out letter by letter, talk to jayden about it
lenency: if the word is in the users input then run, rather than only having to have to put the word in it
"""
