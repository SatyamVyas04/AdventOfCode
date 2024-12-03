import re


def main():
    file = "input.txt"
    with open(file) as f:
        content = f.read()

        # Part 1
        matches = re.findall(r'mul\((\d+),(\d+)\)', content)
        left_args = [int(match[0]) for match in matches]
        right_args = [int(match[1]) for match in matches]
        results = [left * right for left, right in zip(left_args, right_args)]
        print("Part 1 solution:", sum(results))

        # Part 2
        tokens = re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', content)
        enabled = True
        ans = 0

        i = 0
        while i < len(tokens):
            if tokens[i] == 'do()':
                enabled = True
            elif tokens[i] == 'don\'t()':
                enabled = False
            else:
                left, right = map(int, re.findall(
                    r'mul\((\d+),(\d+)\)', tokens[i])[0])
                if enabled:
                    ans += left * right
            i += 1

        print("Part 2 solution:", ans)


if __name__ == "__main__":
    main()
