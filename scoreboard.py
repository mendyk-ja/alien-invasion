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
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Transformation scores to generated image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Displaying scores in the top right corner of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Conversion the best score in game to generated image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Displaying the best score in the top center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Displaying scores on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """Checking, if is there a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats. high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Conversion level number to generated image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Level number is displayed under actual score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
