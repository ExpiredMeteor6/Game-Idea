import pygame
import random
from terrain_handler import Chunk 
from animation import Idle
import sys
from render import Render
import time

pygame.init()
clock = pygame.time.Clock()
FRAME_RATE = 144

'''
TEST_MAP = [['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0', '0', '0', '0'],

            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '1', '1', '1', '1'], 
            ['1', '1', '1', '1', '2', '2', '2', '2'], 
            ['2', '2', '2', '2', '2', '2', '2', '2'], 
            ['2', '2', '2', '2', '2', '2', '2', '2'],

            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],

            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2'],
            ]
'''

pygame.display.set_caption('Terrain Test')

running = True
render = Render()
for i in range(8):
    render.generate_row()


MOVING_RIGHT = False
MOVING_LEFT = False
MOVING_UP = False

ALLOW_RIGHT = False
ALLOW_LEFT = False
ON_GROUND = False
VERTICAL_MOMENTUM = 0

player_location = [1024, 100]

def allow_right():
    if render.screen.get_at((int(player_location[0])+32, int(player_location[1])+30)) != (140, 255, 251, 255):
        return False
    else:
        return True


def allow_left():
    if render.screen.get_at((int(player_location[0])-2, int(player_location[1])+30)) != (140, 255, 251, 255):
        return False
    else:
        return True



last_direction = 'right'
idle = Idle()
player_state = 0
count = 0
count_since_last_input = 0
while running:
    if count == 0:
        render.drawmap()
    count += 1

    if count % 30 == 0 and count_since_last_input > 432:
        if player_state == 0:
            player_state = 1
        else:
            player_state = 0
    
    #RESET sky every frame
    render.redraw_sky()
    
    if last_direction == 'right':
        if player_state == 0:
            render.screen.blit(render.player_img_right, player_location)
        else:
            render.screen.blit(render.player_img_down_right, player_location)
    else:
        if player_state == 0:
            render.screen.blit(render.player_img_left, player_location)
        else:
            render.screen.blit(render.player_img_down_left, player_location)
    
    if render.screen.get_at((int(player_location[0]), int(player_location[1])+32 + int(VERTICAL_MOMENTUM + 0.1))) != (140, 255, 251, 255) or render.screen.get_at((int(player_location[0]+26), int(player_location[1])+32 + int(VERTICAL_MOMENTUM + 0.1))) != (140, 255, 251, 255):
        VERTICAL_MOMENTUM = 0
        ON_GROUND = True
    else:
        ON_GROUND = False
        VERTICAL_MOMENTUM += 0.1
        player_location[1] += VERTICAL_MOMENTUM
    
    
    if MOVING_RIGHT == True and allow_right() == True:
        player_location[0] += 4
        last_direction = 'right'

    if MOVING_LEFT == True and allow_left() == True:
        player_location[0] -= 4
        last_direction = 'left'

    if MOVING_UP == True and ON_GROUND == True:
        count = 0
        while count < 10:
            VERTICAL_MOMENTUM -= 0.4
            player_location[1] += VERTICAL_MOMENTUM
            count += 1
        MOVING_UP = False
    
    if MOVING_LEFT == False and MOVING_RIGHT == False and MOVING_UP == False:
        count_since_last_input += 1
    else:
        pass
    

    for event in pygame.event.get():
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #RIGHT
            if event.key == pygame.K_d:
                MOVING_RIGHT = True
            #LEFT
            if event.key == pygame.K_a:
                MOVING_LEFT = True
            #JUMP
            if event.key == pygame.K_SPACE:
                if ON_GROUND == False:
                    pass
                else:
                    MOVING_UP = True
            
            count_since_last_input = 0
            player_state = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                MOVING_RIGHT = False
            if event.key == pygame.K_a:
                MOVING_LEFT = False
    
    pygame.display.update()
    clock.tick(FRAME_RATE)
    print(clock.get_fps())



