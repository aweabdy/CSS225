# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# globalvariables.py - the game settings and the one shared Player object.
#
# Final version: the inventory, timer and story flags now live inside a
# Player object (see player.py). Every module reaches it with dot
# notation, for example: gv.player.lose_time(1)

from player import Player

STORM_HOURS = 6         # hours before the snowstorm hits (from Milestone 1)
MAX_WRONG_ANSWERS = 3   # third wrong answer to KEEPER's riddle sets off the alarm
PLAYER_NAME = "Nur"     # the player character

# What a chapter's play() function can return. maingame.py looks these up
# in its ROUTES table to decide which chapter comes next.
FORWARD = "forward"     # go on to the next chapter
BACK = "back"           # go back to the previous chapter
ALARM = "alarm"         # KEEPER's alarm forces Nur to retreat
# A chapter can also return the name of an ending (see endings.py).

player = Player(PLAYER_NAME, STORM_HOURS)   # the current game's player


def gVariables():
    """Starts a fresh game by creating a brand-new Player object."""
    global player
    player = Player(PLAYER_NAME, STORM_HOURS)


if __name__ == "__main__":
    # Unit test: a new game must reset everything
    player.add_item("rope")
    gVariables()
    assert player.inventory == [] and player.storm_timer == STORM_HOURS
    print("globalvariables tests passed:", player)
