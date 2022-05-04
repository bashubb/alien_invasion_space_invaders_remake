import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """The class describes single alien in the group"""
    def __init__(self, ai_game):
        """Initialization of alien and defined its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #loading alien's imaage
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # placement new alien near top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # alien's specific position storage
        self.x = float(self.rect.x)


    def check_edges(self):
        """Returns True if an alien is near the screen's edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """move the alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

