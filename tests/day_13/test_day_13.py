import os
import unittest

from src.solution_day_13 import day_13_part_1, day_13_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_13_part1(self):
        self.assertEqual(286, day_13_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_13_part1_example2(self):
        self.assertEqual(480, day_13_part_1(self.CURRENT_DIR + '/input2.txt'))

    def test_day_13_part2(self):
        self.assertEqual(480, day_13_part_2(self.CURRENT_DIR + '/input2.txt'))


if __name__ == '__main__':
    unittest.main()
