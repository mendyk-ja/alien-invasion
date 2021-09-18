import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Main class intended for managing resources and the way of working of the game."""

    def __init__(self):
        """Game initialization and creating their resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Starting main loop of the game"""
        while True:
            # Waiting for pressing the key or mouse button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

            # Refreshing the screen during every loop iteration.
            self.screen.fill(self.settings.bg_color)

            # Displaying recently modified screen
            pygame.display.flip()


if __name__ == '__main__':
    #  Creating game object and starting it
    ai = AlienInvasion()
    ai.run_game()
