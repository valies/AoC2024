import os
import unittest

from src.solution_day_08 import day_08_part_1, day_08_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_08_part1(self):
        self.assertEqual(14, day_08_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_08_part2(self):
        self.assertEqual(34, day_08_part_2(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
