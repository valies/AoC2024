import os
import unittest

from src.solution_day_09 import day_09_part_1, day_09_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_09_part1(self):
        self.assertEqual(1928, day_09_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_09_part2_example1(self):
        self.assertEqual(2858, day_09_part_2(self.CURRENT_DIR + '/input.txt'))

    def test_day_09_part2_example2(self):
        self.assertEqual(636, day_09_part_2(self.CURRENT_DIR + '/input2.txt'))

    def test_day_09_part2_example3(self):
        self.assertEqual(6204, day_09_part_2(self.CURRENT_DIR + '/input3.txt'))

    def test_day_09_part2_example4(self):
        self.assertEqual(2184, day_09_part_2(self.CURRENT_DIR + '/input4.txt'))


if __name__ == '__main__':
    unittest.main()
