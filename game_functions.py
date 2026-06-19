import pygame
import sys
import random
import helper_functions as hf

##########################################
# SYSTEM FUNCTIONS
##########################################
 
def check_input(racket, events):
    """Watch for keyboard and mouse events"""
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, racket, racket.input_up, racket.input_down)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, racket, racket.input_up, racket.input_down)

def update_game_screen(screen, main_settings, racket_L, racket_R, ball, score_L, score_R, net, net_list):
    """Make the most recently drawn screen visible"""
    screen.fill(main_settings.bg_color)
    hf.blit_all(racket_L, racket_R)
    draw_net(screen, net, net_list)
    hf.blit_all(ball, score_L, score_R)
    pygame.display.flip()

##########################################
# RACKET FUNCTIONS
##########################################

def check_keydown_events(event, racket, input_up, input_down):
    """Check for key presses"""
    if event.key == input_down:
        racket.moving_down = True
    elif event.key == input_up:
        racket.moving_up = True

def check_keyup_events(event, racket, input_up, input_down):
    """Check for key releases"""
    if event.key == input_down:
        racket.moving_down = False
    elif event.key == input_up:
        racket.moving_up = False

##########################################
# BALL FUNCTIONS
##########################################

def update_ball(main_settings, sound_effects, ball, racket_L, racket_R):
    """Handles collisions between the ball and the rackets"""
    if ball.pause_timer > 0:
        ball.pause_timer -= 1
    else:
        if main_settings.acceleration_duration < 55:
            hf.initial_acceleration(ball, main_settings)
        collision_helper(main_settings,sound_effects, ball, racket_L, racket_R, racket=racket_L, direction=1, 
                         border=ball.rect.x > main_settings.margin)
        collision_helper(main_settings,sound_effects, ball, racket_L, racket_R, racket=racket_R, direction=-1, 
                         border=ball.rect.x < main_settings.screen_width - main_settings.margin)
        bounce(main_settings, sound_effects, ball, racket_L, racket_R)

def collision_helper(main_settings, sound_effects, ball, racket_L, racket_R, racket, direction, border):
    """refactored collision checking with rackets + anti-tunnelling"""
    if ((ball.rect.x + ball.vel_x + ball.width) * direction < (racket.rect.x + racket.width) * direction and (
        racket.rect.y < (ball.rect.y + ball.vel_y) < (racket.rect.y + racket.height)) and border) or (
        (pygame.Rect.colliderect(ball.rect, racket)) and border):
        collide(main_settings, sound_effects, ball, racket, direction, racket_L, racket_R)

def collide(main_settings, sound_effects, ball, racket, direction, racket_L, racket_R):
    """Handles the ball's collisions with the rackets"""
    sound_effects.collide.play()
    ball.vel_x = -ball.vel_x
    ball.collision_counter += 1
    if direction == 1:  # left racket
        ball.rect.x = int(racket.rect.centerx + racket.width/2)
        # apply an effect if the racket is moving to mimic a real one
        if ((ball.vel_y > 0 and racket_L.moving_down) or (ball.vel_y < 0 and racket_L.moving_up)) and (
            ball.vel_y < main_settings.max_y_vel):
            ball.vel_y *= main_settings.velocity_increment
            ball.vel_y = round (ball.vel_y, 3)
        elif (ball.vel_y > 0 and racket_L.moving_up) or (ball.vel_y < 0 and racket_L.moving_down):
            ball.vel_y *= main_settings.velocity_decrement
            ball.vel_y = round (ball.vel_y, 3)
        acceleration(main_settings, ball, racket_L, racket_R)
    else:  # right racket
        ball.rect.x = racket.rect.x - ball.width
        # apply an effect if the racket is moving to mimic a real one
        if (ball.vel_y > 0 and racket_R.moving_down) or (ball.vel_y < 0 and racket_R.moving_up):
            ball.vel_y *= main_settings.velocity_increment
            ball.vel_y = round (ball.vel_y, 3)
        elif (ball.vel_y > 0 and racket_R.moving_up) or (ball.vel_y < 0 and racket_R.moving_down):
            ball.vel_y *= main_settings.velocity_decrement
            ball.vel_y = round (ball.vel_y, 3)
        acceleration(main_settings, ball, racket_L, racket_R)

def bounce(main_settings, sound_effects, ball, racket_L, racket_R):
    """Handles the ball's collisions with the edges of the screen + general movement"""
    # move back to the center of the screen if someone scored
    if ball.rect.x <= 0 - ball.width or ball.rect.x >= main_settings.screen_width:
        sound_effects.score.play()
        ball.pause_timer = main_settings.round_countdown
        ball.collision_counter = 0
        main_settings.acceleration_duration = 0 
        main_settings.set_velocity("x")
        ball.vel_x = racket_L.vel = racket_R.vel = main_settings.ball_initial_vel_x
        main_settings.set_velocity("y")
        ball.vel_y = main_settings.ball_initial_vel_y
        if ball.rect.x <= 0:
            ball.vel_x = -ball.vel_x # otherwise it always goes in the same direction
        ball.rect.x = main_settings.screen_width / 2 - ball.width / 2
        ball.rect.y = random.randint(main_settings.margin, main_settings.screen_height - main_settings.margin)
    else:
        if ball.rect.y <= 0 or ball.rect.y + ball.height >= main_settings.screen_height:
            sound_effects.bounce.play()
            ball.vel_y = -ball.vel_y # bounce on the top or bottom edge of the screen
        ball.rect.y += ball.vel_y # actually moves the ball when there is no collision with rackets
        ball.rect.x += ball.vel_x # actually moves the ball when there is no collision with rackets

def acceleration(main_settings, ball, racket_L, racket_R):
    """Accelerates the ball / rackets gradually after some collisions"""
    if ball.collision_counter >= main_settings.acceleration_threshold:
        if ball.vel_x > 0:
            ball.vel_x += 1
            racket_L.vel += 1 # increases the speed of the rackets every other collision
            racket_R.vel += 1
        else:
            ball.vel_x -= 1
        if ball.collision_counter % 2 == 0: # increase the vertical speed every other collision
            if ball.vel_y > 0:
                ball.vel_y += 1
            else:
                ball.vel_y -= 1

##########################################
# SCORE FUNCTIONS
##########################################

def update_score(main_settings, ball, score_L, score_R, score_win):
    """Handles the updates of the score ingame"""
    if ball.rect.x <= 0 - ball.width:
        score_R.player_score += 1
        if score_R.player_score == score_win.player_score: 
            return True
    elif ball.rect.x >= main_settings.screen_width:
        score_L.player_score += 1
        if score_L.player_score == score_win.player_score:
            return True
    return False

def win_animation(screen, main_settings, sound_effects, score_L, score_R, score_win, win_text, singleplayer):
    """appears when a player wins"""
    main_settings.acceleration_duration = 0 
    L_wins = score_L.player_score == score_win.player_score
    R_wins = score_R.player_score == score_win.player_score

    WIN_TEXT = {
        (True,  False, False): "!!! Player_1 won !!!",
        (False, True,  False): "!!! Player_2 won !!!",
        (True,  False, True):  "Game Over",
        (False, True,  True):  "!!! You Won !!!",
    }

    sound = sound_effects.game_over if (L_wins and singleplayer) else sound_effects.win
    sound.play()
    win_text.text = WIN_TEXT[(L_wins, R_wins, singleplayer)]

    clock = pygame.time.Clock()
    for _ in range(main_settings.win_animation_countdown):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(main_settings.bg_color)
        win_text.blitme()
        pygame.display.flip()
        clock.tick(60)

##########################################
# NET FUNCTIONS
##########################################
def create_net(main_settings):
    """Creates a list of y-positions for net segments"""
    spacing = 70
    return list(range(0, main_settings.screen_height, spacing))

def draw_net(screen, net, net_list):
    """Displays net segments along the screen"""
    for y in net_list:
        pygame.draw.rect(screen, net.color, (net.rect.x, y, net.width, net.height))