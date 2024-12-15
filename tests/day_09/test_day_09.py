import os
import unittest

from src.solution_day_09 import day_09_part_1, day_09_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_09_part1(self):
        self.assertEqual(1928, day_09_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_09_part2(self):
        self.assertEqual(2858, day_09_part_2(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
