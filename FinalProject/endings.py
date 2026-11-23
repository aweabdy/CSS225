# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# endings.py - the six endings: 1 best, 2 neutral, 3 game over.

from printcommon import slow_print

# ending name -> (title, final text)
ENDINGS = {
    "best": ("BEST ENDING - Signal Received",
             "At dawn a rescue helicopter lands on the roof. Ala-Too Station is back online,\n"
             "and KEEPER's first message is a thank-you to Nur."),
    "neutral_lab": ("NEUTRAL ENDING - The Long Night",
                    "Nur and Dr. Omurova survive the storm in the lab, but the frozen station\n"
                    "is lost. Nobody in Karakol ever learns what happened up there."),
    "neutral_drive": ("NEUTRAL ENDING - Back to Karakol",
                      "Nur and Dr. Omurova are safe, but Ala-Too Station stays dark under the snow."),
    "gameover_sleep": ("GAME OVER - Silence",
                       "Nur goes back to sleep. In the morning the station stays silent forever."),
    "gameover_storm": ("GAME OVER - The Storm Hits",
                       "The storm arrives before the signal is sent. The mountain keeps its secret."),
    "gameover_road": ("GAME OVER - The Icy Road",
                      "Without the right gear, the car slides off the road into the snow."),
}


def is_ending(result):
    """Returns True if a chapter's result is the name of an ending."""
    return result in ENDINGS


def show_ending(name):
    """Prints the ending with the given name."""
    title, text = ENDINGS[name]
    print()
    print("*" * 50)
    print("  " + title)
    print("*" * 50)
    slow_print(text)


if __name__ == "__main__":
    # Unit test: print every ending once
    for ending_name in ENDINGS:
        show_ending(ending_name)
