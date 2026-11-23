# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# challenges.py - the two puzzles in the game.
#
#   start_engine()  - a challenge the player must complete in Chapter 1
#                     before moving on to Chapter 2 (Milestone 2 feedback).
#   keeper_riddle() - KEEPER's security question at the gate in Chapter 3.

import random
import globalvariables as gv
from printcommon import slow_print

ENGINE_TRIES = 3


def start_engine():
    """Challenge: the old car is frozen. The starter has a dial from 1 to 9
    and only one setting works tonight. The player has 3 tries and gets a
    hint after each wrong guess.

    Returns True if the engine starts, False if all tries are used.
    """
    secret = random.randint(1, 9)   # a new random setting every time
    slow_print("The car is frozen solid. The starter dial goes from 1 to 9,")
    slow_print("and only one setting will turn the engine over in this cold.")

    for attempt in range(1, ENGINE_TRIES + 1):
        guess = input("Try " + str(attempt) + " of " + str(ENGINE_TRIES) + " - set the dial (1-9): ").strip()
        if not guess.isdigit() or not 1 <= int(guess) <= 9:
            print("The dial only has the numbers 1 to 9. That try is wasted.")
            continue

        guess = int(guess)
        if guess == secret:
            slow_print("The engine coughs, then roars. The headlights cut through the dark.")
            gv.player.engine_started = True
            return True
        elif guess < secret:
            print("The engine sputters weakly. Try a HIGHER setting.")
        else:
            print("The engine floods and dies. Try a LOWER setting.")

    slow_print("The battery groans and goes quiet. Warming the engine up again takes an hour.")
    return False


# Each riddle is (question, list of accepted answers)
RIDDLES = [
    ("I have keys but open no locks. I have space but no room. What am I?",
     ["keyboard", "a keyboard"]),
    ("The more of me you take, the more you leave behind. What am I?",
     ["footsteps", "steps", "footprints"]),
    ("I can be cracked, made, told, and played. What am I?",
     ["joke", "a joke"]),
]


def keeper_riddle():
    """KEEPER asks one random riddle. Returns True for a correct answer.
    A wrong answer adds 1 to the player's wrong_answers counter."""
    question, answers = random.choice(RIDDLES)
    slow_print('KEEPER: "Security question. ' + question + '"')
    answer = input("Your answer: ").strip().lower()

    if answer in answers:
        slow_print('KEEPER: "Correct. Opening the gate."')
        return True

    gv.player.wrong_answers += 1
    return False


if __name__ == "__main__":
    # Unit test: play both challenges on their own
    gv.gVariables()
    print("Engine started:", start_engine())
    print("Riddle solved:", keeper_riddle(), "| wrong answers:", gv.player.wrong_answers)
