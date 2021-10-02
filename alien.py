import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class presenting one alien from fleet"""

    def __init__(self, ai_game):
        """Alien initialization and defining it's initial location"""
        super().__init__()
        self.screen = ai_game.screen

        # Loading the alien image and defining it's 'rect' attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Placement of a new alien near  upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storage of accurate horizontal alien location
        self.x = float(self.rect.x)
