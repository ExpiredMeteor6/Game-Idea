import pygame
import random
from terrain_handler import Chunk 
from animation import Idle
import sys
from render import Render
import time
import math
from entities import Entity, Player, Enemy
from button import Button
from pathfinding import PathFinder

pygame.init()
clock = pygame.time.Clock()
FRAME_RATE = 144

pygame.display.set_caption('Terrain Test')


render = Render()


for i in range(len(render.LEVEL_MAP_NUMBERS)):
    render.level_row()

render.convert_map_list_to_level(render.file.load())
mode = "Level"

def ray_march(current_position, direction):
    pixels_traveled = 0
    max_pixels = 16
    while (get_block(current_position) == 0 or get_block(current_position) == 5) and pixels_traveled <= max_pixels:
        pixels_traveled += 1
        current_position[0] += direction[0]
        current_position[1] += direction[1]
    return pixels_traveled

def get_player_location():
    return game_entities[0].get_world_position()

def get_entity_location(position_in_list):
    return game_entities[position_in_list].position

def get_block(current_position):
    current_block_size = render.BLOCK_SIZE

    horizontal_offset = (render.movement_horizontal * current_block_size)
    vertical_offset = (render.movement_vertical * current_block_size)

    actual_x_pos = math.floor((current_position[0] - horizontal_offset) / current_block_size)
    actual_y_pos = math.floor((current_position[1] - vertical_offset) / current_block_size)

    chunk_coords = (math.floor(actual_x_pos / 8), math.floor(actual_y_pos / 8))
    block_within_chunk_coords = (int((actual_x_pos / 8 - chunk_coords[0]) * 8), int((actual_y_pos / 8 - chunk_coords[1]) * 8))

    block = render.LEVEL_MAP[chunk_coords[0] * 4 + chunk_coords[1]].CHUNK[block_within_chunk_coords[1]][block_within_chunk_coords[0]]
    return block

def get_block_coords(position):
    current_block_size = render.BLOCK_SIZE

    horizontal_offset = (render.movement_horizontal * current_block_size)
    vertical_offset = (render.movement_vertical * current_block_size)

    actual_x_pos = math.floor((position[0] - horizontal_offset) / current_block_size)
    actual_y_pos = math.floor((position[1] - vertical_offset) / current_block_size)

    chunk_coords = (math.floor(actual_x_pos / 8), math.floor(actual_y_pos / 8))
    block_within_chunk_coords = (int((actual_x_pos / 8 - chunk_coords[0]) * 8), int((actual_y_pos / 8 - chunk_coords[1]) * 8))
    return chunk_coords, block_within_chunk_coords


def Start_Screen():
    displayed = True
    render.screen.blit(render.BG, (0,0))

    render.music.load('Audio/Time.mp3')
    '''render.music.play(-1)'''

    start_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Start", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2))

    while displayed:
        start_button.change_button_colour(pygame.mouse.get_pos())
        start_button.button_update()
    


        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                displayed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_clicked(pygame.mouse.get_pos()) == True:
                    displayed = False

        
        pygame.display.update()
        clock.tick(FRAME_RATE)
        



Start_Screen()

game_entities = []
game_entities.append(Player(1024, 100, render, ray_march, get_player_location, get_block_coords, get_entity_location))
game_entities.append(Enemy(984, 100, render, ray_march, get_player_location, get_block_coords, get_entity_location))
#game_entities.append(Enemy(960, 100, render, ray_march, get_player_location))
#game_entities.append(Enemy(940, 100, render, ray_march, get_player_location))
#game_entities.append(Enemy(920, 100, render, ray_march, get_player_location))
#game_entities.append(Enemy(900, 100, render, ray_march, get_player_location))

def Game_Screen():
    render.find_start()
    running = True

    render.music.load('Audio/Timeless.mp3')
    '''render.music.play(-1)'''

    count = 0
    while running:
        if count == 0:
            render.draw_level()
            render.movement_horizontal += render.start_coords[1] * 32
            render.draw_level()
            
        count += 1
        
        #RESET sky every frame
        #render.redraw_sky()
        render.wipe()
        render.draw_level()

        for entity in game_entities:
            texture = entity.get_texture()
            position = entity.position

            if entity == game_entities[0]: 
                render.screen.blit(texture, position)
            else:
                '''print((entity.position[0] + render.movement_horizontal * render.BLOCK_SIZE, entity.position[1] + render.movement_vertical * render.BLOCK_SIZE))'''
                render.screen.blit(texture, (entity.position[0] + render.movement_horizontal * render.BLOCK_SIZE, entity.position[1] + render.movement_vertical * render.BLOCK_SIZE))
            
        for entity in game_entities:
            entity.tick()
            

        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                for entity in game_entities:
                    entity.on_key_press(event.key)

            if event.type == pygame.KEYUP:
                for entity in game_entities:
                    entity.on_key_release(event.key)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                
        
        pygame.display.update()
        clock.tick(FRAME_RATE)
        #print(clock.get_fps())

Game_Screen()