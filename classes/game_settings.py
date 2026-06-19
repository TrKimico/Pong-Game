import random

class Settings():
    """A Class to handle all the settings"""
    def __init__(self):
        """Initialize all the game's settings"""
        # screen settings
        self.screen_width  = 1200
        self.screen_height = 800
        self.margin        = 40
        # color settings
        self.bg_color      = (60, 60, 60)
        self.menu_bg_color = (10, 10, 10)
        self.items_color   = (200, 200, 180)
        self.highlight_color = (150, 200, 150)
        self.net_color     = (100, 100, 90)
        self.light_green   = (100, 200, 100)
        self.dark_green    = (50, 100, 50)
        self.light_orange  = (200, 170, 100)
        self.dark_orange   = (100, 85, 50)
        self.light_red     = (200, 100, 100)
        self.dark_red      = (100, 50, 50)
        # velocity settings
        self.lower_x_vel = self.upper_x_vel = self.lower_y_vel = self.upper_y_vel = self.max_y_vel = 0
        self.racket_initial_velocity = random.randint(self.lower_x_vel, self.upper_x_vel)
        self.ball_initial_vel_x      = random.choice([-1, 1]) * random.randint(self.lower_x_vel, self.upper_x_vel) 
        self.ball_initial_vel_y      = random.choice([-1, 1]) * random.randint(self.lower_y_vel, self.upper_y_vel)
        self.velocity_increment      = 1.2
        self.velocity_decrement      = 0.8
        self.acceleration_threshold  = 6
        self.initial_vel_slowdown    = None
        # system settings
        self.initial_countdown       = 200
        self.round_countdown         = 180
        self.acceleration_duration   = 0
        self.win_animation_countdown = 300
        self.ai_dead_zone            = 5 
        self.ai_perception = self.ai_slowdown = None
        self.difficulty_mode         = None
        self.max_win_score           = 10
        # font settings
        self.small_font  = 30
        self.medium_font = 45
        self.title_font  = 60
        self.big_font    = 80
        self.score_font  = 100
    
    def ai_settings(self):
        """defines the difficulty of the AI"""
        if self.difficulty_mode == "easy":
            # AI settings
            self.ai_perception = self.screen_width * 0.3
            self.ai_slowdown = 0.1
            # velocity settings
            self.initial_vel_slowdown = 0.2
            self.lower_x_vel = 6
            self.upper_x_vel = 9
            self.lower_y_vel = 1
            self.upper_y_vel = 2
            self.max_y_vel   = 4
        elif self.difficulty_mode == "medium":
            # AI settings
            self.ai_perception = self.screen_width * 0.5
            self.ai_slowdown   = 0.3
            # velocity settings
            self.initial_vel_slowdown = 0.3
            self.lower_x_vel = 10
            self.upper_x_vel = 13
            self.lower_y_vel = 2
            self.upper_y_vel = 3
            self.max_y_vel   = 6
        elif self.difficulty_mode == "hard":
            # AI settings
            self.ai_perception = self.screen_width * 0.7
            self.ai_slowdown   = 0.45
            # velocity settings
            self.initial_vel_slowdown = 0.3
            self.lower_x_vel = 14
            self.upper_x_vel = 16
            self.lower_y_vel = 3
            self.upper_y_vel = 4
            self.max_y_vel   = 6
        
    def set_velocity(self, coordinate):
        """calculates the velocity of all the objects at the start of each round"""
        if coordinate == "x_init":
            self.ball_initial_vel_x = random.choice([-1, 1]) * random.randint(self.lower_x_vel, self.upper_x_vel)
            self.racket_initial_velocity = abs(self.ball_initial_vel_x)
        elif coordinate == "x":
            self.ball_initial_vel_x = random.randint(self.lower_x_vel, self.upper_x_vel)
            self.racket_initial_velocity = abs(self.ball_initial_vel_x)
        elif coordinate == "y":
            self.ball_initial_vel_y = random.choice([-1, 1]) * random.randint(self.lower_y_vel, self.upper_y_vel)            
