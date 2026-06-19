import pygame
import sys
import helper_functions as hf
from classes.menu_dataclasses import DisplayState

##########################################
# Pause FUNCTIONS
##########################################

def check_pause(events, sound_effects):
    """detects pause calls and triggers pause screen"""
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sound_effects.pause.play()
            return DisplayState.PAUSE
    return DisplayState.PLAY

def update_pause(events, main_settings, sound_effects, pause_items):
    """controls the behavior of the menu buttons and text"""
    pygame.mixer.music.pause()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif pause_items.text_continue.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            hf.menu_choice(
                sound_effects, SELECTED_TEXT=pause_items.text_gomenu, SELECTED_BUTTON=pause_items.button_gomenu,
                UNSELECTED_TEXT=pause_items.text_continue, UNSELECTED_BUTTON=pause_items.button_continue)
        elif pause_items.text_gomenu.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            hf.menu_choice(
                sound_effects, SELECTED_TEXT=pause_items.text_continue, SELECTED_BUTTON=pause_items.button_continue,
                UNSELECTED_TEXT=pause_items.text_gomenu, UNSELECTED_BUTTON=pause_items.button_gomenu)
        elif pause_items.text_continue.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # playback music
            sound_effects.unpause.play()
            pygame.mixer.music.unpause()
            return DisplayState.PLAY
        elif pause_items.text_gomenu.selected == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_effects.decline.play()
            main_settings.acceleration_duration = 0 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return DisplayState.END_GAME
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # playback music
            sound_effects.unpause.play()
            pygame.mixer.music.unpause()
            # revert back to default colors
            pause_items.text_gomenu.color = pause_items.button_continue.color = main_settings.items_color
            pause_items.text_continue.color = pause_items.button_gomenu.color = main_settings.bg_color
            # ensure correct vairable values
            pause_items.text_continue.selected = True
            pause_items.text_gomenu.selected = False
            return DisplayState.PLAY
    return DisplayState.PAUSE

def update_pause_screen(screen, main_settings, pause_items, controls_message, controls_message_esc):
    """Make the most recently drawn screen visible"""
    screen.fill(main_settings.menu_bg_color)
    hf.blit_all(*vars(pause_items).values(),controls_message, controls_message_esc)
    pygame.display.flip()