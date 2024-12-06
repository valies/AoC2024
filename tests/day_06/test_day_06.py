import os
import unittest

from src.solution_day_06 import day_06_part_1


class MyTestCases(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_day_06_part1(self):
        self.assertEqual(41, day_06_part_1(self.CURRENT_DIR + '/input.txt'))


if __name__ == '__main__':
    unittest.main()
