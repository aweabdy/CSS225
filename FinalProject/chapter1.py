# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# chapter1.py - Chapter 1: The Last Message (Karakol workshop)
#
# Each chapter's play() function returns WHAT happened (gv.FORWARD, gv.BACK,
# gv.ALARM or the name of an ending). maingame.py decides WHERE that leads.

import globalvariables as gv
import challenges
from printcommon import slow_print, chapter_title, show_status, get_choice

BACKPACK_ITEMS = ["flashlight", "battery", "rope"]


def replay_message():
    """Action 1: Dr. Omurova's message contains the gate code."""
    slow_print('"...Ala-Too Station... lockdown... the gate code is 7-4-1... please help."')
    gv.player.add_item("gate code")
    print("(The gate code 7-4-1 was added to your inventory.)")


def visit_uncle_bakyt():
    """Action 2: Uncle Bakyt tells Nur about the cliff shortcut."""
    slow_print("Uncle Bakyt, the old shepherd, opens the door in his slippers.")
    slow_print('"There is a shortcut along the cliffs above the lake. Take my coat - you will need it."')
    gv.player.add_item("thermal coat")
    print("(The thermal coat was added to your inventory.)")


def pack_backpack():
    """Action 3: the backpack fits only 2 of the 3 items.
    Packing again replaces the earlier choice."""
    for item in BACKPACK_ITEMS:          # empty the backpack before repacking
        gv.player.remove_item(item)

    slow_print("The backpack only fits two things. Choose carefully.")
    chosen = []
    while len(chosen) < 2:
        left = [item for item in BACKPACK_ITEMS if item not in chosen]
        print("Item " + str(len(chosen) + 1) + " of 2:")
        pick = get_choice(left)
        chosen.append(left[pick - 1])

    for item in chosen:
        gv.player.add_item(item)
    print("(Packed: " + chosen[0] + " and " + chosen[1] + ".)")


def drive_up_the_road():
    """Action 4: Nur has to complete a challenge (starting the frozen car)
    before Chapter 2. Returns True when Nur can leave."""
    if gv.player.engine_started:
        slow_print("The engine is still warm from the last trip. You drive off.")
        return True
    if challenges.start_engine():
        return True
    gv.player.lose_time(1)   # a failed challenge costs one hour
    return False


def play():
    chapter_title(1, "The Last Message")
    if len(gv.player.route) > 1:     # Nur came back from the mountain pass
        slow_print("Back in the warm workshop, the radio crackles: the storm is still coming.")
    else:
        slow_print('"At 2:14 a.m., every screen in my workshop lit up with the same broken message:')
        slow_print('\'Ala-Too Station... lockdown... please help.\' Then the signal died."')
        slow_print("Nur is alone in the drone workshop in Karakol. The radio warns that a")
        slow_print("snowstorm will reach the mountains in " + str(gv.player.storm_timer) + " hours.")

    while True:
        if gv.player.storm_timer <= 0:
            return "gameover_storm"
        show_status()
        choice = get_choice(["Replay the message",
                             "Visit Uncle Bakyt next door",
                             "Pack the backpack",
                             "Drive up the mountain road",
                             "Go back to sleep"])
        if choice == 1:
            replay_message()
        elif choice == 2:
            visit_uncle_bakyt()
        elif choice == 3:
            pack_backpack()
        elif choice == 4:
            if drive_up_the_road():
                return gv.FORWARD
        else:
            return "gameover_sleep"


if __name__ == "__main__":
    # Unit test: run Chapter 1 on its own with a fresh player
    gv.gVariables()
    gv.player.visit(1)
    result = play()
    print("\nChapter 1 returned:", result, "|", gv.player)
