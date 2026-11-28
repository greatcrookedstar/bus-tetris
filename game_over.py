import pygame

WIDTH = 500
HEIGHT = 600

PINK = (247, 220, 235)
PURPLE = (140, 90, 170)
WHITE = (255, 255, 255)

def show_game_over(screen, score):
    title_font = pygame.font.SysFont("arial", 48)
    text_font = pygame.font.SysFont("arial", 30)

    restart_button = pygame.Rect(125, 360, 250, 60)
    menu_button = pygame.Rect(125, 440, 250, 60)

    clock = pygame.time.Clock()

    while True:
        screen.fill(PINK)

        title = title_font.render("GAME OVER!", True, PURPLE)
        screen.blit(title, title.get_rect(center=(250, 140)))

        score_text = text_font.render(
            f"Score: {score}", True, PURPLE
        )
        screen.blit(
            score_text,
            score_text.get_rect(center=(250, 250))
        )

        pygame.draw.rect(
            screen, PURPLE, restart_button, border_radius=15
        )
        pygame.draw.rect(
            screen, PURPLE, menu_button, border_radius=15
        )

        restart_text = text_font.render("RESTART", True, WHITE)
        menu_text = text_font.render("MENU", True, WHITE)

        screen.blit(
            restart_text,
            restart_text.get_rect(center=restart_button.center)
        )
        screen.blit(
            menu_text,
            menu_text.get_rect(center=menu_button.center)
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"

                if menu_button.collidepoint(event.pos):
                    return "menu"

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bus Tetris - Game Over")

    result = show_game_over(screen, 350)
    print("Selected:", result)

    pygame.quit()