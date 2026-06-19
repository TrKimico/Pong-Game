import pygame

##########################################
# HELPER FUNCTIONS
##########################################

def play_music(file_path):
    """loads and plays one music at a time"""
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)

def blit_all(*objects):
    """blits all called objects in order"""
    for object in objects:
        object.blitme()

def menu_choice(sound_effects, SELECTED_TEXT, SELECTED_BUTTON, UNSELECTED_TEXT, UNSELECTED_BUTTON):
    """automate the menu selection switching"""
    sound_effects.move_up_and_down.play()
    SELECTED_TEXT.selected = True
    UNSELECTED_TEXT.selected = False
    # Switch each color pair (text <-> button)
    SELECTED_TEXT.color, SELECTED_BUTTON.color = SELECTED_BUTTON.color, SELECTED_TEXT.color
    UNSELECTED_TEXT.color, UNSELECTED_BUTTON.color = UNSELECTED_BUTTON.color, UNSELECTED_TEXT.color

def choose_difficulty(main_settings, sound_effects, difficulty):
    """call methods to calculate difficulty settings"""
    sound_effects.confirm.play()
    main_settings.difficulty_mode = difficulty
    #setattr(main_settings, difficulty, True)
    main_settings.ai_settings()
    main_settings.set_velocity("x_init")
    main_settings.set_velocity("y")

def initial_acceleration(ball, main_settings):
    main_settings.acceleration_duration +=1
    sign = 1 if ball.vel_x >= 0 else -1
    if main_settings.acceleration_duration < 50:
        ball.vel_x = sign * main_settings.initial_vel_slowdown * abs(main_settings.ball_initial_vel_x)
        ball.vel_y = main_settings.initial_vel_slowdown * main_settings.ball_initial_vel_y
    elif main_settings.acceleration_duration == 50:
        ball.vel_x = sign * abs(main_settings.ball_initial_vel_x)
        ball.vel_y = main_settings.ball_initial_vel_y