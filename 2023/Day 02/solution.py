from collections import defaultdict


def parse_game(game_string):
    game_id, draws = game_string.split(':')
    game_id = int(game_id.split()[1])
    return game_id, [parse_draw(draw.strip()) for draw in draws.split(';')]


def parse_draw(draw_string):
    counts = defaultdict(int)
    for cube in draw_string.split(','):
        count, color = cube.strip().split()
        counts[color] += int(count)
    return counts


def calculate_possible_games_sum():
    limits = {"red": 12, "green": 13, "blue": 14}
    with open("input.txt", 'r') as file:
        total = 0
        for line in file:
            game_id, draws = parse_game(line)
            if all(all(count <= limits[color] for color, count in draw.items()) for draw in draws):
                total += game_id
    return total


def calculate_power_sum():
    with open("input.txt", 'r') as file:
        total = 0
        for line in file:
            _, draws = parse_game(line)
            max_counts = defaultdict(int)
            for draw in draws:
                for color, count in draw.items():
                    max_counts[color] = max(max_counts[color], count)
            total += max_counts['red'] * \
                max_counts['green'] * max_counts['blue']
    return total


if __name__ == "__main__":
    filename = 'input.txt'
    part1_result = calculate_possible_games_sum(filename)
    part2_result = calculate_power_sum(filename)
    print(f"Sum of possible game IDs: {part1_result}")
    print(f"Sum of game powers: {part2_result}")
