# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# chapter5.py - Chapter 5: Before the Storm (send the signal or escape)

import globalvariables as gv
from printcommon import slow_print, chapter_title, show_status, get_choice, storm_check


def restart_generator():
    """Action 1: needed only if the power cable was cut in Chapter 4."""
    if gv.player.power_cut:
        gv.player.power_cut = False
        slow_print("You pull the generator cord three times. The lights come back on.")
    else:
        print("The generator is already running.")


def repair_antenna():
    """Action 2: checks three conditions in order - power, the spare sensor,
    and help from Bulut or KEEPER. Returns True for the best ending."""
    if gv.player.power_cut:
        print("No power! Restart the generator first.")
        return False
    if not gv.player.has_item("spare sensor"):
        print("The antenna's sensor is cracked. A spare sensor is needed.")
        return False
    if not (gv.player.has_drone or gv.player.keeper_ally):
        print("The antenna is too high to reach alone. You need Bulut or KEEPER's help.")
        return False

    helper = "Bulut lifts the cable" if gv.player.has_drone else "KEEPER aims the dish"
    slow_print("You fit the spare sensor while " + helper + ".")
    slow_print("The signal reaches Karakol. Somewhere below, a helicopter starts its engine.")
    return True


def drive_down():
    """Action 4: driving in the storm needs the thermal coat and the rope."""
    if gv.player.has_item("thermal coat") and gv.player.has_item("rope"):
        slow_print("Wrapped in the coat, you tie Dr. Omurova and yourself to the car with the rope")
        slow_print("and crawl down the icy road. You reach Karakol at sunrise.")
        return "neutral_drive"
    slow_print("Halfway down, the car slides off the icy road.")
    return "gameover_road"


def go_back_to_core():
    """Action 5: Nur can go back inside to Chapter 4 (for example, to search
    the storage room for a spare sensor). The trip costs one hour."""
    gv.player.lose_time(1)
    slow_print("You hurry back down the stairs to the core room. The storm is one hour closer.")
    return gv.BACK


def play():
    if not storm_check():
        return "gameover_storm"

    chapter_title(5, "Before the Storm")
    slow_print('"Dr. Omurova grabbed my arm. \'The antenna is frozen. If we can\'t send a signal')
    slow_print('in the next hour, nobody will know we\'re here.\'"')

    while True:
        show_status()
        choice = get_choice(["Restart the generator",
                             "Repair the antenna",
                             "Wait out the storm in the lab",
                             "Drive down the mountain",
                             "Go back to the core room (Chapter 4)"])
        if choice == 1:
            restart_generator()
        elif choice == 2:
            if repair_antenna():
                return "best"
        elif choice == 3:
            return "neutral_lab"
        elif choice == 4:
            return drive_down()
        else:
            return go_back_to_core()


if __name__ == "__main__":
    # Unit test: arrive in Chapter 5 ready for the best ending
    gv.gVariables()
    gv.player.add_item("spare sensor")
    gv.player.has_drone = True
    gv.player.visit(5)
    result = play()
    print("\nChapter 5 returned:", result, "|", gv.player)
