import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """The Class manages spaceship"""

    def __init__(self,ai_game):
        """Initialization of the spaceship and its start position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load spaceship image  and save its position
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #every new spaceship appears at the botton of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

        # ship's postion is stored in float
        self.x = float(self.rect.x)

        # describes ship's moving
        self.moving_left = False
        self.moving_right = False


    def blitme(self):
        """displays actual spaceship's position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update spaceship's position based on an option that idicates its movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed

        #update rect object based on self.x value
        self.rect.x = self.x


    def center_ship(self):
        """Put new spaceship in the middle of the screen, near its bottom edge"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


