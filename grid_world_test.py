import unittest
from grid_world import *


EDGES = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
         (1, 4), (2, 4), (3, 4), (4, 4),
         (4, 3), (4, 2), (4, 1), (4, 0),
         (3, 0), (2, 0), (1, 0)]

REGULAR_POINTS = [(1, 3), (2, 3), (3, 3),
                  (1, 2), (2, 2), (3, 2),
                  (1, 1), (2, 1), (3, 1)]


class GridWorldTest(unittest.TestCase):

    def test_get_next_action(self):
        actions = []
        action_counts = {}
        num_actions = 100000
        for i in range(num_actions):
            action = get_next_action()
            actions.append(action)
            if action in action_counts:
                action_counts[action] += 1
            else:
                action_counts[action] = 1

        #print(action_counts)
        self.assertAlmostEqual(.25, action_counts[UP] / num_actions, delta=.01)
        self.assertAlmostEqual(.25, action_counts[LEFT] / num_actions, delta=.01)
        self.assertAlmostEqual(.25, action_counts[DOWN] / num_actions, delta=.01)
        self.assertAlmostEqual(.25, action_counts[RIGHT] / num_actions, delta=.01)

    def test_get_reward_and_next_location_A_and_B(self):
        result = get_next_location_and_reward(A, UP)
        self.assertEqual(A_PRIME, result[0])
        self.assertEqual((1, 0), result[0])
        self.assertEqual(10, result[1])

        # print(get_next_location(A, RIGHT))
        self.assertEqual((A_PRIME, A_TO_A_PRIME_REWARD), get_next_location_and_reward(A, UP))
        self.assertEqual((A_PRIME, A_TO_A_PRIME_REWARD), get_next_location_and_reward(A, DOWN))
        self.assertEqual((A_PRIME, A_TO_A_PRIME_REWARD), get_next_location_and_reward(A, LEFT))
        self.assertEqual((A_PRIME, A_TO_A_PRIME_REWARD), get_next_location_and_reward(A, RIGHT))

        # print(get_next_location(B, RIGHT))
        self.assertEqual((B_PRIME, B_TO_B_PRIME_REWARD), get_next_location_and_reward(B, UP))
        self.assertEqual((B_PRIME, B_TO_B_PRIME_REWARD), get_next_location_and_reward(B, DOWN))
        self.assertEqual((B_PRIME, B_TO_B_PRIME_REWARD), get_next_location_and_reward(B, LEFT))
        self.assertEqual((B_PRIME, B_TO_B_PRIME_REWARD), get_next_location_and_reward(B, RIGHT))

    def test_get_reward_and_next_location_off_the_grid(self):
        # top
        self.assertEqual(((0, 4), OFF_THE_GRID_REWARD), get_next_location_and_reward((0, 4), UP))
        # self.assertEqual(((1, 4), OFF_THE_GRID_REWARD), get_next_location((1, 4), UP))
        self.assertEqual(((2, 4), OFF_THE_GRID_REWARD), get_next_location_and_reward((2, 4), UP))
        # self.assertEqual(((3, 4), OFF_THE_GRID_REWARD), get_next_location((3, 4), UP))
        self.assertEqual(((4, 4), OFF_THE_GRID_REWARD), get_next_location_and_reward((4, 4), UP))

        # right
        self.assertEqual(((4, 3), OFF_THE_GRID_REWARD), get_next_location_and_reward((4, 3), RIGHT))
        self.assertEqual(((4, 2), OFF_THE_GRID_REWARD), get_next_location_and_reward((4, 2), RIGHT))
        self.assertEqual(((4, 1), OFF_THE_GRID_REWARD), get_next_location_and_reward((4, 1), RIGHT))
        self.assertEqual(((4, 0), OFF_THE_GRID_REWARD), get_next_location_and_reward((4, 0), RIGHT))

        # bottom
        self.assertEqual(((3, 0), OFF_THE_GRID_REWARD), get_next_location_and_reward((3, 0), DOWN))
        self.assertEqual(((2, 0), OFF_THE_GRID_REWARD), get_next_location_and_reward((2, 0), DOWN))
        self.assertEqual(((1, 0), OFF_THE_GRID_REWARD), get_next_location_and_reward((1, 0), DOWN))
        self.assertEqual(((0, 0), OFF_THE_GRID_REWARD), get_next_location_and_reward((0, 0), DOWN))

        # left
        self.assertEqual(((0, 1), OFF_THE_GRID_REWARD), get_next_location_and_reward((0, 1), LEFT))
        self.assertEqual(((0, 2), OFF_THE_GRID_REWARD), get_next_location_and_reward((0, 2), LEFT))
        self.assertEqual(((0, 3), OFF_THE_GRID_REWARD), get_next_location_and_reward((0, 3), LEFT))

    def test_get_reward_next_location_regular(self):

        for point in REGULAR_POINTS:
            self.assertEqual(((point[0], point[1] + 1), REGULAR_REWARD), get_next_location_and_reward(point, UP))
            self.assertEqual(((point[0] + 1, point[1]), REGULAR_REWARD), get_next_location_and_reward(point, RIGHT))
            self.assertEqual(((point[0], point[1] - 1), REGULAR_REWARD), get_next_location_and_reward(point, DOWN))
            self.assertEqual(((point[0] - 1, point[1]), REGULAR_REWARD), get_next_location_and_reward(point, LEFT))

    '''def test_is_edge(self):
        all_points = []
        for x in range(5):
            for y in range(5):
                all_points.append((x, y))

        for point in all_points:
            self.assertEqual((point in EDGES), is_edge(point))'''

    def test_reward_for_one_path(self):
        cumulative = 0
        start = (0, 0)
        location, reward = get_next_location_and_reward(start, RIGHT)
        cumulative += reward
        self.assertEqual((1, 0), location)
        self.assertEqual(0, reward)

        location, reward = get_next_location_and_reward(location, UP)
        cumulative += reward
        self.assertEqual((1, 1), location)
        self.assertEqual(0, reward)

        location, reward = get_next_location_and_reward(location, UP)
        cumulative += reward
        self.assertEqual((1, 2), location)
        self.assertEqual(0, reward)

        location, reward= get_next_location_and_reward(location, LEFT)
        cumulative += reward
        self.assertEqual((0, 2), location)
        self.assertEqual(0, reward)

        location, reward = get_next_location_and_reward(location, UP)
        cumulative += reward
        self.assertEqual((0, 3), location)
        self.assertEqual(0, reward)

        location, reward = get_next_location_and_reward(location, UP)
        cumulative += reward
        self.assertEqual((0, 4), location)
        self.assertEqual(0, reward)

        location, reward = get_next_location_and_reward(location, LEFT)
        cumulative += reward
        self.assertEqual((0, 4), location)
        self.assertEqual(-1, reward)

        location, reward = get_next_location_and_reward(location, RIGHT)
        cumulative += reward
        self.assertEqual((1, 4), location)
        self.assertEqual(0, reward)

        location, reward = get_next_location_and_reward(location, UP)
        cumulative += reward
        self.assertEqual((1, 0), location)
        self.assertEqual(10, reward)
        self.assertEqual(9, cumulative)

        location, reward = get_next_location_and_reward(location, DOWN)
        cumulative += reward
        self.assertEqual((1, 0), location)
        self.assertEqual(-1, reward)
        self.assertEqual(8, cumulative)

        location, reward = get_next_location_and_reward(location, RIGHT)
        cumulative += reward
        self.assertEqual((2, 0), location)
        self.assertEqual(0, reward)
        self.assertEqual(8, cumulative)

    def test_get_random_path(self):
        path, reward = get_one_random_path((2, 2), 1000)
        print(path)
        print(reward)

    def test_get_random_path_parallel(self):
        path, reward = get_one_random_path_parallel(1, (2, 2), 1000)
        print(path)
        print(reward)

    def test_estimate_value(self):
        print(estimate_value((0, 0)))

    def test_estimate_value_numpy(self):
        #print(estimate_value_numpy((0, 0)))
        start = datetime.now()
        begin = time.time()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                print(estimate_value_numpy((x, y)))
        stop = datetime.now()
        end = time.time()
        print('completed in ', (stop.timestamp() - start.timestamp()), 'seconds')
        print('completed in ', (end - begin), 'seconds')

    def test_estimate_all_no_for_loop(self):
        start = datetime.now()
        begin = time.time()
        points = []
        for x in range(WIDTH):
            for y in range(HEIGHT):
                points.append((x, y))

        points.reverse()
        est_value_vect = np.vectorize(estimate_value_numpy)
        est_value_vect(points)
        stop = datetime.now()
        end = time.time()
        print('completed in ', (stop.timestamp() - start.timestamp()), 'seconds')
        print('completed in ', (end - begin), 'seconds')

    def test_estimate_value_cupy(self):
        print(estimate_value_cupy((0, 0)))

    def test_estimate_all(self):
        estimate_all()
