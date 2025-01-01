def scan_obstacles(grid):
    """Scans the grid for obstacles (#) and returns their positions."""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                yield (r, c)


def guard_simulation(grid, obstacles, r, c, directions=None, idx=0):
    """
    Simulates the guard's movement for Part 1.
    Tracks visited positions until the guard leaves the grid.
    """
    if directions is None:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set([(r, c)])

    while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        dr, dc = directions[idx]
        next_r, next_c = r + dr, c + dc

        if (next_r, next_c) in obstacles:
            idx = (idx + 1) % len(directions)
            continue

        if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]):
            break

        r, c = next_r, next_c
        visited.add((r, c))

    return visited


def guard_simulation_2(grid, obstacles, r, c, visited, directions=None, idx=0):
    """
    Simulates the guard's movement for Part 2.
    Detects if the guard enters a loop by revisiting a state.
    """
    if directions is None:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        dr, dc = directions[idx]
        next_r, next_c = r + dr, c + dc

        if (next_r, next_c, directions[idx]) in visited:
            return True

        if (next_r, next_c) in obstacles:
            idx = (idx + 1) % len(directions)
            continue

        if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]):
            break

        r, c = next_r, next_c
        visited.add((r, c, directions[idx]))

    return False


def helper(grid, obstacles, candidates, guard_r, guard_c, directions=None, idx=0):
    """
    Helper function for Part 2.
    Tries placing obstacles at each "." position and checks if a loop forms.
    """
    if directions is None:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ans = 0
    for (r, c) in candidates:
        if grid[r][c] == "." and (r, c) != (guard_r, guard_c):
            print("Trying", r, c, grid[r][c])  # Debugging
            grid[r][c] = "#"
            obstacles.add((r, c))
            visited = set([(guard_r, guard_c, directions[idx])])
            in_loop = guard_simulation_2(
                grid, obstacles, guard_r, guard_c, visited)
            if in_loop:
                print("Loop detected at", r, c)  # Debugging
                ans += 1
            obstacles.remove((r, c))
            grid[r][c] = "."
    return ans


def main():
    file = "input.txt"
    with open(file) as f:
        data = f.read().strip()
    rows = data.split("\n")
    grid = [list(row) for row in rows]

    obstacles = set(list(scan_obstacles(grid)))
    guard_r, guard_c = [(r, c) for r in range(len(grid))
                        for c in range(len(grid[0])) if grid[r][c] == "^"][0]

    # Part 1: Predict the guard's path
    visited_positions = guard_simulation(grid, obstacles, guard_r, guard_c)
    print("Part 1:", len(visited_positions))

    # Part 2: Determine possible loop-inducing obstacle placements
    possible_obstacles = helper(
        grid, obstacles, sorted(visited_positions), guard_r, guard_c)
    print("Part 2:", possible_obstacles)


if __name__ == "__main__":
    main()
