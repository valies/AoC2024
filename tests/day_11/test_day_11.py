import os
import unittest

from src.solution_day_11 import day_11_part_1, day_11_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_11_part1(self):
        self.assertEqual(55312, day_11_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_11_part2(self):
        self.assertEqual(65601038650482, day_11_part_2(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
