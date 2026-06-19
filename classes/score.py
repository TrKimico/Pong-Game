import pygame

class Score:
    """A Class that defines how text will look and behave"""
    def __init__(self, screen, main_settings, x: int, y: int, player_score: int):
        """initialize the class"""
        # define general characteristics
        self.screen        = screen
        self.main_settings = main_settings
        self.x             = x
        self.y             = y
        self.player_score  = player_score
        self.font          = pygame.freetype.Font("assets/fonts/pixelpurl.ttf", main_settings.score_font)

    def blitme(self):
        """Draw the text on the screen"""
        self.font.render_to(self.screen, (self.x, self.y), str(self.player_score), self.main_settings.items_color)
