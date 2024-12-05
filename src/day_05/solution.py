from collections import defaultdict

from utils.file_reader import read_file_as_strings
from utils.printer import timing_decorator


@timing_decorator
def day_05_part_1(file):
    data = read_file_as_strings(file)

    rules = [r.split("|") for r in data[: data.index("")]]
    rules_dictionary = defaultdict(list)
    for key, value in rules:
        rules_dictionary[key].append(value)

    result = 0

    updates = data[data.index("") + 1 :]
    for update in updates:
        update_numbers = update.split(",")
        ok, middle = is_correctly_ordered(update_numbers, rules_dictionary)
        result += middle if ok else 0
    return result


@timing_decorator
def day_05_part_2(file):
    data = read_file_as_strings(file)

    result = 0

    rules = [r.split("|") for r in data[: data.index("")]]
    rules_dictionary = defaultdict(list)

    for key, value in rules:
        rules_dictionary[key].append(value)

    updates = data[data.index("") + 1 :]
    for update in updates:
        update_numbers = update.split(",")
        update_numbers_ordered = update_numbers[:]
        wrong_at_least_once = False

        while True:
            ok, middle = is_correctly_ordered(update_numbers_ordered, rules_dictionary)
            if not ok:
                wrong_at_least_once = True
                update_numbers_ordered = fix_it(
                    update_numbers_ordered, rules_dictionary
                )
            else:
                break

        result += (
            int(update_numbers_ordered[len(update_numbers_ordered) // 2])
            if wrong_at_least_once
            else 0
        )
    return result


def is_correctly_ordered(update_numbers, rules_dictionary):
    middle = 0
    ok = True
    order_checks = []
    for i in range(len(update_numbers) - 1):
        order_checks.append(update_numbers[i:])
    for order_check in order_checks:
        rules_check = rules_dictionary[order_check[0]]
        for check in order_check[1:]:
            if check not in rules_check:
                ok = False
                break
        if not ok:
            break
    middle += int(update_numbers[len(update_numbers) // 2])
    return ok, middle


def fix_it(update_numbers_ordered, rules_dictionary):
    order_checks = []
    for i in range(len(update_numbers_ordered) - 1):
        order_checks.append(update_numbers_ordered[i:])
    for order_check in order_checks:
        rules_check = rules_dictionary[order_check[0]]
        for check in order_check[1:]:
            if check not in rules_check:
                rules_for_wrong_check = rules_dictionary[check]
                if order_check[0] in rules_for_wrong_check:
                    (
                        update_numbers_ordered[update_numbers_ordered.index(check)],
                        update_numbers_ordered[
                            update_numbers_ordered.index(order_check[0])
                        ],
                    ) = (
                        update_numbers_ordered[
                            update_numbers_ordered.index(order_check[0])
                        ],
                        update_numbers_ordered[update_numbers_ordered.index(check)],
                    )
    return update_numbers_ordered
