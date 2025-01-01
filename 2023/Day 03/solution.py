def find_number_scan(line, index, visited):
    number = ''
    left_index = index
    right_index = index + 1

    while left_index >= 0 and line[left_index].isdigit():
        number = line[left_index] + number
        visited.add((line, left_index))
        left_index -= 1

    while right_index < len(line) and line[right_index].isdigit():
        number += line[right_index]
        visited.add((line, right_index))
        right_index += 1

    return int(number) if number else None


def find_adjacents(lines):
    total_sum = 0
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit() or char == '.':
                continue

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < len(lines) and 0 <= nj < len(lines[ni])
                    and lines[ni][nj].isdigit()
                    and (lines[ni], nj) not in visited
                ):
                    number = find_number_scan(lines[ni], nj, visited)
                    if number is not None:
                        total_sum += number

    return total_sum


def find_gear_ratio(lines):
    total_sum = 0
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit() or char == '.':
                continue
            if char == "*":
                gear_ratio = 1
                count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < len(lines) and 0 <= nj < len(lines[ni])
                        and lines[ni][nj].isdigit()
                        and (lines[ni], nj) not in visited
                    ):
                        number = find_number_scan(lines[ni], nj, visited)
                        if number is not None:
                            gear_ratio *= number
                            count += 1
                if count > 1:
                    total_sum += gear_ratio

    return total_sum


if __name__ == "__main__":
    filename = 'input.txt'
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    result = find_adjacents(lines)
    print(f"The sum of all part numbers is: {result}")
    result_gear = find_gear_ratio(lines)
    print(f"The gear ratio is: {result_gear}")
