import pygame
import random
from terrain_handler import Chunk 
from animation import Idle
import sys
from render import Render
import time
import math

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

for i in range(len(render.LEVEL_MAP_NUMBERS)):
    render.level_row()

MOVING_RIGHT = False
MOVING_LEFT = False
MOVING_UP = False

ALLOW_RIGHT = False
ALLOW_LEFT = False
ON_GROUND = False
VERTICAL_MOMENTUM = 4

#player_location = [1024, 100]
player_location = [50, 100]

def screen_to_block_coords(pos):
    current_block_size = render.BLOCK_SIZE
    #WHEN CAMERA MOVEMENT IMPLEMENTED USE THIS
    #horizontal_offset = (render.movement_horizontal * current_block_size) + render.offset_x
    #horizontal_offset = render.offset_x

    horizontal_offset = 0
    vertical_offset = 0

    actual_x_pos = math.floor((pos[0] - horizontal_offset) / current_block_size)
    actual_y_pos = math.floor((pos[1] - vertical_offset) / current_block_size)

    return (actual_x_pos, actual_y_pos)

def get_block(pos):
    current_block_size = render.BLOCK_SIZE
    #WHEN CAMERA MOVEMENT IMPLEMENTED USE THIS
    #horizontal_offset = (render.movement_horizontal * current_block_size) + render.offset_x
    #horizontal_offset = render.offset_x

    horizontal_offset = 0
    vertical_offset = 0

    actual_x_pos = math.floor((pos[0] - horizontal_offset) / current_block_size)
    actual_y_pos = math.floor((pos[1] - vertical_offset) / current_block_size)
    chunk_coords = (math.floor(actual_x_pos / 8), math.floor(actual_y_pos / 8))
    block_within_chunk_coords = (actual_x_pos - chunk_coords[0] * 8, actual_y_pos - chunk_coords[1] * 8)

    block = render.TEST_MAP[chunk_coords[0] * 4 + chunk_coords[1]].CHUNK[block_within_chunk_coords[1]][block_within_chunk_coords[0]]
    return block

def block_to_screen_coords(x, y):
    #screen_coords = ((x * render.BLOCK_SIZE) + render.offset_x, (y * render.BLOCK_SIZE) + render.offset_y)
    screen_coords = ((x * render.BLOCK_SIZE) + 0, (y * render.BLOCK_SIZE) + 0)
    return screen_coords


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

def allow_down(blob_x, blob_y, vertical_momentum):
    '''
    currentx,currenty = screen_to_block_coords(blob_screen_position_x, blob_screen_position_y)

    downblockx,downblocky = (current_x,currenty-1)
    downblockxscreen,downblockyscreen = block_to_screen_coords(downblockx, downblocky)

    vert_distance_to_down = downblockyscreen- blob_screen_position_y
    '''
    current_blob_position = screen_to_block_coords((blob_x, blob_y))
    block_beneath = (current_blob_position[0], current_blob_position[1] - 1)
    block_beneath_screen_coords = block_to_screen_coords(block_beneath[0], block_beneath[1])
    print(block_beneath_screen_coords)
    num_block_beneath = get_block(block_beneath_screen_coords)
    vertical_distance_to_down = current_blob_position[1] - block_beneath_screen_coords[1]

    #print(num_block_beneath)
    if vertical_distance_to_down < vertical_momentum and num_block_beneath != 0:
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
        #render.draw_level()
    count += 1

    if count % 30 == 0 and count_since_last_input > 432:
        if player_state == 0:
            player_state = 1
        else:
            player_state = 0
    
    #RESET sky every frame
    render.redraw_sky()
    #render.redraw_sky_level()
    
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

    '''
    if render.screen.get_at((int(player_location[0]), int(player_location[1])+32 + int(VERTICAL_MOMENTUM + 0.1))) != (140, 255, 251, 255) or render.screen.get_at((int(player_location[0]+26), int(player_location[1])+32 + int(VERTICAL_MOMENTUM + 0.1))) != (140, 255, 251, 255):
        VERTICAL_MOMENTUM = 0
        ON_GROUND = True
    else:
        ON_GROUND = False
        VERTICAL_MOMENTUM += 0.1
        player_location[1] += VERTICAL_MOMENTUM
    '''
    if allow_down(int(player_location[0]), int(player_location[1]) + render.BLOCK_SIZE * 2, VERTICAL_MOMENTUM) == True:
        #print("allowed down")
        ON_GROUND = False
        #VERTICAL_MOMENTUM += 0.1
        player_location[1] += VERTICAL_MOMENTUM
    else:
        #print("not allowed down")    
        VERTICAL_MOMENTUM = 4
        ON_GROUND = True

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
    #print(clock.get_fps())



