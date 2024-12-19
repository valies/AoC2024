from utils.file_reader import read_file_as_char_matrix
from utils.printer import timing_decorator


@timing_decorator
def day_12_part_1(file):
    data = read_file_as_char_matrix(file)

    chars = {}
    regions = {}
    visited_locations = []

    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            this_char = data[i][j]

            if (i, j) in visited_locations:
                continue

            visited_locations.append((i, j))

            if this_char in chars:
                chars[this_char] += 1
            else:
                chars[this_char] = 1
            region_id = this_char + "_" + str(chars[this_char])
            regions[region_id], visited_locations_for_region = build_region(
                [(i, j)], data, (i, j), this_char, [(i, j)]
            )
            visited_locations.extend(visited_locations_for_region)

    result = 0

    for region_id, region_locations in regions.items():
        actual_borders = []
        for region_location in region_locations:
            potential_borders = get_adjacent_borders(region_location)
            for border in potential_borders:
                if border not in region_locations:
                    actual_borders.append(border)
        perimeter = len(actual_borders)
        area = len(region_locations)
        result += area * perimeter

    return result


@timing_decorator
def day_12_part_2(file):
    data = read_file_as_char_matrix(file)

    chars = {}
    regions = {}
    visited_locations = []

    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            this_char = data[i][j]

            if (i, j) in visited_locations:
                continue

            visited_locations.append((i, j))

            if this_char in chars:
                chars[this_char] += 1
            else:
                chars[this_char] = 1
            region_id = this_char + "_" + str(chars[this_char])
            regions[region_id], visited_locations_for_region = build_region(
                [(i, j)], data, (i, j), this_char, [(i, j)]
            )
            visited_locations.extend(visited_locations_for_region)

    result = 0

    for region_id, region_locations in regions.items():
        actual_borders = []
        for region_location in region_locations:
            potential_borders = get_adjacent_borders(region_location)
            for border in potential_borders:
                if border not in region_locations:
                    actual_borders.append(border)

        corners = 0
        for region_location in region_locations:
            corners += get_corner_count(data, region_location)
        area = len(region_locations)
        result += area * corners

    return result


def build_region(region, data, start_location, this_char, visited_locations_for_region):
    border_locations = get_surrounding_locations_for_char(
        data, start_location, this_char
    )
    if border_locations:
        for border_location in border_locations:
            if border_location not in visited_locations_for_region:
                visited_locations_for_region.append(border_location)
                region.append(border_location)
                build_region(
                    region,
                    data,
                    border_location,
                    this_char,
                    visited_locations_for_region,
                )
    return region, visited_locations_for_region


def get_surrounding_locations_for_char(data, start_location, this_char):
    surrounding_locations = []

    hor_ver_surrounding_locations = []
    hor_ver_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in hor_ver_directions:
        i, j = start_location
        x, y = direction
        new_i = i + x
        new_j = j + y
        if 0 <= new_i < len(data) and 0 <= new_j < len(data[0]):
            if data[new_i][new_j] == this_char:
                hor_ver_surrounding_locations.append((new_i, new_j))

    diagonal_directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    for direction in diagonal_directions:
        i, j = start_location
        x, y = direction
        new_i = i + x
        new_j = j + y
        if 0 <= new_i < len(data) and 0 <= new_j < len(data[0]):
            if data[new_i][new_j] == this_char:
                borders = get_adjacent_borders((new_i, new_j))
                for border in borders:
                    if (
                        border in hor_ver_surrounding_locations
                    ):  # no diagonal only! needs at least one adjacent location
                        surrounding_locations.append((new_i, new_j))
                        break

    if surrounding_locations:
        surrounding_locations.extend(hor_ver_surrounding_locations)
        return surrounding_locations
    else:
        return hor_ver_surrounding_locations


def get_corner_count(data, location):
    i, j = location
    value = data[i][j]
    neighbors = []  # neighbor means adjacent, but different region
    partners = []  # partner means adjacent, same region
    corners = 0

    # Check upward neighbor
    if (i > 0 and data[i - 1][j] != value) or i <= 0:
        neighbors.append("up")
    else:
        partners.append("up")

    # Check downward neighbor
    if (i < len(data) - 1 and data[i + 1][j] != value) or i >= len(data) - 1:
        neighbors.append("down")
    else:
        partners.append("down")

    # Check left neighbor
    if (j > 0 and data[i][j - 1] != value) or j <= 0:
        neighbors.append("left")
    else:
        partners.append("left")

    # Check right neighbor
    if (j < len(data[0]) - 1 and data[i][j + 1] != value) or j >= len(data[0]) - 1:
        neighbors.append("right")
    else:
        partners.append("right")

    # Check diagonal left up neighbor
    if i > 0 and j > 0 and data[i - 1][j - 1] != value:
        neighbors.append("left-up")

    # Check diagonal up right neighbor
    if i > 0 and j < len(data[0]) - 1 and data[i - 1][j + 1] != value:
        neighbors.append("up-right")

    # Check diagonal right down neighbor
    if i < len(data) - 1 and j < len(data[0]) - 1 and data[i + 1][j + 1] != value:
        neighbors.append("right-down")

    # Check diagonal down left neighbor
    if i < len(data) - 1 and j > 0 and data[i + 1][j - 1] != value:
        neighbors.append("down-left")

    # Check neighbor combinations to find corners
    if "left" in neighbors and "up" in neighbors:
        corners += 1

    if "left" in partners and "up" in partners:
        # Check inner corner by validating inner diagonal
        if "left-up" in neighbors:
            corners += 1

    if "up" in neighbors and "right" in neighbors:
        corners += 1

    if "up" in partners and "right" in partners:
        # Check inner corner by validating inner diagonal
        if "up-right" in neighbors:
            corners += 1

    if "right" in neighbors and "down" in neighbors:
        corners += 1

    if "right" in partners and "down" in partners:
        # Check inner corner by validating inner diagonal
        if "right-down" in neighbors:
            corners += 1

    if "down" in neighbors and "left" in neighbors:
        corners += 1

    if "down" in partners and "left" in partners:
        # Check inner corner by validating inner diagonal
        if "down-left" in neighbors:
            corners += 1

    return corners


def get_adjacent_borders(location):
    borders = []
    left_border = get_left_border(location)
    if left_border:
        borders.append(left_border)
    up_border = get_up_border(location)
    if up_border:
        borders.append(up_border)
    right_border = get_right_border(location)
    if right_border:
        borders.append(right_border)
    down_border = get_down_border(location)
    if down_border:
        borders.append(down_border)
    return borders


def get_left_border(location):
    i, j = location
    left = i - 1
    border = (left, j)
    return border


def get_up_border(location):
    i, j = location
    up = j - 1
    border = (i, up)
    return border


def get_right_border(location):
    i, j = location
    right = j + 1
    border = (i, right)
    return border


def get_down_border(location):
    i, j = location
    down = i + 1
    border = (down, j)
    return border
