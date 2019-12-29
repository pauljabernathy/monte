import numpy as np
import pandas as pd
import time

DEFAULT_CHAIN_LENGTH = 10000
DEFAULT_NUM_CHAINS = 1000

"""
simulating https://stats.stackexchange.com/questions/165/how-would-you-explain-markov-chain-monte-carlo-mcmc-to-a-layperson
P(Next day is Sunny|Given today is Rainy)=0.50 
P(Next day is Rainy|Given today is Rainy)=0.50
P(Next day is Rainy|Given today is Sunny)=0.10
P(Next day is Sunny|Given today is Sunny)=0.90


"""
transition_probs = np.asarray([.9, .1, .5, .5]).reshape(2, 2)  # transition probs given


def get_one_chain(length=DEFAULT_CHAIN_LENGTH):
    """returns 1 if rainy on the last day of the chain, 0 if sunny"""
    current = np.random.choice([0, 1])  # randomly chose sunny or rainy with equal probability
    sum = current
    for i in np.arange(length):
        current = np.random.choice([0, 1], p=transition_probs[current])
        sum += current
    return current


def do_sim(chain_length=DEFAULT_CHAIN_LENGTH, num_chains=DEFAULT_NUM_CHAINS):
    count = 0   # number of rainy days at the end of the chain
    for i in np.arange(num_chains):
        count += get_one_chain(chain_length)
    return count


def do_sim_with_pandas(chain_length=DEFAULT_CHAIN_LENGTH, num_chains=DEFAULT_NUM_CHAINS):
    series = pd.Series(np.arange(num_chains))
    values = series.apply(lambda x: get_one_chain(chain_length))
    return values.sum()


num_chains = 100  # DEFAULT_NUM_CHAINS
chain_length = 1000

point_one = time.time()
loop_results = do_sim(chain_length, num_chains)
point_two = time.time()
print('percentage rainy days at end of chain, using for loop', loop_results / num_chains, str(point_two - point_one) + ' millis')
point_three = time.time()
pandas_results = do_sim_with_pandas(chain_length, num_chains)
point_four = time.time()
print('percentage rainy days at end of chain, using pandas', pandas_results / num_chains, str(point_four - point_three) + ' millis')
