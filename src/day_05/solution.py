from collections import defaultdict

from utils.file_reader import read_file_as_strings
from utils.printer import timing_decorator


@timing_decorator
def day_05_part_1(file):
    data = read_file_as_strings(file)

    rules_dictionary = defaultdict(set)
    for rule in data[: data.index("")]:
        key, value = rule.split("|")
        rules_dictionary[key].add(value)

    result = 0

    updates = data[data.index("") + 1 :]
    for update in updates:
        update_numbers = update.split(",")
        ok, middle = is_correctly_sorted(update_numbers, rules_dictionary)
        result += middle if ok else 0
    return result


@timing_decorator
def day_05_part_2(file):
    data = read_file_as_strings(file)

    result = 0

    rules_dictionary = defaultdict(list)
    for rule in data[: data.index("")]:
        key, value = rule.split("|")
        rules_dictionary[key].append(value)

    updates = data[data.index("") + 1 :]
    for update in updates:
        update_numbers = update.split(",")
        wrong_at_least_once = False

        while True:
            ok, middle = is_correctly_sorted(update_numbers, rules_dictionary)
            if not ok:
                wrong_at_least_once = True
                update_numbers = fix_it(update_numbers, rules_dictionary)
            else:
                break

        result += (
            int(update_numbers[len(update_numbers) // 2]) if wrong_at_least_once else 0
        )
    return result


def is_correctly_sorted(update_numbers, rules_dictionary):
    middle = int(update_numbers[len(update_numbers) // 2])
    ok = True
    for i in range(len(update_numbers) - 1):
        sort_check = update_numbers[i:]
        rules_check = rules_dictionary.get(sort_check[0], set())

        for check in sort_check[1:]:
            if check not in rules_check:
                ok = False
                break
        if not ok:
            break
    return ok, middle


def fix_it(update_numbers, rules_dictionary):
    for i in range(len(update_numbers) - 1):
        sort_check = update_numbers[i:]
        rules_check = rules_dictionary.get(sort_check[0], set())
        for check in sort_check[1:]:
            if check not in rules_check:
                rules_for_wrong_check = rules_dictionary[check]
                if sort_check[0] in rules_for_wrong_check:
                    (
                        update_numbers[update_numbers.index(check)],
                        update_numbers[update_numbers.index(sort_check[0])],
                    ) = (
                        update_numbers[update_numbers.index(sort_check[0])],
                        update_numbers[update_numbers.index(check)],
                    )
    return update_numbers
