# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# printcommon.py - helper functions for output and input that every
# chapter uses, so the same code is not repeated five times.

import time
import globalvariables as gv

DELAY = 0.02    # pause between characters; set to 0 to print instantly


def slow_print(text):
    """Prints text one character at a time, like a radio message."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(DELAY)
    print()


def chapter_title(number, title):
    """Prints a chapter heading."""
    print()
    print("=" * 50)
    print("  Chapter " + str(number) + ": " + title)
    print("=" * 50)


def show_status():
    """Shows the storm timer and the inventory before each menu."""
    print()
    print(gv.player.status_line())


def get_choice(options):
    """Prints a numbered menu and keeps asking until the player types a
    valid number. Returns the chosen number as an int.

    options is a list of strings, e.g. ["Replay the message", "Go back to sleep"].
    """
    for number, option in enumerate(options, start=1):
        print("  " + str(number) + ". " + option)

    while True:
        answer = input("What do you do? ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print("Please type a number from 1 to " + str(len(options)) + ".")


def storm_check():
    """Runs at the start of Chapters 2-5 (and after time is lost).
    Returns True if there is still time, False if the storm has hit."""
    if gv.player.storm_timer <= 0:
        slow_print("The wind turns into a white wall. The storm has arrived.")
        return False
    return True


if __name__ == "__main__":
    # Unit test: type 0, then 9, then 2 to check that bad input is rejected
    chapter_title(0, "printcommon test")
    show_status()
    print("You chose:", get_choice(["Option A", "Option B"]))
