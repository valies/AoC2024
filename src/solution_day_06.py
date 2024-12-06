from enum import Enum

from utils.file_reader import read_file_as_char_matrix
from utils.printer import timing_decorator


@timing_decorator
def day_06_part_1(file):
    data = read_file_as_char_matrix(file)
    start_position = find_start_position(data, "^")
    data = traverse(data, start_position, Direction.UP)
    count_b = sum(row.count("B") for row in data)
    count_x = sum(row.count("X") for row in data)
    return count_b + count_x


def find_start_position(data, start_char):
    start_position = (0, 0)
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == start_char:
                start_position = (i, j)
                break
        if start_position != (0, 0):
            break
    return start_position


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


directions = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]


direction_map = {
    Direction.UP: (-1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1),
}


def traverse(data, start_position, direction):
    rows = len(data)
    cols = len(data[0])

    data[start_position[0]][start_position[1]] = "X"

    while True:
        if (
            start_position[0] >= rows - 1
            or start_position[0] <= 0
            or start_position[1] >= cols - 1
            or start_position[1] <= 0
        ):
            break

        dx, dy = direction_map[direction]
        new_position = (start_position[0] + dx, start_position[1] + dy)

        if data[new_position[0]][new_position[1]] == "#":
            direction = switch_direction(direction)
            data[start_position[0]][start_position[1]] = "B"
        else:
            data[new_position[0]][new_position[1]] = "X"
            start_position = new_position

    return data


def switch_direction(direction):
    return directions[(directions.index(direction) + 1) % len(directions)]
