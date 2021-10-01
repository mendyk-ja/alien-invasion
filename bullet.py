import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing bullets delivered by spaceship"""

    def __init__(self, ai_game):
        """Creating bullet object in actual spaceship's location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creating a bullet square in  (0, 0) location and then
        # Defining the right location for it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet location is defined by float value
        self.y = float(self.rect.y)

    def update(self):
        """Moving bullet on the screen"""
        # Actualization of bullet location
        self.y -= self.settings.bullet_speed
        # Location actualization of bullet square
        self.rect.y = self.y

    def draw_bullet(self):
        """ Displaying bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

