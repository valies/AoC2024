from src.day_01.solution import part_1 as day_01_part_1
from src.day_01.solution import part_2 as day_01_part_2
from src.day_02.solution import part_1 as day_02_part_1
from src.day_02.solution import part_2 as day_02_part_2
from utils.printer import pretty_print

if __name__ == '__main__':
    pretty_print("day 01 part 01", day_01_part_1("./src/day_01/input.txt"))
    pretty_print("day 01 part 02", day_01_part_2("./src/day_01/input.txt"))
    pretty_print("day 02 part 01", day_02_part_1("./src/day_02/input.txt"))
    pretty_print("day 02 part 02", day_02_part_2("./src/day_02/input.txt"))
