import pygame


class Ship:
    """Class intended for managing spaceship."""
    def __init__(self, ai_game):
        """Initialization of spaceship and his primary position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the spaceship image and and getting his position
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new spaceship show up on the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Spaceship position is stored as float.
        self.x = float(self.rect.x)

        # Option indicating on spaceship moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualization of spaceship's x location, not it's quarter."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualization of object rect based on self.x value.
        self.rect.x = self.x

    def blitme(self):
        """Displaying spaceship in his actual position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Putting the spaceship on the center to the bottom of the screen"""
        self.rect.midbottom = self.screen_rect .midbottom
        self.x = float(self.rect.x)
