import os
import unittest

from src.solution_day_06 import day_06_part_1, day_06_part_2


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_06_part1(self):
        self.assertEqual(41, day_06_part_1(self.CURRENT_DIR + '/input.txt'))

    def test_day_06_part2(self):
        self.assertEqual(6, day_06_part_2(self.CURRENT_DIR + '/input.txt'))
        # 6,3 OK
        # 7,6 OK
        # 7,7 OK
        # 8,1 OK
        # 8,3 OK
        # 9,7 OK


if __name__ == '__main__':
    unittest.main()
