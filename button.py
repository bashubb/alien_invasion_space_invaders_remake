import pygame.font

class Button():

    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        #define dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #create button's rectangle and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #msg visible on the button need to be prepared only once
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Put msg in the center of the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """display empty button, then put msg on it"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)