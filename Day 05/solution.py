def lowest_location_number(seeds, lines):
    for mappings in lines:
        new_numbers = []
        for num in seeds:
            mapped = False
            for dest_start, source_start, length in mappings:
                if source_start <= num < source_start + length:
                    new_num = num - source_start + dest_start
                    new_numbers.append(new_num)
                    mapped = True
                    break
            if not mapped:
                new_numbers.append(num)
        seeds = new_numbers
    return min(seeds)


def lowest_location_number_ranges(seeds, lines):
    ranges = [(seeds[i], seeds[i] + seeds[i + 1])
              for i in range(0, len(seeds), 2)]

    for line in lines:
        new_ranges = []
        while ranges:
            range_start, range_end = ranges.pop(0)
            found_overlap = False

            for dest, source, length in line:
                map_start = source
                map_end = source + length
                offset = dest - source

                if range_start < map_end and range_end > map_start:
                    found_overlap = True
                    if range_start < map_start:
                        ranges.append((range_start, map_start))
                    if range_end > map_end:
                        ranges.append((map_end, range_end))

                    overlap_start = max(range_start, map_start)
                    overlap_end = min(range_end, map_end)
                    new_ranges.append(
                        (overlap_start + offset, overlap_end + offset))
                    break

            if not found_overlap:
                new_ranges.append((range_start, range_end))

        ranges = new_ranges

    return min(start for start, _ in ranges)


if __name__ == "__main__":
    filename = 'input.txt'
    with open(filename, 'r') as file:
        seeds, *blocks = file.read().split("\n\n")
        seeds = list(map(int, seeds.split(":")[1].strip().split()))
        lines = []
        for block in blocks:
            ranges = []
            for range_line in block.splitlines()[1:]:
                ranges.append(list(map(int, range_line.split())))
            lines.append(ranges)

    result = lowest_location_number(seeds, lines)
    print("The lowest location number is:", result)

    result = lowest_location_number_ranges(seeds, lines)
    print("The lowest location number with seed ranges is:", result)
