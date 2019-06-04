from prob_dist import *
import pandas as pd

def get_dict_of_dists1():

    sun = ProbDist({'rain':.25, "clouds": .25, 'sun': .5}, id='sun')
    wind = ProbDist({'still': .4, 'moderate': .35, 'high': .2, 'hurricane': .05}, id='wind')
    return {'sun': sun, 'wind':wind}


def test_joint_dists():
    dists = get_dict_of_dists1()
    num_days = 100000
    sun_dist = dists['sun']
    wind_dist = dists['wind']
    sun_values = sun_dist.get_random_value(num_days)
    wind_values = wind_dist.get_random_value(num_days)

    print('theoretical results')
    theoretical_names = []
    theoretical_nums = []
    sun = sun_dist.data
    wind = wind_dist.data
    for sun_key in sun.keys():
        for wind_key in wind.keys():
            #print((sun_key, wind_key), sun[sun_key] * wind[wind_key] * num_days)
            theoretical_names.append((sun_key, wind_key))
            theoretical_nums.append(sun[sun_key] * wind[wind_key] * num_days)

    theoretical_counts = pd.Series(theoretical_nums, index=theoretical_names).sort_values(ascending=False)
    print(theoretical_counts)

    print('\nsimulated results')
    actuals = []
    for i in range(num_days):
        actuals.append((sun_values[i], wind_values[i]))

    actual_counts = pd.Series(actuals).value_counts()
    print(actual_counts)

    print('\ncomparison')
    for name in theoretical_counts.index:
        print(name, theoretical_counts[name], actual_counts[name], (theoretical_counts[name] - actual_counts[name]) / theoretical_counts[name])


def test_conditional():
    dd = get_dict_of_dists1()
    sun = dd['sun']
    go_outside_given_sun = ProbDist({True:.75, False:.25}, id='sun')
    go_outside_given_clouds = ProbDist({True: 80, False: 20}, id='clouds')
    go_outside_given_rain = ProbDist({True:10, False: 90}, id='rain')
    dist_map = {'sun': go_outside_given_sun, 'clouds': go_outside_given_clouds, 'rain': go_outside_given_rain}
    #print(dist_map[sun.get_random_value()[0]].get_random_value())
    #random_values = dist_map[sun.get_random_value()[0]].get_random_value(10000)
    #print(pd.Series(random_values).value_counts())

    #Now get many random weathers and for each, get a random action of going outside or not
    #I am not at all excited about declaring functions inside functions and accessing variables out of the function's scope.
    #But I was trying to do it with apply() and not a for statement and this is a way I found to do it.
    #TODO:  Keep experimenting with other ways to do it.
    results = []

    def random_value(prob_dist):
        return prob_dist.id, prob_dist.get_random_value()[0]

    def one_random_value(x):
        results.append(random_value(dist_map[x]))

    num_observations = 10000
    weather_dists = sun.get_random_value(num_observations)
    pd.Series(weather_dists).apply(one_random_value)
    results_df = pd.DataFrame({'weather': [x[0] for x in results], 'outside': [x[1] for x in results]})
    #print(results_df.head())
    #print(results_df.weather.value_counts())
    print('\nTheoretical Results')

    theoretical = pd.Series([.6 * num_observations, .4 * num_observations], index=[True, False])
    #calculation of theoretical values
    go_outside = 0
    for sun_key, sun_value in sun.data.items():
        #print(sun_key, sun_value)
        #for outside_key, outside_value in dist_map[sun_key].data.items():
            #print(outside_key, outside_value)
        go_outside = go_outside + sun_value * dist_map[sun_key].data[True]
    theoretical = pd.Series([go_outside * num_observations, (1 - go_outside) * num_observations], index=[True, False])
    print(theoretical)

    print('\nActual Results')
    print(results_df.outside.value_counts())


def chain_prob_dists_mc():

    A = ProbDist({'B': 9, 'False': 1}, id='A')
    B = ProbDist({'C': 9, 'False': 1}, id='B')
    C = ProbDist({'D': 9, 'False': 1}, id='C')
    D = ProbDist({'E': 9, 'False': 1}, id='D')
    E = ProbDist({'True': 1}, id='True')
    F = ProbDist({'False': 1}, id='False')
    prob_dist_map = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'E': E,
        'False': F
    }

    num_chains = 10000
    results = []
    for i in range(num_chains):
        results.append(get_random_prob_dist_chain(prob_dist_map, 'A', 0))
    print(pd.Series(results).value_counts())

    print()
    results = []
    for i in range(num_chains):
        results.append(get_random_prob_dist_chain(prob_dist_map, 'A', 1))
    print(pd.Series(results).value_counts())

    print()
    results = []
    for i in range(num_chains):
        results.append(get_random_prob_dist_chain(prob_dist_map, 'A', 2))
    print(pd.Series(results).value_counts())

    print()
    results = []
    for i in range(num_chains):
        results.append(get_random_prob_dist_chain(prob_dist_map, 'A', 3))
    print(pd.Series(results).value_counts())

    print(4)
    results = []
    for i in range(num_chains):
        results.append(get_random_prob_dist_chain(prob_dist_map, 'A', 4))
    print(pd.Series(results).value_counts())


def get_random_prob_dist(prob_dist_map, prob_dist_name):
    return prob_dist_map[prob_dist_map[prob_dist_name].get_random_value()[0]]


def get_random_prob_dist_chain(prob_dist_map, prob_dist_name, chain_length):
    for i in range(chain_length):
        prob_dist_name = prob_dist_map[prob_dist_name].get_random_value()[0]
    return prob_dist_map[prob_dist_name].get_random_value()[0]

#test_joint_dists()
#test_conditional()
chain_prob_dists_mc()


