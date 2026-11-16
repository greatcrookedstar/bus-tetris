import pygame

pygame.init()

WIDTH = 500
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bus Tetris")

background = pygame.image.load("assets/menu_background.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

PURPLE = (126, 75, 151)
LIGHT_PURPLE = (165, 112, 186)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("arial", 30, bold=True)

play_button = pygame.Rect(125, 330, 250, 60)
exit_button = pygame.Rect(125, 410, 250, 60)

clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()

    screen.blit(background, (0, 0))

    for button, label in [
        (play_button, "PLAY"),
        (exit_button, "EXIT")
    ]:
        color = LIGHT_PURPLE if button.collidepoint(mouse_pos) else PURPLE

        pygame.draw.rect(screen, color, button, border_radius=20)
        pygame.draw.rect(screen, WHITE, button, 3, border_radius=20)

        text = font.render(label, True, WHITE)
        screen.blit(
            text,
            text.get_rect(center=button.center)
        )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_button.collidepoint(event.pos):
                    print("Game started")

                if exit_button.collidepoint(event.pos):
                    running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()