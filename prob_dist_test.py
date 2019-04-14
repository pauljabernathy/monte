import unittest
import numpy as np
from prob_dist import *
import pandas as pd


class TestNormalize(unittest.TestCase):

    def test_normalize_data(self):
        data = {'.25': 25, '.3': 30, '.45': 45}
        data = ProbDist.normalize_data(data)
        self.assertEqual({'.25': 0.25, '.3': 0.3, '.45': 0.45}, data)
        self.assertEqual(['.25', '.3', '.45'], list(data.keys()))
        self.assertEqual([.25, .3, .45], list(data.values()))

    def test_normalize_list_with_list(self):
        probs = [25, 30, 45]
        self.assertEqual([.25, .3, .45], ProbDist.normalize_list(probs))

    def test_normalize_list_with_np_array(self):
        probs = np.array([25, 30, 45])
        probs = ProbDist.normalize_list(probs)
        self.assertTrue(np.array(np.array([.25, .3, .45]) == probs).all())


class InstantiationTest(unittest.TestCase):

    def test_instantiate_with_dict_no_lists(self):
        data = {'.25': 25, '.3': 30, '.45': 45}
        p = ProbDist(data)
        self.assertTrue(np.array(np.array([.25, .3, .45]) == p.probs).all())
        self.assertTrue(p.verify_probabilities())


    def test_instantiate_with_dict_and_lists(self):
        """the data dictionary should override the lists"""
        data = {'.25': 25, '.3': 30, '.45': 45}
        values = ['.25', '.3', '.45']
        weights = [250, 30, 45]
        p = ProbDist(data, values= values, probs = weights)
        self.assertTrue(np.array(np.array([.25, .3, .45]) == p.probs).all())
        self.assertTrue(p.verify_probabilities())

    def test_instantiate_with_lists(self):
        values = ['.25', '.3', '.45']
        weights = [25, 30, 45]
        p = ProbDist(values= values, probs = weights)
        self.assertTrue(np.array(np.array([.25, .3, .45]) == p.probs).all())
        self.assertTrue(p.verify_probabilities())

    def test_repeated_items_are_combined(self):
        """only applicable if using a pair of lists, not a dictionary"""
        values = ['.25', '.3', '.45', '.25']
        weights = [20, 30, 45, 5]
        p = ProbDist(values= values, probs = weights)
        self.assertEqual(['.25', '.3', '.45'], p.values)
        self.assertTrue(np.array(np.array([.25, .3, .45]) == p.probs).all())
        self.assertTrue(p.verify_probabilities())

    def test_raise_exception_for_mismatched_lengths(self):
        items = ['.25', '.3', '.45', '46']
        weights = [25, 30, 45]
        try:
            p = ProbDist(values=items, probs=weights)
        except Exception as e:
            self.assertEqual('The set of unique values and probabilities must be equal length.', e.args[0])

    def test_raises_exception_for_no_values_or_probs(self):
        pass

class RandomValueTest(unittest.TestCase):

    def test_get_random_items(self):
        values = ['.25', '.3', '.4', '.05']
        weights = [25, 30, 40, 5]
        p = ProbDist(values=values, probs=weights)
        """results = []
        for i in range(10000):
            results.append(p.get_random_value())

        print(pd.Series(results).value_counts())"""
        #for whatever reason, the above always results in one duplicated name with a count of 1
        print(pd.Series(p.get_random_value(1000000)).value_counts())
        #TODO:  some comparison to the theoretical dist

        d = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
        dist = ProbDist(d)
        random_dice_rolls = dist.get_random_value(1000000)
        #print(pd.Series(random_dice_rolls).value_counts())
        self.assertAlmostEqual(3.5, dist.get_random_value(1000000).mean(), delta=.05)

    @unittest.skip('done to experiment with performace.  Yes, it is much slower than the one above')
    def test_get_many_random_items_of_one(self):
        values = ['.25', '.3', '.4', '.05']
        weights = [25, 30, 40, 5]
        p = ProbDist(values=values, probs=weights)
        results = []
        for i in range(1000000):
            results.append(p.get_random_value())

        print(pd.Series(results).value_counts())
        self.fail('Why did it fail when it was supposeed to skip it?')

class ConditionalRandomValuesTest(unittest.TestCase):

    def test_get_random_values_include_list(self):
        d = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
        dist = ProbDist(d)

        random_evens = dist._get_random_values_include_list([2, 4, 6], 100000)
        print(pd.Series(random_evens).value_counts())
        self.assertAlmostEqual(4, random_evens.mean(), delta=0.05)
        for num in random_evens:
            if num % 2 == 1:
                self.fail(str(num) + ' was odd')

        random_odds = dist._get_random_values_include_list([1, 3, 5], 100000)
        print(pd.Series(random_odds).value_counts())
        self.assertAlmostEqual(3, random_odds.mean(), delta=.05)
        pd.Series(random_odds).apply(self.fail_if_even)
        #TODO: investigate if it is faster to create a Series and apply the function, or do a for statement

    def test_get_random_values_exclude_list(self):
        d = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
        dist = ProbDist(d)

        random_evens = dist._get_random_values_exclude_list([1, 3, 5], 100000)
        evens_series = pd.Series(random_evens)
        print(evens_series.value_counts())
        self.assertAlmostEqual(4, random_evens.mean(), delta=0.05)
        evens_series.apply(self.fail_if_odd)

        random_odds = dist._get_random_values_exclude_list([2, 4, 6], 100000)
        odds_series = pd.Series(random_odds)
        print(odds_series.value_counts())
        self.assertAlmostEqual(3, random_odds.mean(), delta=.05)
        odds_series.apply(self.fail_if_even)

    def fail_if_even(self, number):
        if number % 2 == 0:
            self.fail(str(number) + ' was even')

    def fail_if_odd(self, number):
        if number % 2 == 1:
            self.fail(str(number) + ' was odd')

