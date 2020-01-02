import unittest
import util


class UtilTest(unittest.TestCase):

    def test_get_first_digit(self):
        self.do_test_one_first_digit(18001, 1)
        self.do_test_one_first_digit(99999, 9)
        self.do_test_one_first_digit(185, 1)
        self.do_test_one_first_digit(2767, 2)
        self.do_test_one_first_digit(3.289, 3)
        self.do_test_one_first_digit(5, 5)
        self.do_test_one_first_digit(67, 6)

    def do_test_one_first_digit(self, number, expected_value):
        self.assertEqual(expected_value, util.get_first_digit(number))
        self.assertEqual(expected_value, util.get_first_digit(-1. * number))

