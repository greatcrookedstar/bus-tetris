import pygame


class Notifications:
    def __init__(self):
        self.message = ""
        self.remaining = 0

    def show(self, message, duration=2500):
        self.message = message
        self.remaining = duration

    def update(self, dt):
        self.remaining = max(
            0, self.remaining - dt
        )

    def draw(self, screen):
        if self.remaining <= 0:
            return
        
        font = pygame.font.SysFont(
            "arial", 22, bold=True
        )
        
        panel = pygame.Rect(
            510, 390, 280, 65
        )
        
        pygame.draw.rect(
            screen,
            (150, 125, 136),
            panel,
            border_radius=15
        )
        
        text_surface = font.render(self.message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=panel.center)
        screen.blit(text_surface, text_rect)