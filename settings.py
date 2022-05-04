class Settings:
    """The Class which stores all settings of the game """

    def __init__(self):
        """Initialization the game settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # spaceship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # change speed of the game
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """initialization of settings, which going to change during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # 1 = right direction, -1 = left direction
        self.fleet_direction = 1
        # score
        self.alien_points = 50

    def increse_speed(self):
        """change speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)