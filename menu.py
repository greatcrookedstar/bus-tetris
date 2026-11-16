import pygame

pygame.init()

WIDTH = 500
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bus Tetris")

PINK = (245, 190, 215)
PURPLE = (140, 100, 170)
WHITE = (255, 255, 255)

title_font = pygame.font.SysFont("arial", 48)
button_font = pygame.font.SysFont("arial", 30)

play_button = pygame.Rect(150, 300, 200, 60)
exit_button = pygame.Rect(150, 390, 200, 60)

running = True

while running:
    screen.fill(PINK)

    title = title_font.render("BUS TETRIS", True, PURPLE)
    screen.blit(title, title.get_rect(center=(250, 150)))

    pygame.draw.rect(screen, PURPLE, play_button, border_radius=15)
    pygame.draw.rect(screen, PURPLE, exit_button, border_radius=15)

    play_text = button_font.render("PLAY", True, WHITE)
    exit_text = button_font.render("EXIT", True, WHITE)

    screen.blit(play_text, play_text.get_rect(center=play_button.center))
    screen.blit(exit_text, exit_text.get_rect(center=exit_button.center))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                print("Game started")

            if exit_button.collidepoint(event.pos):
                running = False

    pygame.display.update()

pygame.quit()