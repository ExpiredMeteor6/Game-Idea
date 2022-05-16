import pygame
from terrain_handler import Chunk
class Render:
    def __init__(self):
        self.TEST_MAP = []
        self.LEVEL_MAP_NUMBERS = [[[[0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0]],

                                    [[1, 1, 1, 1, 1, 1, 1, 1], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2]],

                                    [[2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2]],

                                    [[2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2], 
                                    [2, 2, 2, 2, 2, 2, 2, 2]]],

                                    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                                    [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]]],

                                    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                                    [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]]],

                                    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                                    [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]]],

                                    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                                    [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]]],

                                    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                                    [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]]],

                                    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                                    [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]]],

                                    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                                    [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]],
                                    [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2]]]
                                    ]

        self.LEVEL_MAP = []

        self.BLOCK_SIZE = 32
        self.MAP_DIMENSIONS = (8, 4)

        self.WINDOW_WIDTH = 2048
        self.WINDOW_HEIGHT = 1024

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.load_and_scale_imgs()

        self.offset_y = 0
        self.offset_x = 0 

        self.zoom_ins = 0
        self.zoom_outs = 0

        self.ZOOM_IN_LIMIT = 1
        self.ZOOM_OUT_LIMIT = 1

        self.movement_horizontal = 0
        self.movement_vertical = 0
    
    def load_and_scale_imgs(self):
        self.grass_img = pygame.image.load('Images/grass.png')
        self.air_img = pygame.image.load('Images/air.png')
        self.dirt_img = pygame.image.load('Images/dirt.png')
        self.stone_img = pygame.image.load('Images/stone.png')
        self.gravel_img = pygame.image.load('Images/gravel.png')
        self.iron_ore_img = pygame.image.load('Images/iron_ore.png')

        scale_texture = lambda x: pygame.transform.scale(x, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.grass_img = scale_texture(self.grass_img)
        self.air_img = scale_texture(self.air_img)
        self.dirt_img = scale_texture(self.dirt_img)
        self.stone_img = scale_texture(self.stone_img)
        self.gravel_img = scale_texture(self.gravel_img)
        self.iron_ore_img = scale_texture(self.iron_ore_img)

    def place_rotated_block(self, block, y, x):
        random_num = Chunk().block_rotation(y, x)
        block_rotated_img = pygame.transform.rotate(block, random_num * 90)
        return block_rotated_img
    
    def level_row(self):
        y = 0
        x = len(self.LEVEL_MAP) // 4

        for i in range(4):
            current_chunk = Chunk()
            #print(self.LEVEL_MAP_NUMBERS[x][y])
            current_chunk.convert_map_to_chunks(x, y, self.LEVEL_MAP_NUMBERS)
            self.LEVEL_MAP.append(current_chunk)
            y += 1
    
    def add_level_row(self):
        x = len(self.LEVEL_MAP) // 4
        y = len(self.LEVEL_MAP) % x

        air_chunk = Chunk()
        air_chunk.CHUNK = [[0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0]]

        air_chunk.x_y = (x, y)
        self.LEVEL_MAP.append(air_chunk)
        
        grass_chunk = Chunk()
        grass_chunk.CHUNK = [[1, 1, 1, 1, 1, 1, 1, 1], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2]]
        grass_chunk.x_y = (x, y+1)                    
        self.LEVEL_MAP.append(grass_chunk)

        dirt_chunk = Chunk()
        dirt_chunk.CHUNK = [[2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2]]

        dirt_chunk.x_y = (x, y+2)                    
        self.LEVEL_MAP.append(dirt_chunk)

        dirt_chunk2 = Chunk()
        dirt_chunk2.CHUNK = [[2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2], 
                            [2, 2, 2, 2, 2, 2, 2, 2]]

        dirt_chunk2.x_y = (x, y+3)                    
        self.LEVEL_MAP.append(dirt_chunk2)
    
    def remove_level_row(self):
        self.LEVEL_MAP = self.LEVEL_MAP[:-4]

    def draw_level(self):
        for chunk in self.LEVEL_MAP:
            y = 0
            for row in chunk.CHUNK:
                x = 0
                for block in row:
                    placex = (x + self.movement_horizontal + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE
                    placey = (y + self.movement_vertical + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE

                    placex += self.offset_x
                    placey += self.offset_y

                    place_img = lambda i : self.screen.blit(i, (placex, placey))
                    place_rotated_img = lambda i : place_img(self.place_rotated_block(i, y, x))

                    if block == 0:
                        place_img(self.air_img)

                    elif block == 1:
                        place_img(self.grass_img)

                    elif block == 2:
                        place_rotated_img(self.dirt_img)
                    
                    elif block == 3:
                        place_rotated_img(self.stone_img)
                    
                    elif block == 4:
                        place_rotated_img(self.iron_ore_img)
                    
                    x += 1
                y += 1
    
    def convert_level_map_to_list(self):
        level_in_save_format = []

        for chunk in self.LEVEL_MAP:
            y = 0
            temp_chunk = []
            for row in chunk.CHUNK:
                temp_row = []
                x = 0
                for block in row:
                    temp_row.append(block)
                    x += 1
                
                temp_chunk.append(temp_row)
                y += 1
            level_in_save_format.append(temp_chunk)
        
        return level_in_save_format
    
    def convert_map_list_to_level(self, maplst):
        self.LEVEL_MAP = []
        x = 0
        y = 0
        
        for i in range(len(maplst)):
            if i % 4 == 0 and i != 0:
                x += 1
                y = 0
            current_chunk = Chunk()
            current_chunk.CHUNK = maplst[i]
            current_chunk.x_y = (x, y)
            self.LEVEL_MAP.append(current_chunk)
            y += 1

    def wipe(self):
        self.screen.fill((0,0,0))
    
    def adjust_zoom_offsets(self):
        self.offset_x = (self.WINDOW_WIDTH - self.BLOCK_SIZE * self.MAP_DIMENSIONS[0] * 8) / 2
        self.offset_y = (self.WINDOW_HEIGHT - self.BLOCK_SIZE * self.MAP_DIMENSIONS[1] * 8) / 2

    def zoom(self, in_or_out):
        if in_or_out == 'in':
            if self.zoom_ins > self.ZOOM_IN_LIMIT:
                return

            self.BLOCK_SIZE = self.BLOCK_SIZE * 2

            self.adjust_zoom_offsets()

            self.load_and_scale_imgs()

            if self.zoom_outs > 0:
                self.zoom_outs -= 1
            else:
                self.zoom_ins += 1

        else:
            if self.zoom_outs > self.ZOOM_OUT_LIMIT:
                return

            self.BLOCK_SIZE = self.BLOCK_SIZE / 2
            
            self.adjust_zoom_offsets()

            self.load_and_scale_imgs()

            if self.zoom_ins > 0:
                self.zoom_ins -= 1
            else:
                self.zoom_outs += 1



    