class GameStats:
    """Monitoring statistic data in 'Alien Invasion' game"""

    def __init__(self, ai_game):
        """Initialization of statistic data"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Starting game in  disabled mode
        self.game_active = False

        # The best score shouldn't be erased.
        self.high_score = 0

    def reset_stats(self):
        """Initialization of statistic data, which can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score  = 0
        self.level = 1

