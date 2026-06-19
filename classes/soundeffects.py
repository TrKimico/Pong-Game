import pygame

class SoundEffects:
    """A Class that defines sound effects and their behavior"""
    def __init__(self):
        """defines the core aspects of the class"""
        # used in main game
        self.bounce    = pygame.mixer.Sound("assets/sound-effects/bounce.wav")
        self.collide   = pygame.mixer.Sound("assets/sound-effects/collide.wav")
        self.countdown = pygame.mixer.Sound("assets/sound-effects/countdown.mp3")
        self.decline   = pygame.mixer.Sound("assets/sound-effects/decline.wav")
        self.move_up_and_down = pygame.mixer.Sound("assets/sound-effects/move_up_and_down.wav")
        self.pause     = pygame.mixer.Sound("assets/sound-effects/pause.wav")
        self.score     = pygame.mixer.Sound("assets/sound-effects/score.wav")
        self.unpause   = pygame.mixer.Sound("assets/sound-effects/unpause.wav")
        self.win       = pygame.mixer.Sound("assets/sound-effects/win.wav")
        self.game_over = pygame.mixer.Sound("assets/sound-effects/game_over.mp3")
        # used only in the menus
        self.confirm  = pygame.mixer.Sound("assets/sound-effects/confirm.wav")
        self.decrease = pygame.mixer.Sound("assets/sound-effects/decrease.wav")
        self.denied   = pygame.mixer.Sound("assets/sound-effects/denied.wav")
        self.increase = pygame.mixer.Sound("assets/sound-effects/increase.wav")

