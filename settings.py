class Settings:
    """Class designated to storage all game settings"""

    def __init__(self):
        """Initialization game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,  230, 230)
        # Settings concerning spaceship.
        self.ship_speed = 1.5
        self.ship_limit    = 3
        # Settings concerning bullet.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        # Settings concerning alien.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Value fleet_direction amount to 1 means right and -1 means left.
        self.fleet_direction = 1
