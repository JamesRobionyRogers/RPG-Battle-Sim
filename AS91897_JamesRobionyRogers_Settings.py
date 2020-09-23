import random

# DEFIGNING CONSTANTS

# GAME SETTINGS
TITLE = "RPG Battle Sim"
HOW_TO_PLAY = f"""
    How To Play:

    {TITLE} is a turn based text game programmed in python.
    The simulator will allow the player to battle a computer opponent.

    The format of the battle will be turn based with random elements
    included. The battle will continue until either the player's or computer's
    character is defeated.

    Game will pause to allow the player to read. Click ENTER to proceed when ready.\n
"""

MAX_HEALTH = 80


# setting table print settings
TABLE_LETTER_PAUSE = 0.01
TABLE_ENTER_PAUSE = 0

DENTAL_HYGIENE_PRACTICES = ["If there's one thing to take away from this game, it's got to be: \nDon't go to bed without brushing your teeth. Keep those precious teeth squeeky clean\n",
                            "If you're having trouble cleaning those teeth of yours, give this a go: \nTry moving your toothbrush gentialy using circular motions, this should do the trick to \nremove any plaque that may have built up on your teeth\n",
                            "Dont forget your tongue!  Plaque can also build up on your tongue and believe me, \nI may only be a computer game, but you do NOT want to be the person with stinky breath.\n",
                            "Do you know what the F word is?  If you said flossing you'd be 100% correct. Flossing has many advantages such as: \n  - Reducing plaque \n  - Lowering inflammation in the gum area \n  - Stimulating your gums\n",
                            "Finaly the easiest way to improve your dential is plain and simply to drink water. That easy. \nDrinking water after every meal can help out some of the negative effects of sticky and acidic foods and beverages in between brushes\n"]

# PLAYER & OPPONENT VAIRBALES
DODGE_CHANCE = 8  # 8% chance to dodge

# PLAYER SETTINGS
PLAYER_HEALTH = MAX_HEALTH
ALL_WEAPONS = {'Floss': random.randint(10, 15),
               'Toothbrush': random.randint(12, 18)}


# OPPONENT SETTINGS
OPPONENT_HEALTH = MAX_HEALTH
OPPONENT_NAMES_LIST = ['Lollies', 'Soda', 'Citrus', 'Chocolate']
OPPONENT_NAME = random.choice(OPPONENT_NAMES_LIST)
OPPONENT_DAMAGE_RANGE = [5, 16]
OPPONENT_DAMAGE = random.randint(OPPONENT_DAMAGE_RANGE[0], OPPONENT_DAMAGE_RANGE[1])


OPPONENT_ATTACK_TEXT = [f"{OPPONENT_NAME} swung potentialy causing {OPPONENT_DAMAGE} points of damage\n",
                        f"{OPPONENT_NAME} swung potentialy causing {OPPONENT_DAMAGE} points of damage\n"]


if __name__ == '__main__':
    print("\nRunning wring script. Run AS91897_JamesRobionyRogers_Advenced_Processes.py")
