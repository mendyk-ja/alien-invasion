class Settings:
    """Class designated to storage all game settings"""

    def __init__(self):
        """Initialization game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,  230, 230)

        # Settings concerning spaceship.
        self.ship_limit = 3

        # Settings concerning bullet.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Settings concerning alien.
        self.fleet_drop_speed = 10

        # Easy change of game speed
        self.speedup_scale = 1.1

        # Easy change of scores gave for shooting down an alien.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing settings, which change during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #  Value fleet_direction amount to 1 means right and -1 means left.
        self.fleet_direction = 1

        # Scoring system
        self.alien_points = 50

    def increase_speed(self):
        """Changing speed and scoring system settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


