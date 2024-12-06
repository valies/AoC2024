import os
import unittest

from src.solution_day_03 import day_03_part_1, day_03_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_03_part1(self):
        self.assertEqual(161, day_03_part_1(self.CURRENT_DIR + '/input_1.txt'))

    def test_day_03_part2(self):
        self.assertEqual(48, day_03_part_2(self.CURRENT_DIR + '/input_2.txt'))


if __name__ == '__main__':
    unittest.main()
