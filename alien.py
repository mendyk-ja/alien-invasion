import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class presenting one alien from fleet"""

    def __init__(self, ai_game):
        """Alien initialization and defining it's initial location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading the alien image and defining it's 'rect' attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Placement of a new alien near  upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storage of accurate horizontal alien location
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True value, if alien is located on the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Mowing alien to the right or to the left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
