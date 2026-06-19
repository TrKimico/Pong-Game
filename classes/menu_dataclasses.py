from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class HomeMenuItems:
    """the objects that are specific to the home menu"""
    title_home      : object
    button_play     : object
    text_play       : object
    button_play_solo: object
    text_play_solo  : object
    button_quit     : object
    text_quit       : object

@dataclass
class ScoreItems:
    """the objects that are specific to the score menu"""
    title_score          : object
    button_decrease_score: object
    text_decrease_score  : object
    button_increase_score: object
    text_increase_score  : object

@dataclass
class DifficultyItems:
    """the objects that are specific to the difficulty menu"""
    title_difficulty: object
    button_easy     : object
    button_medium   : object
    button_hard     : object
    text_easy       : object
    text_medium     : object
    text_hard       : object

@dataclass
class TutorialItems:
    """the objects that are specific to the tutorial menu"""
    title_tutorial   : object
    player_tutorial  : object
    controls_tutorial: object

@dataclass
class PauseItems:
    """the objects that are specific to the pause menu"""
    title_pause    : object
    button_continue: object
    button_gomenu  : object
    text_continue  : object
    text_gomenu    : object

class DisplayState(Enum):
    """state enum that vastly simplifies the menu selection"""
    # menu states
    HOME       = auto()
    SET_SCORE  = auto()
    DIFFICULTY = auto()
    TUTORIAL   = auto()
    START_GAME = auto()
    # in game states
    PLAY       = auto()
    PAUSE      = auto()
    END_GAME   = auto()