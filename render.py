import pygame
from terrain_handler import Chunk
from file_handler import File_Handler
import random
from PIL import Image

class Render:
    def __init__(self):
        self.file = File_Handler()
        self.LEVEL_MAP = []

        self.BLOCK_SIZE = 32
        self.PLAYER_SIZE = 32

        self.movement_horizontal = 0
        self.movement_vertical = 0

        self.WINDOW_WIDTH = 2048
        self.WINDOW_HEIGHT = 1024

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.BG = pygame.image.load('Images/Background.png').convert()

        #Used to load block textures
        self.load_block_texture = lambda x: pygame.image.load(x).convert()
        #Used to load enemy textures
        self.load_entity_texture = lambda x: pygame.image.load(x)
        #Used to scale enemy textures
        self.scale_entity_texture = lambda x: pygame.transform.scale(x, (self.PLAYER_SIZE, self.PLAYER_SIZE))
        #Used scale block textures + one texture in the main file for the menu screens
        self.scale_texture_normal = lambda x: pygame.transform.scale(x, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        #Used to scale some image textures in the main file for menu screens
        self.scale_texture_large = lambda x: pygame.transform.scale(x, (self.BLOCK_SIZE * 10, self.BLOCK_SIZE * 10))

        #Loading textures
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

        #Scaling textures
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

        #Initialise the pygame mixer class then set starting volume to 1
        pygame.mixer.init()
        self.music = pygame.mixer.music
        self.music_volume = 1
        
        #Dictionary of all music that can be played
        self.music_dict = {0: "Audio/Darkness.mp3",
                           1: "Audio/Echoes of Time.mp3",
                           2: "Audio/Mist.mp3",
                           3: "Audio/Time.mp3",
                           4: "Audio/Timeless.mp3"}

        #Dictionary of the music set for each level
        self.level_music = {0 : self.music_dict[3],
                            1 : self.music_dict[2]}
        
        #Sound effects
        self.grunt = pygame.mixer.Sound('Audio/Grunt_1.WAV')

        #List of blocks that the player can move through
        self.traversable_blocks = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        #List of blocks that kill the player if the player moves into/through
        self.killing_blocks = [10, 11, 13]

        #Block x is [texture, rotated?, random texture?, extra texture if applicable]
        self.blocks = {0: [self.air_img, False, False, None],
                       1: [self.grass_img, False, False, None],
                       2: [self.dirt_img, True, False, None],
                       3: [self.stone_img, True, False, None],
                       4: [self.iron_ore_img, True, False, None],
                       5: [self.start_img, False, False, None],
                       6: [self.finish_img, False, False, None],
                       7: [self.stone_background_img, True, False, None],
                       8: [self.stone_background_start_img, False, False, None],
                       9: [self.dirt_background_img, True, False, None],
                       10: [self.stone_background_stalagmite_img, False, False, None],
                       11: [self.stone_background_stalactite_img, False, False, None],
                       12: [self.air_img, False, False, None],
                       13: [self.lava_dark_img, True, True, self.lava_light_img],
                       14: [self.stone_img, True, False, None]}

    #Rotates blocks (makes the textures look less linear)
    def place_rotated_block(self, block, y, x):
        random_num = Chunk().block_rotation(y, x)
        if random_num == 0:
            block_rotated_img = block
        else:
            block_rotated_img = pygame.transform.rotate(block, random_num * 90)
        return block_rotated_img
    
    #Creates a column of chunks
    def level_column(self):
        y = 0
        x = len(self.LEVEL_MAP) // 4

        for i in range(4):
            current_chunk = Chunk()
            current_chunk.convert_map_to_chunks(x, y, self.LEVEL_MAP_NUMBERS)
            self.LEVEL_MAP.append(current_chunk)
            y += 1

    #Converts image made in PIL (Library) to a pygame image
    def convert_pil_image_to_pygame(self, img):
        return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

    #Converts image loaded by pygame into a PIL (Library) image
    def convert_pygame_image_to_pil(self, img):
        return Image.frombytes("RGBA",(self.BLOCK_SIZE,self.BLOCK_SIZE),pygame.image.tostring(img, "RGBA", False))
    
    #Pastes the chunk image onto the screen given the coordinates
    def draw_chunk(self, chunk_x, chunk_y):
        chunk = self.LEVEL_MAP[chunk_x*4+chunk_y]
        image = chunk.image
        #If a chunk image has already been created, paste on screen. Else create a chunk image out of the block images (Optimisation for performance)
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

                    texture = self.blocks[block][0]
                    rotated = self.blocks[block][1]
                    randomed = self.blocks[block][2]

                    if randomed == True:
                        randomnum = random.randint(1,2)
                        if randomnum == 1:
                            texture = self.blocks[block][0]
                        else:
                            texture = self.blocks[block][3]
                    
                    if rotated == True:
                        place_rotated_img(texture)

                    else:
                        place_img(texture)

                y += 1

            chunk.image = self.convert_pil_image_to_pygame(new_image)
        else:
            self.screen.blit(image, (chunk_x * 8 * self.BLOCK_SIZE + self.movement_horizontal * self.BLOCK_SIZE, chunk_y * 8 * self.BLOCK_SIZE + self.movement_vertical * self.BLOCK_SIZE))


    #Looks for the start block in the map, then sets the self.start_coords variable to the coordinates of the start block
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

    #Looks for enemy spawn blocks in the map, then returns a list of all enemy entity spawn block coordinates
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

    #Looks for the finish block in the map, then sets the self.finish_coords variable to the coordinates of the finish block
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
    
    #Looks for the lava drop spawner blocks in the map, then returns a list of the coordinates of the block just beneath each given lava drop spawner blocks
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

            
    #Draws the level by pasting the images of each chunk on the screen, chunk by chunk
    def draw_level(self):
        for chunk in self.LEVEL_MAP:
            if chunk.x_y[0] + 1 <= abs(self.movement_horizontal / 8) or chunk.x_y[0] >= abs(self.movement_horizontal / 8) + 9:
                pass
                
            else:
                x = chunk.x_y[0]
                y = chunk.x_y[1]
                self.draw_chunk(x, y)

    #Sets the whole game screen to a set colour (like making a blank canvas)
    def wipe(self):
        self.screen.fill((0,0,0))
    
    #Converts a list of chunk lists into a list of chunk objects
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
