import pygame
from render import Render
from file_handler import File_Handler

class PathFinder():
    pass

class ConnectionAssessor():
    def __init__(self):
        self.render = Render()
        self.MAP = File_Handler().load()
        self.traversable_blocks = [0]
   
    def convert_pos_to_block_numbers(self, pos):
        chunk_x = pos[0] // 8
        chunk_y = pos[1] // 8
        block_x = pos[0] % 8
        block_y = pos[1] % 8
        return chunk_x, chunk_y, block_x, block_y
   
    def get_connected_nodes(self, pos, direction):
        #Left One Block
        
        if direction == "left":
            left_or_right = 1
        elsif direction == "right":
            left_or_right = -1
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]-left_or_right, pos[1]))
       
        print(chunk_x,chunk_y,block_x,block_y)
        chunk = self.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            return block
        return pos

class Node():
    def __init__(self, parent):
        pass
