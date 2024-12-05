import os
import unittest

from src.day_05.solution import day_05_part_1, day_05_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_05_part1(self):
        self.assertEqual(143, day_05_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_05_part2(self):
        self.assertEqual(123, day_05_part_2(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
