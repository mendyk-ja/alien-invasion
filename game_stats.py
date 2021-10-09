class GameStats:
    """Monitoring statistic data in 'Alien Invasion' game"""

    def __init__(self, ai_game):
        """Initialization of statistic data"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Starting game in  disabled mode
        self.game_active = False

    def reset_stats(self):
        """Initialization of statistic data, which can change during the game"""
        self.ships_left = self.settings.ship_limit
