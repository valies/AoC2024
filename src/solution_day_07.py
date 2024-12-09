from utils.file_reader import read_file_as_list_of_dictionaries
from utils.printer import timing_decorator


@timing_decorator
def day_07_part_1(file):
    data = read_file_as_list_of_dictionaries(file)

    total = 0

    for line in data:
        total += line["result"] if result_is_in_target(line, 0, 0) else 0

    return total


@timing_decorator
def day_07_part_2(file):
    data = read_file_as_list_of_dictionaries(file)

    total = 0

    for line in data:
        total += line["result"] if result_is_in_target_part_2(line, 0, 0) else 0

    return total


def result_is_in_target(line, current_index, current_result):
    if current_index == len(line["numbers"]):
        return current_result == line["result"]
    else:
        current_number = line["numbers"][current_index]
        if result_is_in_target(
            line, current_index + 1, current_result + current_number
        ):
            return True
        if result_is_in_target(
            line, current_index + 1, current_result * current_number
        ):
            return True


def result_is_in_target_part_2(line, current_index, current_result):
    if current_index == len(line["numbers"]):
        return current_result == line["result"]
    else:
        current_number = line["numbers"][current_index]
        if result_is_in_target_part_2(
            line, current_index + 1, current_result + current_number
        ):
            return True
        if result_is_in_target_part_2(
            line, current_index + 1, current_result * current_number
        ):
            return True
        if result_is_in_target_part_2(
            line, current_index + 1, int(str(current_result) + str(current_number))
        ):
            return True
