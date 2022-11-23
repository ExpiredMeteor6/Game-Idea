import pygame
from render import Render

class PathFinder():
    pass

class ConnectionAssessor():
    def __init__(self):
        self.render = Render()
        self.traversable_blocks = [0]
    
    def convert_pos_to_block_numbers(self, pos):
        chunk_x = pos[0] // 8
        chunk_y = pos[1] // 8
        block_x = pos[0] % 8
        block_y = pos[1] % 8
        return chunk_x, chunk_y, block_x, block_y
    
    def get_connected_nodes(self, pos):
        #Left One Block
        blockcoords = self.convert_pos_to_block_numbers((pos[0]-1, pos[1]))
        
        print(blockcoords)
        print(self.render.LEVEL_MAP_NUMBERS)
        if self.render.LEVEL_MAP_NUMBERS[blockcoords[0]*4+blockcoords[1]][blockcoords[2]][blockcoords[3]] in self.traversable_blocks:
            return self.render.LEVEL_MAP_NUMBERS[blockcoordsleft]
        return pos

class Node():
    def __init__(self, parent):
        pass
