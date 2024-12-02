from utils.file_reader import read_file_as_ints


def part_1(file):
    data = read_file_as_ints(file, " ")
    safe_reports = 0
    for report in data:
        safe_reports += 1 if is_report_safe(report) else 0
    return safe_reports


def part_2(file):
    data = read_file_as_ints(file, " ")
    safe_reports = 0
    for report in data:
        is_safe = is_report_safe(report)
        if is_safe:
            safe_reports += 1
        else:
            for i in range(len(report)):
                altered_report = report[:i] + report[i + 1 :]
                is_altered_safe = is_report_safe(altered_report)
                if is_altered_safe:
                    safe_reports += 1
                    break
    return safe_reports


def is_report_safe(report):
    is_safe = False
    differences = []
    for i in range(len(report)):
        if i < len(report) - 1:
            differences.append(abs(report[i + 1] - report[i]))
    if (
        (report == sorted(report) or report == sorted(report, reverse=True))
        and all(i < 4 for i in differences)
        and all(i > 0 for i in differences)
    ):
        is_safe = True
    return is_safe
