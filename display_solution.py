from time import sleep
import pygame

def draw_tiles(window, grid, size):
    font = pygame.font.SysFont('arial', 50)
    for i, value in enumerate(grid):
        text = font.render(str(value), True, (0, 0, 0))
        if value == 0:
            continue
        if value < 10:
            window.blit(text, (100 * (i % size) + 35, 100 * (i // size) + 30))
        else:
            window.blit(text, (100 * (i % size) + 20, 100 * (i // size) + 30))
    

def draw_grid(window, size):
    for n in range(1, size):
        pygame.draw.line(window, (0, 0, 0), (100 * n, 0), (100 * n, 100 * size), 3)
        pygame.draw.line(window, (0, 0, 0), (0, 100 * n), (100 * size, 100 * n), 3)

def draw_solution(path, size):
    pygame.init()
    win_size = 100 * size
    window = pygame.display.set_mode((win_size, win_size))
    pygame.display.set_caption(f"{size}x{size} Puzzle")

    for grid in path:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        window.fill((255, 255, 255))
        draw_grid(window, size)
        draw_tiles(window, grid, size)
        pygame.display.flip()
        sleep(0.25)

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
