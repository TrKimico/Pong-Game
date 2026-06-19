import pygame
import sys
import helper_functions as hf
from classes.menu_dataclasses import DisplayState

##########################################
# MENU FUNCTIONS
##########################################

def update_menu(screen, events, main_settings,controls_message, home_menu, sound_effects):
    """controls the behavior of the menu buttons and text"""
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif home_menu.text_play.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            hf.menu_choice(sound_effects, SELECTED_TEXT=home_menu.text_play_solo, SELECTED_BUTTON=home_menu.button_play_solo,
                           UNSELECTED_TEXT=home_menu.text_play, UNSELECTED_BUTTON=home_menu.button_play)
        elif home_menu.text_play_solo.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            hf.menu_choice(sound_effects, SELECTED_TEXT=home_menu.text_play,UNSELECTED_TEXT=home_menu.text_play_solo, 
                           SELECTED_BUTTON=home_menu.button_play, UNSELECTED_BUTTON=home_menu.button_play_solo)
        elif home_menu.text_play_solo.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            hf.menu_choice(sound_effects, SELECTED_TEXT=home_menu.text_quit, SELECTED_BUTTON=home_menu.button_quit, 
                           UNSELECTED_TEXT=home_menu.text_play_solo, UNSELECTED_BUTTON=home_menu.button_play_solo)
        elif home_menu.text_quit.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            hf.menu_choice(sound_effects, SELECTED_TEXT=home_menu.text_play_solo, SELECTED_BUTTON=home_menu.button_play_solo,
                           UNSELECTED_TEXT=home_menu.text_quit, UNSELECTED_BUTTON=home_menu.button_quit)
        elif home_menu.text_play.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_effects.confirm.play()
            return DisplayState.SET_SCORE, False
        elif home_menu.text_play_solo.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_effects.confirm.play()
            return DisplayState.SET_SCORE, True
        elif home_menu.text_quit.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_effects.decline.play()
            sys.exit()
    # show changes on screen
    screen.fill(main_settings.menu_bg_color)
    hf.blit_all(*vars(home_menu).values(), controls_message)
    pygame.display.flip()
    return DisplayState.HOME, False
        
##########################################
# SCORE FUNCTIONS
##########################################

def define_score(events, main_settings, score_win, score_items, sound_effects):
    """define the win score in the start menu"""
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif (main_settings.max_win_score >= score_win.player_score > 1) and (
            event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            sound_effects.decrease.play()
            score_win.player_score -= 1
            score_items.button_decrease_score.color = main_settings.items_color
            score_items.text_decrease_score.color = main_settings.bg_color
        elif (main_settings.max_win_score >= score_win.player_score > 1) and (
            event.type == pygame.KEYUP and event.key == pygame.K_DOWN):
            score_items.button_decrease_score.color = main_settings.bg_color
            score_items.text_decrease_score.color = main_settings.items_color
        elif (main_settings.max_win_score > score_win.player_score >= 1) and (
            event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            sound_effects.increase.play()
            score_win.player_score += 1
            score_items.button_increase_score.color = main_settings.items_color
            score_items.text_increase_score.color = main_settings.bg_color
        elif (main_settings.max_win_score > score_win.player_score >= 1) and (
            event.type == pygame.KEYUP and event.key == pygame.K_UP):
            score_items.button_increase_score.color = main_settings.bg_color
            score_items.text_increase_score.color = main_settings.items_color
        elif (
            score_win.player_score == main_settings.max_win_score and event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (
                score_win.player_score == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            sound_effects.denied.play()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_effects.confirm.play()
            return DisplayState.DIFFICULTY
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            score_win.player_score = 1
            sound_effects.decline.play()
            return DisplayState.HOME
    return DisplayState.SET_SCORE

def update_score_screen(screen, main_settings, score_win, score_items, controls_message_esc, controls_message):
    """update the elements on screen for the score start menu"""
    screen.fill(main_settings.menu_bg_color)
    score_win.blitme()
    if score_win.player_score != main_settings.max_win_score:
        hf.blit_all(score_items.button_increase_score, score_items.text_increase_score)
    else:
        score_items.button_increase_score.color = main_settings.bg_color # resets the color
        score_items.text_increase_score.color = main_settings.items_color
    if score_win.player_score != 1:
        hf.blit_all(score_items.button_decrease_score, score_items.text_decrease_score)
    else:
        score_items.button_decrease_score.color = main_settings.bg_color # resets the color
        score_items.text_decrease_score.color = main_settings.items_color
    hf.blit_all(controls_message, controls_message_esc, score_items.title_score)
    pygame.display.flip()

##########################################
# DIFFICULTY FUNCTIONS
##########################################

def difficulty(events, screen, main_settings, difficulty_items, controls_message, sound_effects):
    """menu to define the difficulty of the AI"""
    #events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        #elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
        #    proceed_tutorial = True
        elif difficulty_items.text_easy.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            hf.menu_choice(
                sound_effects, SELECTED_TEXT=difficulty_items.text_medium, SELECTED_BUTTON=difficulty_items.button_medium,
                UNSELECTED_TEXT=difficulty_items.text_easy, UNSELECTED_BUTTON=difficulty_items.button_easy)
        elif difficulty_items.text_medium.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            hf.menu_choice(
                sound_effects, SELECTED_TEXT=difficulty_items.text_easy, SELECTED_BUTTON=difficulty_items.button_easy, 
                UNSELECTED_TEXT=difficulty_items.text_medium, UNSELECTED_BUTTON=difficulty_items.button_medium)
        elif difficulty_items.text_medium.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            hf.menu_choice(
                sound_effects, SELECTED_TEXT=difficulty_items.text_hard, SELECTED_BUTTON=difficulty_items.button_hard, 
                UNSELECTED_TEXT=difficulty_items.text_medium, UNSELECTED_BUTTON=difficulty_items.button_medium)
        elif difficulty_items.text_hard.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            hf.menu_choice(
                sound_effects, SELECTED_TEXT=difficulty_items.text_medium, SELECTED_BUTTON=difficulty_items.button_medium, 
                UNSELECTED_TEXT=difficulty_items.text_hard, UNSELECTED_BUTTON=difficulty_items.button_hard)
        elif difficulty_items.text_easy.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hf.choose_difficulty(main_settings, sound_effects, "easy")
            return DisplayState.TUTORIAL
        elif difficulty_items.text_medium.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hf.choose_difficulty(main_settings, sound_effects, "medium")
            return DisplayState.TUTORIAL
        elif difficulty_items.text_hard.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hf.choose_difficulty(main_settings, sound_effects, "hard")
            return DisplayState.TUTORIAL
    # draw all the elements on screen
    screen.fill(main_settings.bg_color)
    hf.blit_all(*vars(difficulty_items).values(), controls_message)
    pygame.display.flip()
    return DisplayState.DIFFICULTY

##########################################
# TUTORIAL FUNCTIONS
##########################################

def tutorial(events, screen,main_settings, tutorial_items,sound_effects,singleplayer):
    """displays the tutorial screen"""
    PLAYER_INFO = {
        "single": [(main_settings.screen_width/2, ("Player", "go up: up arrow      ^", "go down: down arrow v"))],
        "multi":  [(main_settings.screen_width*1/4, ("Player_1", "go up:    z", "go down: s")),
                   (main_settings.screen_width*3/4, ("Player_2", "go up: up arrow      ^", "go down: down arrow v"))]
    }
    def draw_player_info(x, lines):
        initial_margin = main_settings.screen_height/6
        interline_margin = 80
        tutorial_items.player_tutorial.x, tutorial_items.player_tutorial.y = x, initial_margin
        for line in lines:
            tutorial_items.player_tutorial.y += interline_margin
            tutorial_items.player_tutorial.text = line
            tutorial_items.player_tutorial.blitme()

    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_effects.confirm.play()
            return DisplayState.START_GAME
    
    screen.fill(main_settings.bg_color)
    for x, lines in PLAYER_INFO["single" if singleplayer else "multi"]:
        draw_player_info(x, lines)
    hf.blit_all(tutorial_items.controls_tutorial, tutorial_items.title_tutorial)
    pygame.display.flip()
    return DisplayState.TUTORIAL