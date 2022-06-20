import pygame
import random
from terrain_handler import Chunk 
from animation import Idle
import sys
from render import Render
import time
import math
from entities import Entity, Player

pygame.init()
clock = pygame.time.Clock()
FRAME_RATE = 144

pygame.display.set_caption('Terrain Test')

running = True
render = Render()
for i in range(8):
    render.generate_row()

for i in range(len(render.LEVEL_MAP_NUMBERS)):
    render.level_row()

render.convert_map_list_to_level(render.file.load())
mode = "Level"

def ray_march(current_position, direction):
    pixels_traveled = 0
    max_pixels = 16
    while get_block(current_position) == 0 and pixels_traveled <= max_pixels:
        print(get_block(current_position))
        pixels_traveled += 1
        current_position[0] += direction[0]
        current_position[1] += direction[1]
    return pixels_traveled

def get_block(current_position):
    print(current_position)
    current_block_size = render.BLOCK_SIZE

    horizontal_offset = (render.movement_horizontal * current_block_size)
    vertical_offset = (render.movement_vertical * current_block_size)

    actual_x_pos = math.floor((current_position[0] - horizontal_offset) / current_block_size)
    actual_y_pos = math.floor((current_position[1] - vertical_offset) / current_block_size)

    chunk_coords = (math.floor(actual_x_pos / 8), math.floor(actual_y_pos / 8))
    block_within_chunk_coords = (int((actual_x_pos / 8 - chunk_coords[0]) * 8), int((actual_y_pos / 8 - chunk_coords[1]) * 8))

    block = render.LEVEL_MAP[chunk_coords[0] * 4 + chunk_coords[1]].CHUNK[block_within_chunk_coords[1]][block_within_chunk_coords[0]]
    return block

game_entities = []
game_entities.append(Player(1024, 100, render, ray_march))

idle = Idle()
count = 0
while running:
    if count == 0:
        #render.drawmap()
        render.draw_level()
    count += 1
    
    #RESET sky every frame
    #render.redraw_sky()
    render.wipe()
    render.draw_level()

    for entity in game_entities:
        texture = entity.get_texture()
        position = entity.position

        render.screen.blit(texture, position)

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
