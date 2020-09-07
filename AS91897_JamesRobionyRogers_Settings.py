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

MAX_HEALTH = 10

# PLAYER SETTINGS
PLAYER_HEALTH = MAX_HEALTH
ALL_WEAPONS = {'Floss': random.randint(10, 15),
               'Toothbrush': random.randint(12, 18)}


# OPPONENT SETTINGS
OPPONENT_HEALTH = MAX_HEALTH
OPPONENT_NAMES_LIST = ['Lollies', 'Soda', 'Citrus', 'Chocolate']
OPPONENT_NAME = random.choice(OPPONENT_NAMES_LIST)
OPPONENT_DAMAGE = random.randint(5, 16)

OPPONENT_ATTACK_TEXT = [f"{OPPONENT_NAME} swung potentialy causing {OPPONENT_DAMAGE} points of damage\n",
                        f"{OPPONENT_NAME} swung potentialy causing {OPPONENT_DAMAGE} points of damage\n"]


if __name__ == '__main__':
    print("\nRunning wring script. Run AS91897_JamesRobionyRogers_Advenced_Processes.py")
