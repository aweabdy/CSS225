# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# chapter4.py - Chapter 4: Inside the Core (KEEPER has locked the lab)

import globalvariables as gv
from printcommon import slow_print, chapter_title, show_status, get_choice, storm_check


def read_logs():
    """Action 1: the logs show the radiation alarm is false."""
    gv.player.logs_read = True
    slow_print("LOG 02:09 - storm damage: radiation sensor R-7 reports 9999. Lockdown started.")
    slow_print("The storm broke the radiation sensor. There is no leak!")


def talk_to_keeper():
    """Action 2: with the logs, Nur can prove the alarm is false.
    Returns True when KEEPER opens the lab."""
    if gv.player.keeper_ally:
        slow_print('KEEPER: "The lab is open, Nur. Dr. Omurova is waiting."')
        return True
    if not gv.player.logs_read:
        slow_print('KEEPER: "Radiation detected. Access denied."')
        return False
    gv.player.keeper_ally = True
    slow_print('You show KEEPER the log. A long pause. KEEPER: "Sensor fault confirmed.')
    slow_print('I was wrong. I will help you." The lab door opens.')
    return True


def cut_power():
    """Action 3: opens the lab, but the station goes dark (matters in Chapter 5)."""
    gv.player.power_cut = True
    slow_print("You pull the main power cable. Sparks - then darkness.")
    slow_print("The lab door slides open, but KEEPER goes silent.")


def search_storage():
    """Action 4: a spare sensor, if Nur did not find one at the gate."""
    if gv.player.has_item("spare sensor"):
        print("The shelves are empty.")
    else:
        gv.player.add_item("spare sensor")
        slow_print("Behind a box of cables you find a spare sensor.")


def play():
    if not storm_check():
        return "gameover_storm"

    chapter_title(4, "Inside the Core")
    slow_print('"Inside, every screen showed the same five words: I AM PROTECTING HER NOW."')
    slow_print("KEEPER has sealed Dr. Omurova inside the lab because of a radiation leak.")

    while True:
        show_status()
        choice = get_choice(["Read the station logs",
                             "Talk to KEEPER",
                             "Cut the main power cable",
                             "Search the storage room",
                             "Leave the core room"])
        if choice == 1:
            read_logs()
        elif choice == 2:
            if talk_to_keeper():
                return gv.FORWARD
        elif choice == 3:
            cut_power()
            return gv.FORWARD
        elif choice == 4:
            search_storage()
        else:
            slow_print("You step back out to the gate.")
            return gv.BACK


if __name__ == "__main__":
    # Unit test: run Chapter 4 on its own with a fresh player
    gv.gVariables()
    gv.player.visit(4)
    result = play()
    print("\nChapter 4 returned:", result, "|", gv.player)
