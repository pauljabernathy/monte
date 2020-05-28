"""
Simulation of an example on page 60 of Reinforcement Learning, second Edition, by Barto and Sutton
"""
import numpy as np
import cupy as cp
# import pandas as pd
# import matplotlib.pyplot as plt
from datetime import datetime
import time
from functools import partial

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

WIDTH = 5
HEIGHT = 5

A = (1, 4)
A_PRIME = (1, 0)
B = (3, 4)
B_PRIME = (3, 2)
A_TO_A_PRIME_REWARD = 10
B_TO_B_PRIME_REWARD = 5
OFF_THE_GRID_REWARD = -1
REGULAR_REWARD = 0

GAMMA = 0.9

DEFAULT_PATH_LENGTH = 1000
DEFAULT_NUM_RUNS = 10000


def get_next_action():
    return np.random.choice([UP, DOWN, LEFT, RIGHT])


def get_next_location_and_reward(current_location, next_action):
    """
    Gets the next location based on the current location and the next action.  Attemptin to left, right, up or down
    will often reult in going that direction, but not always.
    :param current_location:  a tuple for the (x, y) coordinates, where the bottom right corner is defined to be (0, 0)
    :param next_action: the action we are attempting to take
    :return: a tuple containing the resulting location, as a tuple, and the resulting reward; example ((x, y), -1)
    """
    # First, look at A to A' or B to B'
    if current_location == A:
        return A_PRIME, A_TO_A_PRIME_REWARD
    elif current_location == B:
        return B_PRIME, B_TO_B_PRIME_REWARD

    # Look for off the grid rewards
    #if is_edge(current_location):
    #    return current_location, OFF_THE_GRID_REWARD

    # on left edge and trying to move left
    if current_location[0] == 0 and next_action == LEFT:
        return current_location, OFF_THE_GRID_REWARD

    # on top edge and trying to go up
    if current_location[1] == 4 and next_action == UP:
        return current_location, OFF_THE_GRID_REWARD

    # on right edge and tryig to go right
    if current_location[0] == 4 and next_action == RIGHT:
        return current_location, OFF_THE_GRID_REWARD

    # on bottom edge and trying to go down
    if current_location[1] == 0 and next_action == DOWN:
        return current_location, OFF_THE_GRID_REWARD

    # Now, a "regular" move
    if next_action == LEFT:
        next_location = current_location[0] - 1, current_location[1]
    elif next_action == UP:
        next_location = current_location[0], current_location[1] + 1
    elif next_action == RIGHT:
        next_location = current_location[0] + 1, current_location[1]
    elif next_action == DOWN:
        next_location = current_location[0], current_location[1] - 1

    return next_location, 0


#def is_edge(location):
#    return location[0] in (0, 4) or location[1] in (0, 4)

def get_one_random_path(starting_point, length=DEFAULT_PATH_LENGTH):
    location = starting_point
    cumulative_reward = 0
    path = [location]
    for k in range(length):
        next_action = get_next_action()
        location, reward = get_next_location_and_reward(location, next_action)
        reward = reward * (GAMMA ** k)
        cumulative_reward += reward
        path.append(location)

    return path, cumulative_reward


def estimate_value(point, num_runs=DEFAULT_NUM_RUNS):
    print('computing estimated value for ', point)
    rewards = []
    for i in range(num_runs):
        rewards.append(get_one_random_path(point, DEFAULT_PATH_LENGTH)[1])

    mean = sum(rewards) / len(rewards)
    #print(mean)

    # plt.hist(rewards)
    # plt.show()
    # print(pd.Series(rewards).value_counts())

    return mean


def get_one_random_path_parallel(run_num, starting_point, length=DEFAULT_PATH_LENGTH):
    return get_one_random_path(starting_point, length)


def estimate_value_numpy(point, num_runs=DEFAULT_NUM_RUNS):
    print('computing estimated value for ', point, 'using numpy')
    values = np.zeros(num_runs)
    f = partial(get_one_random_path_parallel, starting_point=point, length=DEFAULT_PATH_LENGTH)
    runs = np.arange(num_runs).reshape(1, num_runs)
    estimated_values = np.apply_along_axis(f, 0, runs)
    return estimated_values[1].mean()


def estimate_value_cupy(point, num_runs=DEFAULT_NUM_RUNS):
    print('computing estimated value for ', point, 'using numpy')
    f = partial(get_one_random_path_parallel, starting_point=point, length=DEFAULT_PATH_LENGTH)
    runs = cp.arange(num_runs).reshape(1, num_runs)
    estimated_values = cp.apply_along_axis(f, 0, runs)
    return estimated_values[1].mean()


def estimate_all():
    start = datetime.now()
    begin = time.time()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(estimate_value((x, y)))
    stop = datetime.now()
    end = time.time()
    print('completed in ', (stop.timestamp() - start.timestamp()), 'seconds')
    print('completed in ', (end - begin), 'seconds')



#value = estimate_value((2, 2))
#print(value)

#estimate_all()
