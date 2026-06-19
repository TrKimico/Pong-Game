import pygame
import game_functions as gf
import menu_functions as mf
import pause_functions as pf
import helper_functions as hf
from classes.menu_dataclasses import HomeMenuItems, ScoreItems, DifficultyItems, TutorialItems, PauseItems, DisplayState
from classes.game_settings import Settings
from classes.soundeffects import SoundEffects
from classes.racket import Racket
from classes.ball import Ball
from classes.score import Score
from classes.start_menu import Text, Button, Information

def run_game(score_win, singleplayer, main_settings, sound_effects):
    """The main function that runs the game"""

    ##########################################
    # DEFINITIONS
    ##########################################

    # Initialize the main settings and the screen
    screen = pygame.display.set_mode((main_settings.screen_width, main_settings.screen_height))
    # Initialize the clock
    clock = pygame.time.Clock()
    # Initialize music
    hf.play_music("assets/sound-effects/game_music.wav")
    pygame.mixer.music.set_volume(0.15)
    # Initialize the racket
    racket_L = Racket(screen, main_settings, x=main_settings.margin, 
                      y=main_settings.screen_height/2, input_down=pygame.K_s, input_up=pygame.K_z)
    racket_R = Racket(screen, main_settings, x=main_settings.screen_width-main_settings.margin, 
                      y=main_settings.screen_height/2, input_down=pygame.K_DOWN, input_up=pygame.K_UP)
    # Initialize the ball
    ball = Ball(screen, main_settings)
    # Initialize the score
    score_L = Score(screen, main_settings, x=main_settings.margin*3, 
                    y=main_settings.screen_height/8, player_score=0)
    score_R = Score(screen, main_settings, 
                    x=main_settings.screen_width-main_settings.margin*3.9, 
                    y=main_settings.screen_height/8, player_score=0)
    # Initialize the net
    net = Button(screen, main_settings, y=15, width=4, height=30, color=main_settings.net_color)
    net_list = gf.create_net(main_settings)
    # Initialize the win animation text
    win_text = Information(
        screen, main_settings, font_size= main_settings.big_font, x=main_settings.screen_width/2, 
        y=main_settings.screen_height/2, text="waiting for winner", color=main_settings.highlight_color)
    # Initialize the pause elements + class
    button_continue = Button(
        screen, main_settings, y=300, width=300, height=120, color=main_settings.items_color)
    button_gomenu = Button(
        screen, main_settings, y=500, width=300, height=120, color=main_settings.bg_color)
    text_continue = Text(
        screen, main_settings, rect=button_continue.rect, text="CONTINUE", selected=True, color=main_settings.bg_color)
    text_gomenu = Text(
        screen, main_settings, rect=button_gomenu.rect, text="QUIT GAME", selected=False,color=main_settings.items_color)
    controls_message = Information(
        screen, main_settings, font_size=main_settings.small_font,x=main_settings.screen_width/2, y=760, 
        text="select with up and down arrow, confirm with spacebar", color=main_settings.items_color)
    controls_message_esc = Information(
        screen, main_settings, font_size=main_settings.small_font,x=main_settings.screen_width/2,
        y=700, text="Go back with escape,", color=main_settings.items_color)
    title_pause = Information(
        screen, main_settings, font_size= main_settings.title_font, x=main_settings.screen_width/2, 
        y=60, text="Pause Menu", color=main_settings.highlight_color)
    pause_items = PauseItems(
        title_pause=title_pause,
        button_continue=button_continue,
        button_gomenu=button_gomenu,
        text_continue=text_continue,
        text_gomenu=text_gomenu,
    )
    # Loop variables definition
    state = DisplayState.PLAY # menu state

    ##########################################
    # FUNCTION EXECUTION
    ##########################################

    # Start the main loop for the game
    while True:
        # Check for events
        events = pygame.event.get()
        if state == DisplayState.PLAY:
            # check input
            state = pf.check_pause(events, sound_effects)
            gf.check_input(racket_R, events)
            if  singleplayer:
                # Apply changes to the AI racket
                racket_L.update_ai_racket(main_settings, ball)
            else:
                # Check for racket keyboard inputs
                gf.check_input(racket_L, events)
                # Apply changes to the racket
                racket_L.update_racket(main_settings)
            # apply changes to the other racket
            racket_R.update_racket(main_settings)
            # Apply changes to the ball
            gf.update_ball(main_settings, sound_effects, ball, racket_L, racket_R)
            # Apply changes to the score
            win = gf.update_score(main_settings, ball, score_L, score_R, score_win)
            if win:
                gf.win_animation(screen, main_settings, sound_effects, score_L, score_R, score_win, win_text, singleplayer)
                return
            # Show changes on screen
            gf.update_game_screen(screen, main_settings, racket_L, racket_R, ball, score_L, score_R, net, net_list)
            clock.tick(60) # caps the execution at 60fps
        elif state == DisplayState.PAUSE:
            # update pause menu
            state = pf.update_pause(events, main_settings, sound_effects, pause_items)
            # show changes on screen
            pf.update_pause_screen(screen, main_settings, pause_items, controls_message, controls_message_esc)
        elif state == DisplayState.END_GAME:
            main_settings.difficulty_mode = None
            return

def start_menu(main_settings, sound_effects):
    """Organises the game menu screens"""

    ##########################################
    # DEFINITIONS
    ##########################################

    # system objects
    screen = pygame.display.set_mode((main_settings.screen_width, main_settings.screen_height))
    pygame.display.set_caption("Pong")
    # initialise music
    hf.play_music("assets/sound-effects/menu_music.wav")
    # Home menu objects
    title_home = Information(
        screen, main_settings, font_size= main_settings.title_font, x=main_settings.screen_width/2, y=60,
        text="Welcome to PONG!", color=main_settings.highlight_color)
    controls_message = Information(
        screen, main_settings, font_size=main_settings.small_font,x=main_settings.screen_width/2, y=760,
        text="select with up and down arrow, confirm with spacebar", 
        color=main_settings.items_color)
    controls_message_esc = Information(
        screen, main_settings, font_size=main_settings.small_font,x=main_settings.screen_width/2, y=700,
        text="Go back with escape,", color=main_settings.items_color)
    button_play = Button(screen, main_settings, y=250, width=500, height=120, color=main_settings.items_color)
    button_play_solo = Button(screen, main_settings, y=450, width=500, height=120, color=main_settings.bg_color)
    button_quit = Button(screen, main_settings, y=650, width=500, height=120, color=main_settings.bg_color)
    text_play = Text(
        screen, main_settings,rect=button_play.rect, text="PLAY MULTIPLAYER", selected=True, color=main_settings.bg_color)
    text_play_solo = Text(
        screen, main_settings,rect=button_play_solo.rect, text="PLAY SOLO", selected=False, color=main_settings.items_color)
    text_quit = Text(
        screen, main_settings, rect=button_quit.rect, text="QUIT", selected=False, color=main_settings.items_color)
    # Win Score menu objects
    score_win = Score(screen, main_settings, x=main_settings.screen_width/2, 
                      y=main_settings.screen_height/2, player_score=1)
    button_increase_score = Button(
        screen, main_settings, y=300, width=100, height=100, color=main_settings.bg_color)
    button_decrease_score = Button(
        screen, main_settings, y=550, width=100, height=100, color=main_settings.bg_color)
    text_increase_score = Text(
        screen, main_settings, rect=button_increase_score.rect, text="^", selected=False, color=main_settings.items_color)
    text_decrease_score = Text(
        screen, main_settings, rect=button_decrease_score.rect, text="v", selected=False, color=main_settings.items_color)
    title_score = Information(
        screen, main_settings, font_size= main_settings.title_font, x=main_settings.screen_width/2, y=60,
        text="Winning Points Needed", color=main_settings.highlight_color)
    # Difficulty Setting objects
    title_difficulty = Information(
        screen, main_settings, font_size= main_settings.title_font, x=main_settings.screen_width/2, y=60,
        text="Choose The Difficulty Level", color=main_settings.highlight_color)
    button_easy = Button(screen, main_settings, y=250, width=500, height=120, color=main_settings.light_green)
    button_medium = Button(screen, main_settings, y=400, width=500, height=120, color=main_settings.dark_orange)
    button_hard = Button(screen, main_settings, y=550, width=500, height=120, color=main_settings.dark_red)
    text_easy = Text(
        screen, main_settings, rect=button_easy.rect, text="easy", selected=True, color=main_settings.dark_green)
    text_medium = Text(
        screen, main_settings, rect=button_medium.rect, text="medium", selected=False, color=main_settings.light_orange)
    text_hard = Text(
        screen, main_settings, rect=button_hard.rect, text="hard", selected=False, color=main_settings.light_red)
    # Tutorial objects
    title_tutorial = Information(
        screen, main_settings, font_size= main_settings.title_font, x=main_settings.screen_width/2, y=60,
        text="Tutorial", color=main_settings.highlight_color)
    player_tutorial = Information(
        screen, main_settings, font_size= main_settings.medium_font, x=main_settings.screen_width/4, y=60,
        text="???????", color=main_settings.items_color)
    controls_tutorial = Information(
        screen, main_settings, font_size=main_settings.small_font, x=main_settings.screen_width/2, y=760,
        text="Start game with spacebar", color=main_settings.items_color)
    # Initiate dataclasses
    home_menu = HomeMenuItems(
        title_home=title_home,
        button_play=button_play,
        text_play=text_play,
        button_play_solo=button_play_solo,
        text_play_solo=text_play_solo,
        button_quit=button_quit,
        text_quit=text_quit,
    )
    score_items = ScoreItems(
        title_score=title_score,
        button_decrease_score=button_decrease_score,
        text_decrease_score=text_decrease_score,
        button_increase_score=button_increase_score,
        text_increase_score=text_increase_score,
    )
    difficulty_items = DifficultyItems(
        title_difficulty=title_difficulty,
        button_easy=button_easy,
        button_medium=button_medium,
        button_hard=button_hard,
        text_easy=text_easy,
        text_medium=text_medium,
        text_hard=text_hard,
    )
    tutorial_items = TutorialItems(
        title_tutorial=title_tutorial,
        player_tutorial=player_tutorial,
        controls_tutorial=controls_tutorial,
    )
    # Loop variables definition
    state = DisplayState.HOME # menu state
    singleplayer = False # triggered if solo play is choosen

    ##########################################
    # FUNCTION EXECUTION
    ##########################################

    while True:# handles both screens so that the player can go back to the main menu from the score menu
        # Check for events
        events = pygame.event.get()
        # Go into the correct menu depending on enum dataclas value
        if state == DisplayState.HOME:
            (state, singleplayer) = mf.update_menu(screen, events, main_settings,controls_message, home_menu, sound_effects)
        elif state == DisplayState.SET_SCORE:
            state = mf.define_score(events, main_settings, score_win, score_items, sound_effects)
            # separated to account for 
            mf.update_score_screen(screen, main_settings, score_win, score_items, controls_message, controls_message_esc)
        elif state == DisplayState.DIFFICULTY:
            state = mf.difficulty(events, screen, main_settings, difficulty_items, controls_message, sound_effects)
        elif state == DisplayState.TUTORIAL:
            state = mf.tutorial(events, screen, main_settings, tutorial_items, sound_effects, singleplayer)
        elif state == DisplayState.START_GAME:
            return score_win, singleplayer

##########################################
# PROGRAM EXECUTION
##########################################
if __name__ == "__main__":
    # initialize the game library module
    pygame.init()
    # initialize core classes
    main_settings = Settings()
    sound_effects = SoundEffects()
    # start the game logic
    while True:
        (score_win, singleplayer) = start_menu(main_settings, sound_effects)
        run_game(score_win, singleplayer, main_settings, sound_effects)