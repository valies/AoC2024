from utils.file_reader import read_file_as_ints
from utils.printer import timing_decorator


@timing_decorator
def day_11_part_1(file):
    data = read_file_as_ints(file, " ")[0]
    cache = {}
    for i in range(25):
        data, cache = transform(data, cache)

    return len(data)


@timing_decorator
def day_11_part_2(file):
    data = read_file_as_ints(file, " ")[0]
    cache = {}
    for i in range(75):
        data, cache = transform(data, cache)

    return len(data)


def transform_stone(stone, cache):
    if stone in cache:
        return cache[stone]
    if stone == 0:
        result = (1,)
    else:
        stone_str = str(stone)
        if len(str(stone)) % 2 == 0:
            split_index = len(stone_str) // 2
            left = int(stone_str[:split_index])
            right = int(stone_str[split_index:])
            result = (left, right)
        else:
            result = (stone * 2024,)
    cache[stone] = result
    return result


def transform(data, cache):
    transformed_data = []
    bump = 0
    for i in range(len(data)):
        stone = data[i]
        transformed_stone_data = transform_stone(stone, cache)
        transformed_data.extend(transformed_stone_data)
        bump += len(transformed_stone_data) - 1
    return transformed_data, cache
