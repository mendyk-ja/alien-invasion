import pygame.font


class Button:

    def __init__(self, ai_game, msg):
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
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Putting message in generated image and  center it on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Displaying an empty button and then message on it"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
