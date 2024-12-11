import concurrent.futures
from multiprocessing import Manager

from utils.file_reader import read_file_as_char_matrix
from utils.printer import timing_decorator


@timing_decorator
def day_08_part_1(file):
    data = read_file_as_char_matrix(file)

    rows = len(data)
    cols = len(data[0])

    all_antenna_locations = get_all_antenna_locations(data, rows, cols)

    antenna_locations_grouped_by_antenna = group_by_antenna(all_antenna_locations)

    data, antinodes = get_antinodes(data, antenna_locations_grouped_by_antenna)

    return len(list(set(antinodes)))


@timing_decorator
def day_08_part_2(file):
    data = read_file_as_char_matrix(file)

    rows = len(data)
    cols = len(data[0])

    all_antenna_locations = get_all_antenna_locations(data, rows, cols)

    antenna_locations_grouped_by_antenna = group_by_antenna(all_antenna_locations)

    data, antinodes = get_antinodes_v2(data, antenna_locations_grouped_by_antenna)

    return len(list(set(antinodes)))


def get_all_antenna_locations(data, rows, cols):
    return [
        {"antenna": data[i][j], "location": (i, j)}
        for j in range(cols)
        for i in range(rows)
        if data[i][j] != "."
    ]


def group_by_antenna(all_antenna_locations):
    antenna_locations_grouped_by_antenna = {}
    for antenna_location in all_antenna_locations:
        antenna = antenna_location["antenna"]
        location = antenna_location["location"]

        if antenna not in antenna_locations_grouped_by_antenna:
            antenna_locations_grouped_by_antenna[antenna] = []
        antenna_locations_grouped_by_antenna[antenna].append(location)
    return antenna_locations_grouped_by_antenna


def get_antinodes(data, antenna_locations_grouped_by_antenna):
    rows = len(data)
    cols = len(data[0])

    antinodes = []
    for antenna, locations in antenna_locations_grouped_by_antenna.items():
        for i1, j1 in locations:
            for i2, j2 in locations:
                if (i1, j1) != (i2, j2):
                    difference_i = i1 - i2
                    difference_j = j1 - j2

                    antinode_1_i = i1 + difference_i
                    antinode_1_j = j1 + difference_j
                    if 0 <= antinode_1_i < rows and 0 <= antinode_1_j < cols:
                        antinodes.append((antinode_1_i, antinode_1_j))
                        data[antinode_1_i][antinode_1_j] = "#"

                    antinode_2_i = i2 - difference_i
                    antinode_2_j = j2 - difference_j
                    if 0 <= antinode_2_i < rows and 0 <= antinode_2_j < cols:
                        antinodes.append((antinode_2_i, antinode_2_j))
                        data[antinode_2_i][antinode_2_j] = "#"
    return data, antinodes


def get_antinodes_v2(data, antenna_locations_grouped_by_antenna):
    # Use Manager to allow shared mutable data for storing antinodes
    with Manager() as manager:
        antinodes = (
            manager.list()
        )  # Shared list for storing results from different processes

        # List of futures for parallel execution
        futures = []

        # Create a process pool for processing antennas in parallel
        with concurrent.futures.ProcessPoolExecutor() as executor:
            # Submit tasks to process each antenna in parallel
            for antenna, locations in antenna_locations_grouped_by_antenna.items():
                futures.append(
                    executor.submit(process_antenna, data, locations, antinodes)
                )

            # Wait for all tasks to finish and combine results
            for future in futures:
                future.result()  # This will raise any exceptions that occurred in the process

        return data, list(antinodes)


def process_antenna(data, locations, antinodes):
    for i1, j1 in locations:
        for i2, j2 in locations:
            if (i1, j1) != (i2, j2):
                difference_i = i1 - i2
                difference_j = j1 - j2

                result = find_antinodes(data, i1, j1, difference_i, difference_j)
                if result:
                    data, direction_1 = result
                    antinodes.extend(direction_1)

                result = find_antinodes(data, i2, j2, difference_i, difference_j)
                if result:
                    data, direction_2 = result
                    antinodes.extend(direction_2)


def find_antinodes(data, i, j, difference_i, difference_j):
    rows = len(data)
    cols = len(data[0])

    stack = [(i, j)]

    antinodes = []

    while stack:
        x, y = stack.pop()

        antinode_i = x + difference_i
        antinode_j = y + difference_j

        if 0 <= antinode_i < rows and 0 <= antinode_j < cols:
            antinodes.append((antinode_i, antinode_j))
            data[antinode_i][antinode_j] = "#"
            stack.append((antinode_i, antinode_j))

    if antinodes:
        return data, antinodes
    else:
        return None
