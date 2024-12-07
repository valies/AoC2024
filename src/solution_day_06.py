import multiprocessing
from enum import Enum
from functools import partial

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


@timing_decorator
def day_06_part_2(file):
    data = read_file_as_char_matrix(file)
    start_position = find_start_position(data, "^")

    # generate maps with an obstruction
    data_list, data_drawn = traverse_and_place_obstructions(data)

    # filter new maps to only keep the ones that have a new obstruction "O"
    obstruction_lists = []
    for sub_list in data_list:
        for line in sub_list:
            if "O" in line:
                obstruction_lists.append(sub_list)

    # for each new map: do a traverse: either stop by loop or stop by leaving the map, do it parallel
    useful_obstructions = parallel_processing(
        obstruction_lists, start_position, Direction.UP
    )

    useful_obstructions_as_tuples = [tuple(map) for map in useful_obstructions]
    unique_obstructions = set(useful_obstructions_as_tuples)
    unique_obstructions = {o for o in unique_obstructions if o}

    return len(unique_obstructions)


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

    while 0 < start_position[0] < rows - 1 and 0 < start_position[1] < cols - 1:  # quit when leaving map
        dx, dy = direction_map[direction]
        new_position = (start_position[0] + dx, start_position[1] + dy)

        if data[new_position[0]][new_position[1]] == "#":
            direction = switch_direction(direction, 1)
            data[start_position[0]][start_position[1]] = "B"
        else:
            data[new_position[0]][new_position[1]] = "X"
            start_position = new_position

    return data


def switch_direction(direction, times):
    for _ in range(times):
        direction = directions[(directions.index(direction) + 1) % len(directions)]
    return direction


def parallel_processing(obstruction_lists, start_position, direction):
    start_position = tuple(start_position)
    direction = Direction(direction)

    # Use functools.partial to provide the extra arguments to the function
    partial_traverse = partial(
        traverse_and_keep_infinite_loop,
        start_position=start_position,
        direction=direction,
    )

    # Create a Pool of workers (using number of CPU cores available)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the function with the data in parallel
        results = pool.map(partial_traverse, obstruction_lists)
    return results


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


def traverse_and_place_obstructions(data):
    rows = len(data)
    cols = len(data[0])

    data_list = []

    for r in range(rows):
        for c in range(cols):
            if data[r][c] != "#":
                copy_of_data = [line[:] for line in data]
                copy_of_data[r][c] = "O"
                data_list.append(copy_of_data)

    return data_list, data


def traverse_and_keep_infinite_loop(data, start_position, direction):
    rows = len(data)
    cols = len(data[0])

    visited_positions = set()
    useful_obstructions = []

    position_o = find_o(data)

    while 0 < start_position[0] < rows - 1 and 0 < start_position[1] < cols - 1:  # quit when leaving map
        dx, dy = direction_map[direction]
        new_position = (start_position[0] + dx, start_position[1] + dy)

        if data[new_position[0]][new_position[1]] in ("#", "O"):
            direction = switch_direction(direction, 1)
        else:
            start_position = new_position
            if (start_position, direction) in visited_positions:  # we have a loop
                useful_obstructions.append(position_o)
                return useful_obstructions
            visited_positions.add((start_position, direction))

    return []


def find_o(data):
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == "O":
                return i, j
    return None


def place_obstructions(data, obstruction_side):
    obstruction_data = [line[:] for line in data]
    if obstruction_data[obstruction_side[0]][obstruction_side[1]] != "#":
        obstruction_data[obstruction_side[0]][obstruction_side[1]] = "O"
    return obstruction_data
