import itertools

from utils.file_reader import read_file_as_char_matrix
from utils.printer import timing_decorator


@timing_decorator
def day_08_part_1(file):
    data = read_file_as_char_matrix(file)

    rows = len(data)
    cols = len(data[0])

    all_antenna_locations = [
        {"antenna": data[i][j], "location": (i, j)}
        for j in range(cols)
        for i in range(rows)
        if data[i][j] != "."
    ]

    antenna_locations_grouped_by_antenna = {}
    for antenna_location in all_antenna_locations:
        antenna = antenna_location["antenna"]
        location = antenna_location["location"]

        if antenna not in antenna_locations_grouped_by_antenna:
            antenna_locations_grouped_by_antenna[antenna] = []
        antenna_locations_grouped_by_antenna[antenna].append(location)

    antinodes = []
    for antenna, locations in antenna_locations_grouped_by_antenna.items():
        combinations = list(itertools.product(locations, repeat=2))

        for combo in combinations:
            if combo[0] != combo[1]:
                (i1, j1), (i2, j2) = combo
                difference_i = i1 - i2
                difference_j = j1 - j2
                antinode_1_i = i1 + difference_i
                antinode_1_j = j1 + difference_j
                antinode_2_i = i2 - difference_i
                antinode_2_j = j2 - difference_j
                if 0 <= antinode_1_i < rows and 0 <= antinode_1_j < cols:
                    antinodes.append((antinode_1_i, antinode_1_j))
                if 0 <= antinode_2_i < rows and 0 <= antinode_2_j < cols:
                    antinodes.append((antinode_2_i, antinode_2_j))

    return len(list(set(antinodes)))
