import sys

import pygame


class AlienInvasion:
    """Main class intended for managing resources and the way of working of the game."""

    def __init__(self):
        """Game initialization and creating their resources."""

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien invasion")

        # Defining background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting main loop of the game"""
        while True:
            # Waiting for pressing the key or mouse button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

            # Refreshing the screen during every loop iteration.
            self.screen.fill(self.bg_color)

            # Displaying recently modified screen
            pygame.display.flip()


if __name__ == '__main__':
    #  Creating game object and starting it
    ai = AlienInvasion()
    ai.run_game()
