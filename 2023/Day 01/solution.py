def replace_spelled_numbers(word):
    number_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    result = ''
    i = 0
    while i < len(word):
        if word[i].isdigit():
            result += word[i]
        else:
            for num_word, digit in number_words.items():
                if word[i:].startswith(num_word):
                    result += digit
                    break
            else:
                result += word[i]
        i += 1
    return result


def calculate_calibration():
    with open("input.txt", 'r') as file:
        total = 0
        for line in file:
            digits = [char for char in line if char.isdigit()]
            if digits:
                total += int(digits[0] + digits[-1])
    return total


def calculate_calibration_with_replacement():
    with open("input.txt", 'r') as file:
        total = 0
        for line in file:
            processed_line = replace_spelled_numbers(line)
            digits = [char for char in processed_line if char.isdigit()]
            if digits:
                total += int(digits[0] + digits[-1])
    return total


if __name__ == "__main__":
    filename = 'input.txt'
    part1_result = calculate_calibration()
    part2_result = calculate_calibration_with_replacement()
    print(f"Calibration Value: {part1_result}")
    print(f"Calibration Value with replacements: {part2_result}")
