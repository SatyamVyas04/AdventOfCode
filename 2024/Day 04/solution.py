directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]


def dfs(grid, r, c, word, direction):
    '''Solves part 1 of the problem'''
    word_length = len(word)
    path = []

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    dr, dc = directions[direction]

    curr_r, curr_c = r, c

    for i in range(word_length):
        if (0 <= curr_r < len(grid) and
            0 <= curr_c < len(grid[0]) and
                grid[curr_r][curr_c] == word[i]):

            path.append(grid[curr_r][curr_c])

            curr_r += dr
            curr_c += dc
        else:
            return False

    return True if len(path) == word_length else False


def find_mas(r, c, grid):
    '''Solves part 2 of the problem'''
    diagonals = directions[4:]
    for dr, dc in diagonals:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] in ['M', 'S']:
            continue
        else:
            return False

    dr1, dc1 = diagonals[0]
    dr2, dc2 = diagonals[1]
    word1 = grid[r + dr1][c + dc1] + "A" + grid[r - dr1][c - dc1]
    word2 = grid[r + dr2][c + dc2] + "A" + grid[r - dr2][c - dc2]
    valid_words = ["MAS", "SAM"]
    if word1 in valid_words and word2 in valid_words:
        return True
    return False


def helper(grid):
    '''
    Helper function calls the dfs function to find the number of XMAS in the grid and also calls the find_mas function to find the number of MAS in the grid
    '''
    word = "XMAS"
    xmas_count = 0
    mas_count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'X':
                for direction in range(8):
                    if dfs(grid, r, c, word, direction):
                        xmas_count += 1
            elif grid[r][c] == "A":
                if find_mas(r, c, grid):
                    mas_count += 1

    return xmas_count, mas_count


def main():
    file = "input.txt"
    with open(file) as f:
        grid = [list(line.strip()) for line in f]

    part1, part2 = helper(grid)

    print("Number of XMAS found:", part1)
    print("Number of MAS found:", part2)


if __name__ == "__main__":
    main()
