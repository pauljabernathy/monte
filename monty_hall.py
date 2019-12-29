from numpy import random


def run_sim(n=1000):
    num_wins_true = 0
    for i in range(n):
        num_wins_true += do_one_turn(True)

    num_wins_false = 0
    for i in range(n):
        num_wins_false += do_one_turn(False)

    return num_wins_true, num_wins_false


# TODO: perf test between using lists and using sets
def do_one_turn(change_choice=True):
    door_numbers = [1, 2, 3]
    prize_door = random.choice(door_numbers)
    door_choice = random.choice(door_numbers)

    # Now reveal a door.
    doors_to_reveal_from = door_numbers.copy()
    doors_to_reveal_from.remove(door_choice)
    if prize_door in doors_to_reveal_from:
        doors_to_reveal_from.remove(prize_door)
    revealed_door = random.choice(doors_to_reveal_from)

    # If contestant wants to change their choice.
    if change_choice:
        doors = door_numbers.copy()
        doors.remove(revealed_door)
        doors.remove(door_choice)
        door_choice = doors.pop()

    return door_choice == prize_door


print(run_sim(10000))

