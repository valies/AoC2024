import os
import unittest

from src.day_02.solution import part_1, part_2


class MyTestCases(unittest.TestCase):
    def test_day_02_part1(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        actual_result = part_1(current_dir + '/input.txt')
        self.assertEqual(2, actual_result)

    def test_day_02_part2(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        actual_result = part_2(current_dir + '/input.txt')
        self.assertEqual(4, actual_result)


if __name__ == '__main__':
    unittest.main()
