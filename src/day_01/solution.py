from utils.file_reader import read_file_as_strings


def part_1(file):
    data = read_file_as_strings(file)
    left, right = zip(*[map(int, string.split()) for string in data])
    result = sum(
        abs(sorted(right)[index] - sorted(left)[index]) for index in range(len(left))
    )
    return result


def part_2(file):
    data = read_file_as_strings(file)
    left, right = zip(*[map(int, string.split()) for string in data])
    result = sum(right.count(number) * number for number in left)
    return result
