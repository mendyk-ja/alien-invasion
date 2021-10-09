import pygame.font

class Button():

    def __init__(self, ai_game, screen, msg):
        """Initialization of button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Defining button's dimension and features
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creating the button and centre it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message displayed by button need to be prepared only once.
        