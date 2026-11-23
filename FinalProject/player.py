# Abdyrakhman Raiapov
# November 23, 2026
# CSS-225 Final Project - Signal from Ala-Too
# player.py - NEW in the final version: the Player class.
#
# One Player object stores everything about Nur's current game: the
# inventory, the storm timer, the story flags and the route through the
# chapters. Keeping this data inside an object (instead of many separate
# global variables) means a new game only needs a new Player().


class Player:
    """The player character and the state of one playthrough."""

    def __init__(self, name="Nur", storm_hours=6):
        # attributes - the data each Player object stores
        self.name = name
        self.inventory = []            # items collected, e.g. "gate code", "rope"
        self.storm_timer = storm_hours # hours left before the snowstorm hits
        self.wrong_answers = 0         # wrong answers to KEEPER's riddle (Chapter 3)
        self.route = []                # chapter numbers in the order they were visited

        # True/False story flags that remember earlier decisions
        self.has_drone = False         # Bulut the drone was repaired (Chapter 2)
        self.logs_read = False         # the station logs were read (Chapter 4)
        self.keeper_ally = False       # KEEPER was convinced to help (Chapter 4)
        self.power_cut = False         # the main power cable was cut (Chapter 4)
        self.engine_started = False    # the frozen car was started (Chapter 1 challenge)

    # methods - the actions a Player can do
    def has_item(self, item):
        """Returns True if the item is in the inventory."""
        return item in self.inventory

    def add_item(self, item):
        """Adds an item once (no duplicates)."""
        if item not in self.inventory:
            self.inventory.append(item)

    def remove_item(self, item):
        """Removes an item if the player has it."""
        if item in self.inventory:
            self.inventory.remove(item)

    def lose_time(self, hours=1):
        """The storm gets closer. The timer never goes below 0."""
        self.storm_timer = max(0, self.storm_timer - hours)

    def visit(self, chapter_number):
        """Records that the player entered a chapter."""
        self.route.append(chapter_number)

    def status_line(self):
        """One line with the storm timer and inventory, shown before each menu."""
        items = ", ".join(self.inventory) if self.inventory else "empty"
        return "[Storm in " + str(self.storm_timer) + " hour(s)]  [Inventory: " + items + "]"

    def route_text(self):
        """The path through the game, e.g. 'Chapter 1 -> Chapter 2 -> Chapter 1'."""
        return " -> ".join("Chapter " + str(n) for n in self.route)

    def __str__(self):
        return self.name + " " + self.status_line()


if __name__ == "__main__":
    # Unit test for the Player class
    p = Player()
    p.add_item("rope")
    p.add_item("rope")                 # a duplicate is ignored
    assert p.inventory == ["rope"]
    p.lose_time(10)
    assert p.storm_timer == 0          # never below zero
    p.visit(1); p.visit(2); p.visit(1)
    print(p)
    print("Route:", p.route_text())
    print("Player class tests passed.")
