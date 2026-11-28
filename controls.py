import pygame

def handle_controls(event, paused):
    if event.type != pygame.KEYDOWN:
        return None, paused

    if event.key == pygame.K_p:
        return None, not paused

    if paused:
        return None, paused

    if event.key == pygame.K_LEFT:
        return "left", paused

    if event.key == pygame.K_RIGHT:
        return "right", paused

    if event.key == pygame.K_DOWN:
        return "down", paused

    if event.key == pygame.K_UP:
        return "rotate", paused

    if event.key == pygame.K_SPACE:
        return "drop", paused

    return None, paused