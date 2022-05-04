class GameStats:
    """Monitoring of statistical data in the game 'alien invasion'"""
    def __init__(self, ai_game):
        """Initialization statistical data"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0


    def reset_stats(self):
        """Initialization statistical data, which could change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1