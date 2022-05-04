import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    "The Class manages bullets which are fired by the spaceship"
    def __init__(self, ai_game):
        super(). __init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creating a bullet rectangle at a point (0,0)
        # and then defining the appropriate position for it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #position is defined by float value
        self.y = float(self.rect.y)


    def update(self):
        """The bullet's movment on the screen"""
        #update bullet's position
        self.y -= self.settings.bullet_speed
        #update a bullet rectangle's position
        self.rect.y = self.y

    def draw_bullet(self):
        """Display bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

