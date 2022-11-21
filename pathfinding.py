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
        if chunk_x > 0:
            chunk_x = chunk_x * 4
        
        chunk = chunk_x + chunk_y

        block_x = pos[0] % 8
        block_y = pos[1] % 8

        row = block_y

        block = block_x



        return chunk, row, block
    
    def get_connected_nodes(self, pos):
        #Left One Block
        blockcoordsleft = self.convert_pos_to_block_numbers((pos[0]-1, pos[1]))
        print(blockcoordsleft)
        print(self.render.LEVEL_MAP_NUMBERS)
        if self.render.LEVEL_MAP_NUMBERS[blockcoordsleft[0]][blockcoordsleft[1]][blockcoordsleft[2]] in self.traversable_blocks:
            return self.render.LEVEL_MAP_NUMBERS[blockcoordsleft]
        return pos

class Node():
    def __init__(self, parent):
        pass
