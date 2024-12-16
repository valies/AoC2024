import os
import unittest

from src.solution_day_12 import day_12_part_1


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_12_part1_example1(self):
        self.assertEqual(140, day_12_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_12_part1_example2(self):
        self.assertEqual(772, day_12_part_1(self.CURRENT_DIR + '/input2.txt'))

    def test_day_12_part1_example3(self):
        self.assertEqual(1930, day_12_part_1(self.CURRENT_DIR + '/input3.txt'))

    def test_day_12_part1_example4(self):
        self.assertEqual(16, day_12_part_1(self.CURRENT_DIR + '/input4.txt'))


if __name__ == '__main__':
    unittest.main()
