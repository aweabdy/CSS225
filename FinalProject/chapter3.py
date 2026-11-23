# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# chapter3.py - Chapter 3: The Locked Gate (KEEPER at the station gate)

import globalvariables as gv
import challenges
from printcommon import slow_print, chapter_title, show_status, get_choice, storm_check


def enter_gate_code():
    """Action 1: works only if the message was replayed in Chapter 1."""
    if gv.player.has_item("gate code"):
        slow_print("You type 7-4-1. The lock clicks and the gate slides open.")
        return True
    print("You don't know the code. Maybe the message had it?")
    return False


def answer_riddle():
    """Action 2: KEEPER's riddle. Returns gv.FORWARD (correct), gv.ALARM
    (third wrong answer), or None (wrong, but Nur can try again)."""
    if challenges.keeper_riddle():
        return gv.FORWARD

    if gv.player.wrong_answers >= gv.MAX_WRONG_ANSWERS:
        slow_print("ALARM! Red lights flash and the security drones wake up. Nur must retreat.")
        gv.player.wrong_answers = 0   # KEEPER resets the counter after the alarm
        return gv.ALARM

    tries_left = gv.MAX_WRONG_ANSWERS - gv.player.wrong_answers
    slow_print('KEEPER: "Incorrect. Try again." (' + str(tries_left) + " tries left before the alarm)")
    return None


def send_drone():
    """Action 3: Bulut flies through the air vent and opens the gate."""
    if gv.player.has_drone:
        slow_print("Bulut slips through the air vent. A moment later the gate opens from inside.")
        return True
    print("There is no drone to send.")
    return False


def search_snow():
    """Action 4: a spare sensor lies in the snow (needed in Chapter 5)."""
    if gv.player.has_item("spare sensor"):
        print("You already found everything here.")
    else:
        gv.player.add_item("spare sensor")
        slow_print("Under the snow you find a spare sensor that fell off the dome.")


def play():
    if not storm_check():
        return "gameover_storm"

    chapter_title(3, "The Locked Gate")
    slow_print('"The observatory dome glowed red against the dark sky. A calm voice spoke from')
    slow_print('the gate: \'Access denied. This station is under lockdown.\'"')

    while True:
        show_status()
        choice = get_choice(["Enter the gate code",
                             "Answer KEEPER's security question",
                             "Send Bulut through the air vent",
                             "Search the snow around the gate",
                             "Walk back down the path"])
        if choice == 1:
            if enter_gate_code():
                return gv.FORWARD
        elif choice == 2:
            result = answer_riddle()
            if result is not None:
                return result
        elif choice == 3:
            if send_drone():
                return gv.FORWARD
        elif choice == 4:
            search_snow()
        else:
            slow_print("You walk back down to the pass.")
            return gv.BACK


if __name__ == "__main__":
    # Unit test: arrive at the gate without the code, so the riddle is needed
    gv.gVariables()
    gv.player.visit(3)
    result = play()
    print("\nChapter 3 returned:", result, "|", gv.player)
