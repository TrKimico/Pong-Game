import pygame

class Racket:
    """A Class that defines how rackets will look and behave"""
    def __init__(self, screen, main_settings, x: int, y: int, input_up, input_down):
        """initialize the class"""
        # define general characteristics
        self.screen        = screen
        self.main_settings = main_settings
        self.width         = 30
        self.height        = 110
        self.color         = main_settings.items_color
        self.rect          = pygame.Rect(x, y, self.width, self.height)
        self.rect.centerx  = x  # treat x as center instead of left edge
        self.rect.centery  = y # treat y as center instead of left edge
        self.vel           = main_settings.racket_initial_velocity
        # store inputs for each object
        self.input_up      = input_up
        self.input_down    = input_down
        # handle reaction to user inputs
        self.moving_up     = False
        self.moving_down   = False

    def blitme(self):
        """Draw the racket at its current location"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update_racket(self, main_settings):
        """Handles the movements of the racket"""
        # stay still if both keys are pressed at the same time
        if self.moving_up and self.moving_down:
            return
        elif self.moving_up and self.rect.y > 0:
            self.rect.y -= self.vel
        elif self.moving_down and self.rect.y < main_settings.screen_height - self.height:
            self.rect.y += self.vel
    
    def update_ai_racket(self, main_settings, ball):
        """Controls the movement patterns of the ai opponent"""
        if main_settings.difficulty_mode == "hard" and ball.pause_timer > 0: # avoids stutter at the start of the rounds
            return
        else:
            self.ball = ball
            if ball.rect.centerx <= main_settings.ai_perception: # first difficulty leverage
                # avoids stutter because of minimal movements
                if ball.rect.y - main_settings.ai_dead_zone < self.rect.centery < ball.rect.y + main_settings.ai_dead_zone: 
                    return
                elif self.rect.centery < ball.rect.y and self.rect.y < main_settings.screen_height - self.height:
                    self.rect.centery += self.vel
                # not "else" because it stays still if self.rect.centery == ball.rect.y
                elif self.rect.centery > ball.rect.y and self.rect.y > 0:
                    self.rect.centery -= self.vel
            else:
                if ball.rect.y - main_settings.ai_dead_zone < self.rect.centery < ball.rect.y + main_settings.ai_dead_zone:
                    return
                elif self.rect.centery < ball.rect.y and self.rect.y < main_settings.screen_height - self.height:
                    self.rect.centery += self.vel * main_settings.ai_slowdown # second difficulty leverage
                # not "else" because it stays still if self.rect.centery == ball.rect.y
                elif self.rect.centery > ball.rect.y and self.rect.y > 0:
                    self.rect.centery -= self.vel * main_settings.ai_slowdown # second difficulty leverage