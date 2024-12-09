import os
import unittest

from src.solution_day_07 import day_07_part_1, day_07_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_07_part1(self):
        self.assertEqual(3749, day_07_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_07_part2(self):
        self.assertEqual(11387, day_07_part_2(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
