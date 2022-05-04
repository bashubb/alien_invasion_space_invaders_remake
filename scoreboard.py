import pygame.font
from pygame.sprite import Group


from ship import Ship



class Scoreboard():
    """The class which describes score information """

    def __init__(self,ai_game):
        """Initialization score atribiutes"""

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # settings for a font used for score information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # prepare image of score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_high_score(self):
        "conversion of the best score to the image"
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True , self.text_color, self.settings.bg_color)
        # display the best score on the top and center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.screen_rect.top = self.score_rect.top


    def prep_score(self):
        """transform score to the generated image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right = -20
        self.score_rect.top = 20

    def show_score(self):
        """display score on the screen"""
        self.score_image.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def check_high_score(self):
        """Check if actual score is the best"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """conversion level number to the image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        # level number is displayed under the actual score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Display number of spaceships left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 +ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
