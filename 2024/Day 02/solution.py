def is_safe_record(record):
    if (
        sorted(record) in [record, record[::-1]]
        and all([1 <= abs(record[idx] - record[idx - 1]) <= 3 for idx in range(1, len(record))])
    ):
        return True
    return False


def find_safe_reports(lines):
    '''
    Solves the first part of the problem
    '''
    safe_records = 0
    for record in lines:
        if is_safe_record(record):
            safe_records += 1
    return safe_records


def is_safe_record_v2(record):
    if any([is_safe_record(record[:idx]+record[idx+1:]) for idx in range(len(record))]):
        return True
    return False


def find_safe_reports_v2(lines):
    '''
    Solves the second part of the problem
    '''
    safe_records = 0
    for record in lines:
        if is_safe_record(record):
            safe_records += 1
        elif is_safe_record_v2(record):
            safe_records += 1
    return safe_records


def main():
    file = "input.txt"
    with open(file) as f:
        lines = f.read().split("\n")
        for idx in range(len(lines)):
            lines[idx] = list(map(int, lines[idx].split(" ")))

        print("Number of safe records:", find_safe_reports(lines))
        print("Number of safe records v2:", find_safe_reports_v2(lines))


if __name__ == "__main__":
    main()
