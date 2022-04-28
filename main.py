import pygame
import random
from terrain_handler import Chunk 
import sys

pygame.init()
clock = pygame.time.Clock()
WINDOW_WIDTH = 2048
WINDOW_HEIGHT = 1024
FRAME_RATE = 60
BLOCK_SIZE = 32

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

chunk_0_0 = Chunk()
chunk_0_0.generate_chunk(0, 0)
chunk_0_1 = Chunk()
chunk_0_1.generate_chunk(0, 1)
chunk_0_2 = Chunk()
chunk_0_2.generate_chunk(0, 2)

TEST_MAP = []

def generate_row():
    y = 0
    x = len(TEST_MAP) // 4
    for i in range(4):
        current_chunk = Chunk()
        current_chunk.generate_chunk(x, y)
        TEST_MAP.append(current_chunk)
        y += 1

generate_row()
generate_row()
generate_row()
generate_row()
generate_row()
generate_row()
generate_row()
generate_row()
generate_row()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Terrain Test')
grass_img = pygame.image.load('Images/grass.png')
air_img = pygame.image.load('Images/air.png')
dirt_img = pygame.image.load('Images/dirt.png')
player_img = pygame.image.load('Images/blob.png')

grass_img = pygame.transform.scale(grass_img, (BLOCK_SIZE, BLOCK_SIZE))
air_img = pygame.transform.scale(air_img, (BLOCK_SIZE, BLOCK_SIZE))
dirt_img = pygame.transform.scale(dirt_img, (BLOCK_SIZE, BLOCK_SIZE))
player_img = pygame.transform.scale(player_img, (BLOCK_SIZE, BLOCK_SIZE))

def drawmap():
    block_rects = []
    for chunk in TEST_MAP:
        y = 0
        for row in chunk.CHUNK:
            x = 0
            for block in row:
                if block == 0:
                    screen.blit(air_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * BLOCK_SIZE))

                elif block == 1:
                    screen.blit(grass_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * BLOCK_SIZE))

                elif block == 2:
                    random_num = random.randint(0, 3)
                    if random_num == 0:
                        dirt_rotated_img = dirt_img
                    else:
                        dirt_rotated_img = pygame.transform.rotate(dirt_img, random_num * 90)
                    screen.blit(dirt_rotated_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * BLOCK_SIZE))
                
                if block != 0:
                    block_rects.append(pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                
                x += 1
            y += 1

def redraw_sky():
    for chunk in TEST_MAP:
        y=0
        for row in chunk.CHUNK:
            x=0
            for block in row:
                if block == 0:
                    screen.blit(air_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * BLOCK_SIZE))
                else:
                    pass
                x +=1
            y += 1

running = True
drawmap()
MOVING_RIGHT = False
MOVING_LEFT = False
VERTICAL_MOMENTUM = 0
player_location = [50, 100]

while running:
    #RESET sky every frame
    redraw_sky()
    screen.blit(player_img, player_location)
    
   
    VERTICAL_MOMENTUM += 0.2
    player_location[1] += VERTICAL_MOMENTUM


    if MOVING_RIGHT == True:
        player_location[0] += 4 

    if MOVING_LEFT == True:
        player_location[0] -= 4

    for event in pygame.event.get():
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                MOVING_RIGHT = True
            if event.key == pygame.K_a:
                MOVING_LEFT = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                MOVING_RIGHT = False
            if event.key == pygame.K_a:
                MOVING_LEFT = False
         
    pygame.display.update()
    clock.tick(FRAME_RATE)



