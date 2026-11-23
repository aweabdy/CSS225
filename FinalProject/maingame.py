# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# maingame.py - starts the game. Run this file: python maingame.py
#
# FINAL VERSION (Milestone 3 feedback): the main game file now holds the
# logic that sends the player to different chapters. Each chapter only
# reports WHAT happened (gv.FORWARD, gv.BACK, gv.ALARM or an ending), and
# the ROUTES table below decides WHERE the player goes next - on to the
# next level or back to an earlier one. To change the story map, only this
# table has to change; the chapter files stay the same.

import globalvariables as gv
import printcommon
import endings
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

# chapter number -> (chapter title, the function that plays that chapter)
CHAPTERS = {
    1: ("The Last Message", chapter1.play),
    2: ("The Frozen Pass", chapter2.play),
    3: ("The Locked Gate", chapter3.play),
    4: ("Inside the Core", chapter4.play),
    5: ("Before the Storm", chapter5.play),
}

# The story map: chapter number -> {result of that chapter: next chapter}
ROUTES = {
    1: {gv.FORWARD: 2},                          # workshop -> mountain pass
    2: {gv.FORWARD: 3, gv.BACK: 1},              # pass -> gate, or back to Karakol
    3: {gv.FORWARD: 4, gv.BACK: 2, gv.ALARM: 2}, # gate -> core, or retreat to the pass
    4: {gv.FORWARD: 5, gv.BACK: 3},              # core -> roof, or back out to the gate
    5: {gv.BACK: 4},                             # roof -> back to the core (the rest are endings)
}


def next_step(current, result):
    """Decides where the game goes after a chapter.

    Returns a chapter number (int) to keep playing, or the name of an
    ending (str) when the story is over."""
    if endings.is_ending(result):
        return result
    if result not in ROUTES[current]:
        # Defensive check: a chapter returned a result the map does not know.
        raise ValueError("Chapter " + str(current) + " returned an unknown result: " + str(result))
    return ROUTES[current][result]


def announce_move(current, target):
    """Tells the player whether they are moving forward or going back."""
    title = CHAPTERS[target][0]
    if target > current:
        print("\n>>> Moving on to Chapter " + str(target) + ": " + title)
    else:
        print("\n<<< Going back to Chapter " + str(target) + ": " + title)


def play_game():
    """Plays one full game from Chapter 1 to an ending."""
    gv.gVariables()               # a brand-new Player object for this game
    current = 1
    while True:
        gv.player.visit(current)
        result = CHAPTERS[current][1]()       # play the chapter
        step = next_step(current, result)
        if isinstance(step, str):             # the name of an ending
            endings.show_ending(step)
            print("\nYour route: " + gv.player.route_text())
            return step
        announce_move(current, step)
        current = step


def main():
    print("SIGNAL FROM ALA-TOO")
    print("A text adventure in the Tian Shan mountains, 2087")
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            printcommon.slow_print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
