import pygame

def load_images():
    background = pygame.image.load("assets/bus_background.jpg")

    people = []
    for i in range(1, 14):
        image = pygame.image.load(f"assets/person_{i:02d}.jpg")
        people.append(image)

    controller = pygame.image.load("assets/controller.jpg")

    return background, people, controller

def draw_background(screen, background):
    background = pygame.transform.scale(background, (500, 500))
    screen.blit(background, (0, 0))

def draw_person(screen, people, number, x, y):
    image = pygame.transform.scale(people[number], (100, 100))
    screen.blit(image, (x, y))

def draw_controller(screen, controller, x, y):
    image = pygame.transform.scale(controller, (100, 100))
    screen.blit(image, (x, y))