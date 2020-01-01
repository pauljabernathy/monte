import numpy.random as random


"""
Simulation of the One Armed Bandit problem.

Read about it in Algorithms to Live By.

Create several slot machines of random probability.  Start with just two.
Try several algorithms.

1. Try one slot machine.  If you win, keep playing.  If you lose, switch to the other.

2. Alternate between them

3: Test them first to see which one seems better, then use that one exclusively.


Another simulation is a bayesian analysis of the payout probability; what you think the probability is based on
results so far.

Other TODO:
-variable numbers of slot machines
-ability to specify the payout probabilities; and experiment with how that affects the effectiveness of the different
algorithms
"""


class SlotMachine:

    def __init__(self, payout_probability):
        self.payout_probability = payout_probability

    def __repr__(self):
        return str(self.payout_probability)

    def pull(self):
        if random.choice([0, 1], p=[1 - self.payout_probability, self.payout_probability]):
            return True
        else:
            return False


DEFAULT_NUM_PULLS = 100000
DEFAULT_EXPLORE_PULLS_EACH = 100


def start_win_stay(num_pulls=DEFAULT_NUM_PULLS):
    bandit1 = SlotMachine(.1)
    bandit2 = SlotMachine(.3)
    winning_count = run_win_stay(bandit1, bandit2, num_pulls)
    print('win stay: ', winning_count, winning_count/num_pulls)


def test_references():
    bandit1 = SlotMachine(.1)
    bandit2 = SlotMachine(.3)
    using = bandit1
    other = bandit2
    print('bandit1', bandit1)
    print('bandit2', bandit2)
    print('using', using)
    print('other', other)
    temp = using
    using = other
    other = temp
    print('bandit1', bandit1)
    print('bandit2', bandit2)
    print('using', using)
    print('other', other)


def run_win_stay(bandit1: SlotMachine, bandit2: SlotMachine, num_pulls_to_do):
    """
    If you win, stay on that slot machine till you lose, then go to the other.
    :param bandit1: a SlotMachine object
    :param bandit2: a SlotMachine object
    :param num_pulls_to_do: the number of pulls you can do
    :return:
    """
    using = bandit1
    other = bandit2

    num_pulls_so_far = 0
    winning_count = 0
    while num_pulls_so_far < num_pulls_to_do:
        did_I_win = using.pull()
        num_pulls_so_far += 1
        if did_I_win:
            winning_count += 1
        else:
            temp = using
            using = other
            other = temp

    return winning_count


def start_explore_first(num_pulls=DEFAULT_NUM_PULLS, num_explore_pulls_each=DEFAULT_EXPLORE_PULLS_EACH):
    bandit1 = SlotMachine(.1)
    bandit2 = SlotMachine(.3)
    if num_pulls > 200:
        winning_count = run_explore_first(bandit1, bandit2, num_pulls, num_explore_pulls_each)
        print('win stay n: ', winning_count, winning_count/num_pulls)
    else:
        winning_count = run_win_stay(bandit1, bandit2, num_pulls)
        print('did win stay instead: ', winning_count, winning_count/num_pulls)


def run_explore_first(bandit1: SlotMachine, bandit2: SlotMachine, num_pulls_to_do, num_explore_pulls_each):
    """
    Do a certain number of pulls on each one to guess with has a better payout probability, then use that one
    for the rest of the pulls.
    :param bandit1: a SlotMachine object
    :param bandit2: a SlotMachine object
    :param num_pulls_to_do: the number of pulls you can do
    :param num_explore_pulls_each: how many pulls you will do on each one to guess the payout probability
    :return:
    """

    num_pulls_so_far = 0
    num_pulls_bandit1 = 0
    num_pulls_bandit2 = 0
    winning_count = 0
    winning_count_bandit1 = 0
    winning_count_bandit2 = 0

    # TODO: refactor this to allow for a variable number of bandits
    while num_pulls_bandit1 < num_explore_pulls_each:
        did_I_win = bandit1.pull()
        num_pulls_so_far += 1
        num_pulls_bandit1 += 1
        if did_I_win:
            winning_count += 1
            winning_count_bandit1 += 1

    while num_pulls_bandit2 < num_explore_pulls_each:
        did_I_win = bandit2.pull()
        num_pulls_so_far += 1
        num_pulls_bandit2 += 1
        if did_I_win:
            winning_count += 1
            winning_count_bandit2 += 1

    if winning_count_bandit1 > winning_count_bandit2:
        using = bandit1
    else:
        using = bandit2

    while num_pulls_so_far < num_pulls_to_do:
        did_I_win = using.pull()
        num_pulls_so_far += 1
        if did_I_win:
            winning_count += 1

    return winning_count


def start_alternate(num_pulls=DEFAULT_NUM_PULLS):
    bandit1 = SlotMachine(.1)
    bandit2 = SlotMachine(.3)
    winning_count = run_alternate(bandit1, bandit2, num_pulls)
    print('alternate: ', winning_count, winning_count/num_pulls)


def run_alternate(bandit1:SlotMachine, bandit2: SlotMachine, num_pulls_to_do):
    """
    Alternate between slot machines, regardless of if you win or lose
    :param bandit1: a SlotMachine object
    :param bandit2: a SlotMachine object
    :param num_pulls_to_do: the number of pulls you can do
    :return:
    """
    using = bandit1
    other = bandit2

    num_pulls_so_far = 0
    winning_count = 0
    while num_pulls_so_far < num_pulls_to_do:
        did_I_win = using.pull()
        num_pulls_so_far += 1
        winning_count += did_I_win    # an alternative to if did_I_win: winning_count += 1

        temp = using
        using = other
        other = temp

    return winning_count


start_win_stay()
start_alternate()
start_explore_first()
