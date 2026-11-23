# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# chapter2.py - Chapter 2: The Frozen Pass (avalanche on the road)

import globalvariables as gv
from printcommon import slow_print, chapter_title, show_status, get_choice, storm_check


def repair_drone():
    """Action 1: the broken patrol drone needs the spare battery."""
    if gv.player.has_drone:
        print("Bulut is already hovering next to you.")
    elif gv.player.has_item("battery"):
        gv.player.has_drone = True
        gv.player.remove_item("battery")   # the battery is now inside the drone
        slow_print("You swap in the spare battery. The drone's eye turns blue.")
        slow_print("It beeps twice. You name it Bulut - 'cloud'. Bulut joins you.")
    else:
        print("The drone needs a spare battery. You don't have one.")


def climb_cliff():
    """Action 2: the fast shortcut needs the rope. Returns True if Nur makes it."""
    if gv.player.has_item("rope"):
        slow_print("You tie the rope to a frozen pine and climb the cliff shortcut.")
        return True
    print("The cliff is too steep to climb without a rope.")
    return False


def walk_around_lake():
    """Action 3: the safe but slow path costs one hour.
    Returns gv.FORWARD with the coat, gv.BACK (to Karakol) without it."""
    gv.player.lose_time(1)
    slow_print("You walk around the frozen lake. The storm is one hour closer.")
    if gv.player.has_item("thermal coat"):
        slow_print("Uncle Bakyt's coat keeps you warm all the way to the station.")
        return gv.FORWARD
    slow_print("Too cold! Your fingers go numb, and you turn back to Karakol.")
    return gv.BACK


def play():
    if not storm_check():
        return "gameover_storm"

    chapter_title(2, "The Frozen Pass")
    slow_print('"Halfway up the pass, my headlights hit a wall of snow. An avalanche had swallowed the road."')
    slow_print("A broken patrol drone from the station lies half-buried in the snow, its red light blinking.")

    while True:
        show_status()
        choice = get_choice(["Repair the patrol drone",
                             "Climb the cliff shortcut",
                             "Walk around the frozen lake",
                             "Drive back to Karakol"])
        if choice == 1:
            repair_drone()
        elif choice == 2:
            if climb_cliff():
                return gv.FORWARD
        elif choice == 3:
            return walk_around_lake()
        else:
            slow_print("You turn the car around and drive back to Karakol.")
            return gv.BACK


if __name__ == "__main__":
    # Unit test: start Chapter 2 as if Nur packed the battery and rope
    gv.gVariables()
    gv.player.add_item("battery")
    gv.player.add_item("rope")
    gv.player.visit(2)
    result = play()
    print("\nChapter 2 returned:", result, "|", gv.player)
