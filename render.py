import pygame
from terrain_handler import Chunk
from file_handler import File_Handler
import random
from PIL import Image

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

                                    [[0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
                                    [0, 0, 0, 0, 0, 0, 0, 0], 
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
        self.file = File_Handler()
        self.LEVEL_MAP = []
        self.SHOW_CHUNK_COORDS = False

        self.BLOCK_SIZE = 32

        self.movement_horizontal = 0
        self.movement_vertical = 0

        self.WINDOW_WIDTH = 2048
        self.WINDOW_HEIGHT = 1024

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.BG = pygame.image.load('Images/Background.png').convert()

        self.load_block_texture = lambda x: pygame.image.load(x).convert()

        self.scale_texture_normal = lambda x: pygame.transform.scale(x, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.scale_texture_large = lambda x: pygame.transform.scale(x, (self.BLOCK_SIZE * 10, self.BLOCK_SIZE * 10))

        self.grass_img = self.load_block_texture('Images/grass.png')
        self.air_img = self.load_block_texture('Images/air.png')
        self.dirt_img = self.load_block_texture('Images/dirt.png')
        self.stone_img = self.load_block_texture('Images/stone.png')
        self.gravel_img = self.load_block_texture('Images/gravel.png')
        self.iron_ore_img = self.load_block_texture('Images/iron_ore.png')
        self.start_img = self.load_block_texture('Images/start.png')
        self.finish_img = self.load_block_texture('Images/end.png')
        self.stone_background_img = self.load_block_texture('Images/stone_background.png')
        self.stone_background_start_img = self.load_block_texture('Images/start_stone.png')
        self.dirt_background_img = self.load_block_texture('Images/dirt_background.png')
        self.stone_background_stalagmite_img = self.load_block_texture('Images/stone_background_stalagmite.png')
        self.stone_background_stalactite_img = self.load_block_texture('Images/stone_background_stalactite.png')
        self.lava_dark_img = self.load_block_texture('Images/lava_dark.png')
        self.lava_light_img = self.load_block_texture('Images/lava_light.png')

        self.grass_img = self.scale_texture_normal(self.grass_img)
        self.air_img = self.scale_texture_normal(self.air_img)
        self.dirt_img = self.scale_texture_normal(self.dirt_img)
        self.stone_img = self.scale_texture_normal(self.stone_img)
        self.gravel_img = self.scale_texture_normal(self.gravel_img)
        self.iron_ore_img = self.scale_texture_normal(self.iron_ore_img)
        self.start_img = self.scale_texture_normal(self.start_img)
        self.finish_img = self.scale_texture_normal(self.finish_img)
        self.stone_background_img = self.scale_texture_normal(self.stone_background_img)
        self.stone_background_start_img = self.scale_texture_normal(self.stone_background_start_img)
        self.dirt_background_img = self.scale_texture_normal(self.dirt_background_img)
        self.stone_background_stalagmite_img = self.scale_texture_normal(self.stone_background_stalagmite_img)
        self.stone_background_stalactite_img = self.scale_texture_normal(self.stone_background_stalactite_img)
        self.lava_dark_img = self.scale_texture_normal(self.lava_dark_img)
        self.lava_light_img = self.scale_texture_normal(self.lava_light_img)

        pygame.mixer.init()
        self.music = pygame.mixer.music
        '''self.music.load('Audio/Timeless.mp3')'''
        '''self.music.play(-1)'''

        self.grunt = pygame.mixer.Sound('Audio/Grunt_1.WAV')

        self.font = pygame.font.SysFont(None, 12)
        self.music_volume = 1

        self.traversable_blocks = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.killing_blocks = [10, 11, 13]


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

    def convert_pil_image_to_pygame(self, img):
        return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

    def convert_pygame_image_to_pil(self, img):
        return Image.frombytes("RGBA",(self.BLOCK_SIZE,self.BLOCK_SIZE),pygame.image.tostring(img, "RGBA", False))
    
    def draw_chunk(self, chunk_x, chunk_y):
        chunk = self.LEVEL_MAP[chunk_x*4+chunk_y]
        image = chunk.image
        if image is None:
            new_image = Image.new('RGB',(8 * self.BLOCK_SIZE ,8 * self.BLOCK_SIZE), (250,250,250))
            y = 0
            for row in chunk.CHUNK:
                for x in range(len(row)):
                    placex = (x) * self.BLOCK_SIZE
                    placey = (y) * self.BLOCK_SIZE

                    block = row[x]

                    place_img = lambda i : new_image.paste(self.convert_pygame_image_to_pil(i),(placex,placey))
                    place_rotated_img = lambda i : place_img(self.place_rotated_block(i, y, x))

                    if block == 0 or block == 12:
                        place_img(self.air_img)

                    elif block == 1:
                        place_img(self.grass_img)

                    elif block == 2:
                        place_rotated_img(self.dirt_img)
                    
                    elif block == 3:
                        place_rotated_img(self.stone_img)
                    
                    elif block == 4:
                        place_rotated_img(self.iron_ore_img)
                    
                    elif block == 5:
                        place_img(self.start_img)
                    
                    elif block == 6:
                        place_img(self.finish_img)
                    
                    elif block == 7:
                        place_rotated_img(self.stone_background_img)
                    
                    elif block == 8:
                        place_img(self.stone_background_start_img)
                    
                    elif block == 9:
                        place_rotated_img(self.dirt_background_img)
                    
                    elif block == 10:
                        place_img(self.stone_background_stalagmite_img)

                    elif block == 11:
                        place_img(self.stone_background_stalactite_img)
                    
                    elif block == 13:
                        randomnum = random.randint(1,2)
                        if randomnum == 1:
                            place_rotated_img(self.lava_dark_img)
                        else:
                            place_rotated_img(self.lava_light_img)
                    
                    elif block == 14:
                        place_rotated_img(self.stone_img)


                y += 1
            '''new_image.show()'''

            chunk.image = self.convert_pil_image_to_pygame(new_image)
        else:
            self.screen.blit(image, (chunk_x * 8 * self.BLOCK_SIZE + self.movement_horizontal * self.BLOCK_SIZE, chunk_y * 8 * self.BLOCK_SIZE + self.movement_vertical * self.BLOCK_SIZE))


    def find_start(self):
        chunk_num = 0
        for chunk in self.LEVEL_MAP:
            row_within_chunk = 0
            for row in chunk.CHUNK:
                block_within_row = 0
                for block in row:
                    
                    if block == 5 or block == 8:
                        chunk_row_block = [chunk_num, row_within_chunk, block_within_row]
                        self.start_coords = [0, 0]

                        chunk_coords = [0, 0]
                        chunk_coords[0] += chunk_row_block[0] // 4
                        chunk_coords[1] += chunk_row_block[0] % 4

                        block_coords = [0, 0]
                        block_coords[0] += block_within_row
                        block_coords[1] += row_within_chunk

                        self.start_coords[1] = chunk_coords[1] * 8 + block_coords[1]
                        self.start_coords[0] = chunk_coords[0] * 8 + block_coords[0]

                        return
                    
                    else:
                        pass

                    block_within_row += 1
                row_within_chunk += 1
            chunk_num += 1
    
    def find_enemy_spawn_points(self):
        enemy_spawn_coords = []
        chunk_num = 0
        for chunk in self.LEVEL_MAP:
            row_within_chunk = 0
            for row in chunk.CHUNK:
                block_within_row = 0
                for block in row:
                    
                    if block == 12:
                        chunk_row_block = [chunk_num, row_within_chunk, block_within_row]
                        enemy_spawn = [0, 0]

                        chunk_coords = [0, 0]
                        chunk_coords[0] += chunk_row_block[0] // 4
                        chunk_coords[1] += chunk_row_block[0] % 4

                        block_coords = [0, 0]
                        block_coords[0] += block_within_row
                        block_coords[1] += row_within_chunk

                        enemy_spawn[1] = chunk_coords[1] * 8 + block_coords[1]
                        enemy_spawn[0] = chunk_coords[0] * 8 + block_coords[0]

                        enemy_spawn_coords.append(enemy_spawn)
                    
                    else:
                        pass

                    block_within_row += 1
                row_within_chunk += 1
            chunk_num += 1
        
        return enemy_spawn_coords

    def find_finish(self):
        chunk_num = 0
        for chunk in self.LEVEL_MAP:
            row_within_chunk = 0
            for row in chunk.CHUNK:
                block_within_row = 0
                for block in row:
                    
                    if block == 6:
                        chunk_row_block = [chunk_num, row_within_chunk, block_within_row]
                        self.finish_coords = [0, 0]

                        chunk_coords = [0, 0]
                        chunk_coords[0] += chunk_row_block[0] // 4
                        chunk_coords[1] += chunk_row_block[0] % 4

                        block_coords = [0, 0]
                        block_coords[0] += block_within_row
                        block_coords[1] += row_within_chunk

                        self.finish_coords[1] = chunk_coords[1] * 8 + block_coords[1]
                        self.finish_coords[0] = chunk_coords[0] * 8 + block_coords[0]

                        return
                    
                    else:
                        pass

                    block_within_row += 1
                row_within_chunk += 1
            chunk_num += 1
    
    def find_lava_drop_spawners(self):
        lava_drop_spawners = []
        chunk_num = 0
        for chunk in self.LEVEL_MAP:
            row_within_chunk = 0
            for row in chunk.CHUNK:
                block_within_row = 0
                for block in row:
                    
                    if block == 14:
                        chunk_row_block = [chunk_num, row_within_chunk, block_within_row]
                        lava_drop_spawn = [0, 0]

                        chunk_coords = [0, 0]
                        chunk_coords[0] += chunk_row_block[0] // 4
                        chunk_coords[1] += chunk_row_block[0] % 4

                        block_coords = [0, 0]
                        block_coords[0] += block_within_row
                        block_coords[1] += row_within_chunk

                        #Plus one to make entity spawn block below
                        lava_drop_spawn[1] = chunk_coords[1] * 8 + block_coords[1] + 1
                        lava_drop_spawn[0] = chunk_coords[0] * 8 + block_coords[0] 

                        lava_drop_spawners.append(lava_drop_spawn)
                    
                    else:
                        pass

                    block_within_row += 1
                row_within_chunk += 1
            chunk_num += 1
        
        return lava_drop_spawners

            

    def draw_level(self):
        for chunk in self.LEVEL_MAP:
            if chunk.x_y[0] + 1 <= abs(self.movement_horizontal / 8) or chunk.x_y[0] >= abs(self.movement_horizontal / 8) + 9:
                pass
                
            else:
                x = chunk.x_y[0]
                y = chunk.x_y[1]
                self.draw_chunk(x, y)

    def wipe(self):
        self.screen.fill((0,0,0))
    
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
