import os
import unittest

from src.solution_day_12 import day_12_part_1, day_12_part_2


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

    def test_day_12_part2_example1(self):
        self.assertEqual(80, day_12_part_2(self.CURRENT_DIR + '/input.txt'))

    def test_day_12_part2_example2(self):
        self.assertEqual(436, day_12_part_2(self.CURRENT_DIR + '/input2.txt'))

    def test_day_12_part2_example3(self):
        self.assertEqual(368, day_12_part_2(self.CURRENT_DIR + '/input5.txt'))

    def test_day_12_part2_example4(self):
        self.assertEqual(1206, day_12_part_2(self.CURRENT_DIR + '/input3.txt'))


if __name__ == '__main__':
    unittest.main()
