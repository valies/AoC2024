import os
import unittest

from src.day_01.solution import day_01_part_1, day_01_part_2


class MyTestCases(unittest.TestCase):
    def test_day_01_part1(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        actual_result = day_01_part_1(current_dir + '/input.txt')
        self.assertEqual(11, actual_result)

    def test_day_01_part2(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        actual_result = day_01_part_2(current_dir + '/input.txt')
        self.assertEqual(31, actual_result)


if __name__ == '__main__':
    unittest.main()
