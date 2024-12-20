import os
import unittest

from src.solution_day_02 import day_02_part_1, day_02_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_02_part1(self):
        self.assertEqual(2, day_02_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_02_part2(self):
        self.assertEqual(4, day_02_part_2(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
