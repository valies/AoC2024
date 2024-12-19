from utils.file_reader import read_file_as_ints
from utils.printer import timing_decorator


@timing_decorator
def day_11_part_1(file, runs):
    data = read_file_as_ints(file, " ")[0]
    cache = {}
    count = transform(data, cache, runs)
    return count


def day_11_part_2(file, runs):
    data = read_file_as_ints(file, " ")[0]
    cache = {}
    count = transform(data, cache, runs)
    return count


def transform_stone(stone, cache, runs):
    if runs == 0:
        return 1
    if stone == 0:
        result = transform_stone(1, cache, runs - 1)
    else:
        length = len(str(stone))
        if length % 2 == 0:
            split_index = length // 2
            divisor = 10**split_index
            left = stone // divisor
            right = stone % divisor
            result = transform_stone(left, cache, runs - 1) + transform_stone(
                right, cache, runs - 1
            )
        else:
            if (stone, runs) in cache:
                return cache[stone, runs]
            result = transform_stone(stone * 2024, cache, runs - 1)
            if (stone, runs) not in cache:
                cache[stone, runs] = result
    return result


def transform(data, cache, runs):
    count = 0
    for i in range(len(data)):
        stone = data[i]
        count += transform_stone(stone, cache, runs)

    return count
