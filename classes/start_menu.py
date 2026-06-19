import pygame
import pygame.freetype

class Text:
    """A Class that defines how text will look and behave"""
    def __init__(self, screen, main_settings, rect, text: str, selected, color):
        """initialize the class"""
        # define general characteristics
        self.screen        = screen
        self.main_settings = main_settings
        self.text          = text
        self.font          = pygame.freetype.Font("assets/fonts/pixelpurl.ttf", main_settings.title_font)
        self.selected      = selected
        self.color         = color
        # necessary because otherwise the txt position of reference 
        # is top left corner, not center
        text_rect = self.font.get_rect(self.text)
        self.x    = rect.centerx - text_rect.width / 2
        self.y    = rect.centery - text_rect.height / 2

    def blitme(self):
        """Draw the text on the screen"""
        self.font.render_to(self.screen, (self.x, self.y), self.text, self.color)

class Button:
    """A Class that defines how buttons will look and behave"""
    def __init__(self, screen, main_settings, y: int, width: int, height: int, color):
        """initialize the class"""
        # define general characteristics
        self.screen        = screen
        self.main_settings = main_settings
        self.width         = width
        self.height        = height
        self.color         = color
        self.x             = main_settings.screen_width / 2
        self.rect          = pygame.Rect(self.x, y, width, height)
        self.rect.centerx  = self.x  # treat x as center instead of left edge
        self.rect.centery  = y # treat y as center instead of left edge
    
    def blitme(self):
        """Draw the button on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Information:
    """A Class that defines how informative text will look and behave"""
    def __init__(self, screen, main_settings, font_size: int, x: int, y: int, text: str, color):
        """initialize the class"""
        # define general characteristics
        self.screen = screen
        self.main_settings = main_settings
        self.text   = text
        self.font   = pygame.freetype.Font("assets/fonts/pixelpurl.ttf", font_size)
        self.font_size = font_size
        self.color  = color
        self.x      = x
        self.y      = y

    def blitme(self):
        """Draw the text on the screen"""
        text_surface, text_rect = self.font.render(self.text, self.color)
        text_rect.center        = (self.x, self.y)
        self.screen.blit(text_surface, text_rect)
        #self.font.render_to(self.screen, (self.x, self.y), self.text, self.color)