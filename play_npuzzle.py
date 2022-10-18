import pygame
from display_solution import draw_tiles, draw_grid


def move_tile(grid, size, move):
    directions = [
    lambda i, j: (i, j + 1),
    lambda i, j: (i + 1, j),
    lambda i, j: (i, j - 1),
    lambda i, j: (i - 1, j),
    ]
    
    zero = grid.index(0)
    i, j = zero // size, zero % size

    new_i, new_j = directions[move](i, j)

    if size - 1 >= new_i >= 0 and size - 1 >= new_j >= 0:
        grid[size * new_i + new_j], grid[size * i + j] = grid[size * i + j], grid[size * new_i + new_j]
    return grid


def play_npuzzle(grid, size, solved_grid):
    grid = [n for row in grid for n in row]
    solved_grid = [n for row in solved_grid for n in row]
    pygame.init()
    win_size = 100 * size
    window = pygame.display.set_mode((win_size, win_size))
    pygame.display.set_caption(f"{size}x{size} Puzzle")
    window.fill((255, 255, 255))
    draw_grid(window, size)
    draw_tiles(window, grid, size)
    pygame.display.flip()
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    grid = move_tile(grid, size, 0)
                elif event.key == pygame.K_UP:
                    grid = move_tile(grid, size, 1)
                elif event.key == pygame.K_RIGHT:
                    grid = move_tile(grid, size, 2)
                elif event.key == pygame.K_DOWN:
                    grid = move_tile(grid, size, 3)
                elif event.key == pygame.K_ESCAPE:
                    exit()
                else:
                    continue
                window.fill((255, 255, 255))
                draw_grid(window, size)
                draw_tiles(window, grid, size)
                pygame.display.flip()
        if grid == solved_grid:
            break
    pygame.draw.rect(window, (0, 255, 0), (0, 0, 100 * size, 100 * size), 5)
    pygame.display.flip()
    pygame.display.set_caption(f"{size}x{size} Puzzle - SOLVED")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()