from utils.file_reader import read_file_as_char_matrix
from utils.printer import timing_decorator


@timing_decorator
def day_04_part_1(file):
    matrix = read_file_as_char_matrix(file)
    horizontal = find_horizontal(matrix)
    transposed_matrix = [list(row) for row in zip(*matrix)]
    vertical = find_horizontal(transposed_matrix)
    diagonal = find_diagonal_xmas(matrix, "X", ["M", "A", "S"])
    return horizontal + vertical + diagonal


@timing_decorator
def day_04_part_2(file):
    matrix = read_file_as_char_matrix(file)
    return find_diagonal_cross_mas(matrix)


def find_horizontal(matrix):
    counter = 0
    for line in matrix:
        check_line = "".join(line)
        counter += check_line.count("XMAS")
        counter += check_line.count("SAMX")
    return counter


def find_diagonal_xmas(matrix, start_char, find_chars):
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    rows = len(matrix)
    cols = len(matrix[0])
    counter = 0
    for i in range(len(matrix)):
        line = matrix[i]
        for j in range(len(line)):
            a_char = line[j]
            if a_char == start_char:
                for r, c in directions:
                    found = True
                    for k in range(len(find_chars)):
                        check_row_index = i + ((k + 1) * r)
                        check_col_index = j + ((k + 1) * c)
                        if (
                            not 0 <= check_row_index < rows
                            or not 0 <= check_col_index < cols
                        ):
                            found = False
                            break
                        if matrix[check_row_index][check_col_index] != find_chars[k]:
                            found = False
                            break
                    counter += 1 if found else 0
    return counter


def find_diagonal_cross_mas(matrix):
    directions = [[(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]
    counter = 0
    a_counter = 0
    for i in range(len(matrix)):
        line = matrix[i]
        for j in range(len(line)):
            a_char = line[j]
            if (
                a_char == "A" and 0 < i < len(matrix) - 1 and 0 < j < len(matrix[0]) - 1
            ):  # A can't be in first or last row/col when forming cross MAS so skip these rows and cols
                a_counter += 1
                cross_legs = 0
                for direction in directions:
                    general_r, general_c = direction[0]
                    matching_r, matching_c = direction[1]
                    check_row_index_general = i + general_r
                    check_col_index_general = j + general_c
                    check_row_index_matching = i + matching_r
                    check_col_index_matching = j + matching_c
                    if (
                        matrix[check_row_index_general][check_col_index_general] == "S"
                        and matrix[check_row_index_matching][check_col_index_matching]
                        == "M"
                    ):
                        cross_legs += 1
                    if (
                        matrix[check_row_index_general][check_col_index_general] == "M"
                        and matrix[check_row_index_matching][check_col_index_matching]
                        == "S"
                    ):
                        cross_legs += 1
                if cross_legs == 2:
                    counter += 1
    return counter
