from copy import deepcopy

def in_bound(i, j, border):
    return i >= border[2] and i <= border[3] and j >= border[0] and j <= border[1]

def swap_numbers(i, j, value, moves, size, grid):
    if not grid[i][j] == value:
        for n in range(size * size - 1) :
            if (grid[n // size][n % size] == value):
                grid[i][j], grid[n // size][n % size] = grid[n // size][n % size], grid[i][j]
                moves += 1
                break
    return grid, moves

def step_zero(i, j, map):
    for n in range(map["size"] * map["size"] - 1):
            if (map["grid"][n // map["size"]][n % map["size"]] == 0):
                return abs(n // map["size"] - i) + abs(n % map["size"] - j)

def is_solvable(map):
    directions = [
    lambda i, j: (i, j + 1),
    lambda i, j: (i + 1, j),
    lambda i, j: (i, j - 1),
    lambda i, j: (i - 1, j),
    ]

    border_reshape = [
    lambda l, r, t, b: (l, r, t + 1, b),
    lambda l, r, t, b: (l, r - 1, t, b),
    lambda l, r, t, b: (l, r, t, b - 1),
    lambda l, r, t, b: (l + 1, r, t, b),
    ]

    border = [0, map["size"] - 1, 0, map["size"] -1]

    turn = 0
    i, j = 0, 0
    index = 1
    moves = 0
    grid_cpy = deepcopy(map["grid"])
    while True:
        direction_func = directions[turn % 4]
        tmp_i, tmp_j = direction_func(i, j)
        if (not in_bound(tmp_i, tmp_j, border)):
            border = [*border_reshape[turn % 4](*border)]
            turn += 1
        else:
            grid_cpy, moves = swap_numbers(i, j, index, moves, map["size"], grid_cpy)
            i, j = tmp_i, tmp_j

            index += 1
            if index >= map["size"] * map["size"]:
                if step_zero(i, j, map) % 2 != moves % 2:
                    print("The map requested is not solvable.")
                    exit()
                return