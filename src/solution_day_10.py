from utils.file_reader import read_file_as_int_matrix
from utils.printer import timing_decorator


@timing_decorator
def day_10_part_1(file):
    data = read_file_as_int_matrix(file)

    score = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                end_locations = get_end_locations(data, (i, j))
                score += len(set(end_locations))

    return score


@timing_decorator
def day_10_part_2(file):
    data = read_file_as_int_matrix(file)

    total = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                total += get_ratings(data, (i, j))

    return total


def get_end_locations(data, start_location):
    queue = [start_location]
    end_locations = []

    while queue:
        i, j = queue.pop()

        new_locations = []
        if i > 0:
            new_locations.append((i - 1, j))
        if i < len(data) - 1:
            new_locations.append((i + 1, j))
        if j > 0:
            new_locations.append((i, j - 1))
        if j < len(data[0]) - 1:
            new_locations.append((i, j + 1))

        height = data[i][j] + 1

        for new_location in new_locations:
            x, y = new_location
            number = data[x][y]
            if number == height:
                if height == 9:
                    end_locations.append(new_location)
                else:
                    queue.append(new_location)

    return end_locations


def get_ratings(data, start_location):
    queue = [start_location]
    count = 0

    while queue:
        i, j = queue.pop()

        new_locations = []
        if i > 0:
            new_locations.append((i - 1, j))
        if i < len(data) - 1:
            new_locations.append((i + 1, j))
        if j > 0:
            new_locations.append((i, j - 1))
        if j < len(data[0]) - 1:
            new_locations.append((i, j + 1))

        height = data[i][j] + 1

        for new_location in new_locations:
            x, y = new_location
            number = data[x][y]
            if number == height:
                if height == 9:
                    count += 1
                else:
                    queue.append(new_location)

    return count
