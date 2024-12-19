from utils.file_reader import read_file_as_string
from utils.printer import timing_decorator


@timing_decorator
def day_09_part_1(file):
    disk_map = read_file_as_string(file)

    files = generate_files(disk_map)

    moved_files = move_files(files)

    checksum = 0
    for i, file in enumerate(moved_files):
        if file != ".":
            checksum += i * int(file)
    return checksum


@timing_decorator
def day_09_part_2(file):
    disk_map = read_file_as_string(file)

    files = generate_files_v2(disk_map)

    moved_files = move_files_v2(files)

    flat_list = [x for file in moved_files for x in file]

    checksum = 0
    for i, file in enumerate(flat_list):
        if file != ".":
            checksum += i * int(file)
    return checksum


def generate_files(disk_map):
    files = []
    id_to_use = 0
    for i in range(len(disk_map)):
        number = int(disk_map[i])
        if i % 2 == 0:
            for n in range(number):
                files.append(str(id_to_use))
            id_to_use += 1
        else:
            for n in range(number):
                files.append(".")
    return files


def move_files(files):
    first_free_space_index = 0
    last_number_index = len(files) - 1

    while first_free_space_index < last_number_index:

        while (
            first_free_space_index < len(files) and files[first_free_space_index] != "."
        ):
            first_free_space_index += 1
        while last_number_index >= 0 and files[last_number_index] == ".":
            last_number_index -= 1

        if first_free_space_index < last_number_index:
            files[first_free_space_index], files[last_number_index] = (
                files[last_number_index],
                files[first_free_space_index],
            )

            first_free_space_index += 1
            last_number_index -= 1

    return files


def generate_files_v2(disk_map):
    files = []
    id_to_use = 0
    for i in range(len(disk_map)):
        number = int(disk_map[i])
        if i % 2 == 0:
            whole_file = []
            for n in range(number):
                whole_file.append(str(id_to_use))
            if whole_file:
                files.append(whole_file)
            id_to_use += 1
        else:
            whole_free_space = []
            for n in range(number):
                whole_free_space.append(".")
            if whole_free_space:
                files.append(whole_free_space)
    return files


def move_files_v2(files):
    first_free_space_index = 0
    last_number_index = len(files) - 1

    while True:
        file = files[last_number_index]

        if file == files[0]:
            break

        if (
            "." in file
            or first_free_space_index >= last_number_index
            or first_free_space_index > len(files)
        ):
            last_number_index -= 1
            first_free_space_index = 0
            continue

        free_space_file = files[first_free_space_index]

        if "." not in free_space_file:
            first_free_space_index += 1
            continue

        if len(file) > len(free_space_file):
            first_free_space_index += 1
            continue

        if len(files[last_number_index]) == len(free_space_file):
            files[first_free_space_index], files[last_number_index] = (
                files[last_number_index],
                files[first_free_space_index],
            )
        else:
            for i in range(min(len(free_space_file), len(file))):
                files[first_free_space_index][i], files[last_number_index][i] = (
                    file[i],
                    free_space_file[i],
                )

            if len(free_space_file) >= len(file):
                files = split_and_move(files, first_free_space_index, len(file))
                first_free_space_index = 0

            while last_number_index >= 0 and files[last_number_index].count(".") > 0:
                last_number_index -= 1

    return files


def split_and_move(files, index_to_split, split_position):
    sublist = files[index_to_split]

    first_part = sublist[:split_position]
    second_part = sublist[split_position:]

    files.pop(index_to_split)

    files.insert(index_to_split, first_part)
    files.insert(index_to_split + 1, second_part)

    return files
