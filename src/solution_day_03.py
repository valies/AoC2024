import re

from utils.file_reader import read_file_as_strings
from utils.printer import timing_decorator


@timing_decorator
def day_03_part_1(file):
    data = read_file_as_strings(file)

    multiplications = []
    pattern = r"mul\(([0-9]+),([0-9]+)\)"
    [multiplications.extend(re.findall(pattern, line)) for line in data]

    return sum(int(x) * int(y) for x, y in multiplications)


@timing_decorator
def day_03_part_2(file):
    data = read_file_as_strings(file)

    matches = []
    pattern = r"(mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\))"
    [matches.append(re.findall(pattern, line)) for line in data]

    my_sum = 0
    do = True
    for i in range(len(data)):
        for match in matches[i]:
            if "do()" == match[0]:
                do = True
            elif "don't()" == match[0]:
                do = False
            else:
                if do:
                    my_sum += int(match[1]) * int(match[2])
    return my_sum
