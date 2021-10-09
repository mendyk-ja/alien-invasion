import pygame.font


class Scoreboard:
    """Class for  displaying information about scores"""

    def __init__(self, ai_game):
        """Initialization attributes concerning scores"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Settings of font for information about scores.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Preparing initial images with scores.
        self.prep_score()

    def prep_score(self):
        """Transformation scores to generated image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Displaying scores in the top right corner of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Displaying scores on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
