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

        self.WINDOW_WIDTH = 2048
        self.WINDOW_HEIGHT = 1024

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        self.player_img_right = pygame.image.load('Images/blob_right.png')
        self.player_img_left = pygame.image.load('Images/blob_left.png')
        self.player_img_down_right = pygame.image.load('Images/blob_down_right.png')
        self.player_img_down_left = pygame.image.load('Images/blob_down_left.png')

        self.grass_img = pygame.image.load('Images/grass.png')
        self.air_img = pygame.image.load('Images/air.png')
        self.dirt_img = pygame.image.load('Images/dirt.png')
        self.stone_img = pygame.image.load('Images/stone.png')
        self.gravel_img = pygame.image.load('Images/gravel.png')
        self.iron_ore_img = pygame.image.load('Images/iron_ore.png')

        self.player_img_right = pygame.transform.scale(self.player_img_right, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.player_img_left = pygame.transform.scale(self.player_img_left, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.player_img_down_right = pygame.transform.scale(self.player_img_down_right, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.player_img_down_left = pygame.transform.scale(self.player_img_down_left, (self.BLOCK_SIZE, self.BLOCK_SIZE))

        self.grass_img = pygame.transform.scale(self.grass_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.air_img = pygame.transform.scale(self.air_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.dirt_img = pygame.transform.scale(self.dirt_img, (self.BLOCK_SIZE,self.BLOCK_SIZE))
        self.stone_img = pygame.transform.scale(self.stone_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.gravel_img = pygame.transform.scale(self.gravel_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.iron_ore_img = pygame.transform.scale(self.iron_ore_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))

        pygame.mixer.music.load('Audio/DiesIrae.mp3')
        #pygame.mixer.music.play(-1)

        grunt = pygame.mixer.Sound('Audio/Grunt_1.WAV')
    
    #FREE PLAY MODE
    def generate_row(self):
        y = 0
        x = len(self.TEST_MAP) // 4
        for i in range(4):
            current_chunk = Chunk()
            current_chunk.generate_chunk(x, y)
            self.TEST_MAP.append(current_chunk)
            y += 1

    def drawmap(self):
        for chunk in self.TEST_MAP:
            y = 0
            for row in chunk.CHUNK:
                x = 0
                for block in row:
                    if block == 0:
                        self.screen.blit(self.air_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))

                    elif block == 1:
                        self.screen.blit(self.grass_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))

                    elif block == 2:
                        random_num = Chunk().block_rotation(y, x)
                        if random_num == 0:
                            dirt_rotated_img = self.dirt_img
                        else:
                            dirt_rotated_img = pygame.transform.rotate(self.dirt_img, random_num * 90)
                        self.screen.blit(dirt_rotated_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    
                    elif block == 3:
                        self.screen.blit(self.place_rotated_block(self.stone_img, y, x), ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    
                    elif block == 4:
                        self.screen.blit(self.place_rotated_block(self.iron_ore_img, y, x), ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    
                    x += 1
                y += 1
    
    def redraw_sky(self):
        for chunk in self.TEST_MAP:
            y=0
            for row in chunk.CHUNK:
                x=0
                for block in row:
                    if block == 0:
                        self.screen.blit(self.air_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    else:
                        pass
                    x +=1
                y += 1
    
    def redraw_sky_level(self):
        for chunk in self.LEVEL_MAP:
            y=0
            for row in chunk.CHUNK:
                x=0
                for block in row:
                    if block == 0:
                        self.screen.blit(self.air_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    else:
                        pass
                    x +=1
                y += 1

    def place_rotated_block(self, block, y, x):
        random_num = Chunk().block_rotation(y, x)
        if random_num == 0:
            block_rotated_img = block
        else:
            block_rotated_img = pygame.transform.rotate(block, random_num * 90)
        return block_rotated_img
    
    #STORY MODE
    def level_row(self):
        y = 0
        x = len(self.LEVEL_MAP) // 4

        for i in range(4):
            current_chunk = Chunk()
            #print(self.LEVEL_MAP_NUMBERS[x][y])
            current_chunk.convert_map_to_chunks(x, y, self.LEVEL_MAP_NUMBERS)
            self.LEVEL_MAP.append(current_chunk)
            y += 1

    def draw_level(self):
        for chunk in self.LEVEL_MAP:
            y = 0
            for row in chunk.CHUNK:
                x = 0
                for block in row:
                    if block == 0:
                        self.screen.blit(self.air_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))

                    elif block == 1:
                        self.screen.blit(self.grass_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))

                    elif block == 2:
                        random_num = Chunk().block_rotation(y, x)
                        if random_num == 0:
                            dirt_rotated_img = self.dirt_img
                        else:
                            dirt_rotated_img = pygame.transform.rotate(self.dirt_img, random_num * 90)
                        self.screen.blit(dirt_rotated_img, ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    
                    elif block == 3:
                        self.screen.blit(self.place_rotated_block(self.stone_img, y, x), ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    
                    elif block == 4:
                        self.screen.blit(self.place_rotated_block(self.iron_ore_img, y, x), ((x + chunk.CHUNK_SIZE * chunk.x_y[0]) * self.BLOCK_SIZE, (y + chunk.CHUNK_SIZE * chunk.x_y[1]) * self.BLOCK_SIZE))
                    
                    x += 1
                y += 1
    