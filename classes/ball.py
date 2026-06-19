import pygame

class Ball:
    """A Class that defines how the ball will look and behave"""
    def __init__(self, screen, main_settings):
        """Define general characteristics"""
        self.main_settings = main_settings
        self.screen        = screen
        self.width = self.height = 20
        self.x             = main_settings.screen_width / 2 - self.width / 2
        self.y             = main_settings.screen_height / 2 - self.height / 2
        self.color         = main_settings.items_color
        self.rect          = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel_x         = main_settings.ball_initial_vel_x
        self.vel_y         = main_settings.ball_initial_vel_y
        self.pause_timer   = main_settings.initial_countdown
        self.collision_counter = 0
        self.gradual_acc   = main_settings.acceleration_duration

    def blitme(self):
        """Draw the ball at its current location"""
        pygame.draw.rect(self.screen, self.color, self.rect)
