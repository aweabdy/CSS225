# Abdyrakhman Raiapov
# November 15, 2026
# Problem 5 - Checks whether the game character has picked up all the items
# needed for a task and does not have any status debuff that blocks it.
# Uses the given character class (unchanged) and prints the result of each
# check for Task 1 (climb a mountain), Task 2 (cook a meal) and Task 3
# (write a book).


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses


player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)


def can_do_task(player, task, needed_items, blocking_debuff):
    """Prints and returns True if the player has every needed item AND does
    not have the blocking debuff.

    By de Morgan's law, "not (has_items and not blocked)" is the same as
    "missing an item or blocked", which is how the failure reason is built.
    """
    missing = [item for item in needed_items if item not in player.weapons]
    has_all_items = len(missing) == 0
    is_blocked = blocking_debuff in player.weaknesses

    print()
    print("Task:", task)
    print("  Needs:", ", ".join(needed_items), "| cannot have:", blocking_debuff)
    if has_all_items and not is_blocked:
        print("  Result: YES -", player.nickname, "can do this task.")
        return True

    # at least one condition failed - explain which one(s)
    if not has_all_items:
        print("  Missing items:", ", ".join(missing))
    if is_blocked:
        print("  Blocked by the debuff:", blocking_debuff)
    print("  Result: NO -", player.nickname, "cannot do this task yet.")
    return False


results = [
    can_do_task(player1, "1. Climb a mountain", ["rope", "coat", "first aid kit"], "slow"),
    can_do_task(player1, "2. Cook a meal", ["pan", "groceries"], "small"),
    can_do_task(player1, "3. Write a book", ["pen", "paper", "idea"], "confusion"),
]
print()
print("Tasks the character can do:", results.count(True), "of", len(results))
