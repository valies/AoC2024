def read_file_as_strings(file):
    data = []
    with open(file) as my_file:
        for line in my_file:
            data.append(line.rstrip())
    return data
