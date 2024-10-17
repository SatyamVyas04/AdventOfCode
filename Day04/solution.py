def winning_score(lines):
    total_score = 0
    for line in lines:
        semicolon = line.index(':')
        split_line = line.index("|")
        winning_score = (line[semicolon + 1:split_line].strip()).split()
        winning_score = [int(i) for i in winning_score]
        your_score = (line[split_line + 1:].strip()).split()
        your_score = [int(i) for i in your_score]
        common_numbers = [i for i in your_score if i in winning_score]
        if len(common_numbers) > 0:
            total_score += 2 ** (len(common_numbers) - 1)
    return total_score


def scratchcards(lines):
    scratchcards = [1] * len(lines)
    for i, line in enumerate(lines):
        semi_colon = line.index(':')
        split_line = line.index("|")
        winning_score = (line[semi_colon + 1:split_line].strip()).split()
        winning_score = [int(i) for i in winning_score]
        your_score = (line[split_line + 1:].strip()).split()
        your_score = [int(i) for i in your_score]
        common_numbers = [i for i in your_score if i in winning_score]
        matches = len(common_numbers)
        for j in range(i + 1, min(i + matches + 1, len(lines))):
            scratchcards[j] += scratchcards[i]
    return sum(scratchcards)


if __name__ == "__main__":
    filename = 'input.txt'
    with open("./input.txt", 'r') as file:
        lines = file.read().splitlines()

    result = winning_score(lines)
    print("The total score is:", result)

    result = scratchcards(lines)
    print("The number of scratchcards won is:", result)
