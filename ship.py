import pygame


class Ship():
    """Class intended for managing spaceship."""
    def __init__(self, ai_game):
        """Initialization of spaceship and his primary position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the spaceship image and and getting his position
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new spaceship show up on the bottom of the screen.
        self.rect.midbottom = self. screen_rect.midbottom

        # Option indicating on spaceship moving.
        self.moving_right = False

    def update(self):
        """Actualization of spaceship location based on option indicating on it's moving"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Displaying spaceship in his actual position"""
        self.screen.blit(self.image, self.rect)