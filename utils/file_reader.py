def read_file_as_strings(file):
    data = []
    with open(file) as my_file:
        for line in my_file:
            data.append(line.rstrip())
    return data


def read_file_as_string(file):
    with open(file) as my_file:
        return my_file.read().rstrip()


def read_file_as_ints(file, separator):
    data = []
    with open(file) as my_file:
        for line in my_file:
            data.append(list(map(int, line.rstrip().split(separator))))
    return data


def read_file_as_char_matrix(file):
    data = []
    with open(file) as my_file:
        for line in my_file:
            data.append(list(line.rstrip()))
    return data


def read_file_as_int_matrix(file):
    data = []
    with open(file) as my_file:
        for line in my_file:
            data.append(list(map(int, line.rstrip())))
    return data


def read_file_as_list_of_dictionaries(file):
    data = []
    with open(file) as my_file:
        for line in my_file:
            line = line.rstrip().replace(":", "")
            data.append(
                {
                    "result": int(line.split()[0]),
                    "numbers": list(map(int, list(line.split()[1:]))),
                }
            )
    return data
