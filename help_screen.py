import pygame


def show_bonus_help(screen):
    clock = pygame.time.Clock()
    
    title_font = pygame.font.SysFont(
        "arial", 28, bold=True
    )
    font = pygame.font.SysFont("arial", 20)
    
    while True:
        screen.fill((233, 223, 209))
        
        title = title_font.render(
            "CONTROLLER BONUS",
            True,
            (98, 81, 93)
        )
        screen.blit(title, (65, 65))
        
        lines = [
            "R - Remove 3 random passengers",
            "C - Choose one passenger",
            "",
            "Each use costs 1 bonus charge",
            "",
            "ESC - Back"
        ]
        
        for i, line in enumerate(lines):
            text = font.render(
                line,
                True,
                (98, 81, 93)
            )
            screen.blit(text, (65, 120 + i * 30))
            
        pygame.display.flip()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return