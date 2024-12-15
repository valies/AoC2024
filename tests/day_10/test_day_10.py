import os
import unittest

from src.solution_day_10 import day_10_part_1, day_10_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_10_part1(self):
        self.assertEqual(36, day_10_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_10_part2(self):
        self.assertEqual(81, day_10_part_2(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
