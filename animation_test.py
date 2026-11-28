import pygame
import random
from graphics import load_images, draw_background, draw_person

pygame.init()

CELL = 100
ROWS = 5
COLS = 5

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bus Tetris - Animation Test")

background, people, controller = load_images()

SHAPES = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)]
]

clock = pygame.time.Clock()

def new_shape():
    shape = random.choice(SHAPES)
    width = max(x for x, y in shape) + 1
    x = (COLS - width) // 2
    ids = random.sample(range(len(people)), 4)
    return shape, x, -3.0, ids

shape, shape_x, shape_y, person_ids = new_shape()

running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    shape_y += dt * 1.2

    height = max(y for x, y in shape) + 1

    if shape_y + height >= ROWS:
        shape, shape_x, shape_y, person_ids = new_shape()

    screen.fill((255, 255, 255))
    draw_background(screen, background)

    for i, (dx, dy) in enumerate(shape):
        px = (shape_x + dx) * CELL
        py = (shape_y + dy) * CELL

        if py >= -CELL and py < ROWS * CELL:
            draw_person(screen, people, person_ids[i], px, py)

    pygame.display.flip()

pygame.quit()