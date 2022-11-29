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
   
    def get_connected_nodes(self, pos):
        connected_nodes = []

        # Check Left By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]-1, pos[1]))
        chunk = self.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            connected_nodes.append((pos[0]-1, pos[1]))
        else:
            print(f"Not a possible move - block: {block}")

        # Check Right By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]+1, pos[1]))
        chunk = self.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            result = True
            count = 1
            while result == True:
                try:
                    chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]+1, pos[1]-count))
                    chunk = self.MAP[chunk_x*4+chunk_y]
                    row = chunk[block_y]
                    block = row[block_x]

                    if block in self.traversable_blocks:
                        pass
                        count += 1
                    else:
                        connected_nodes.append((pos[0]+1, pos[1]))
                        result = False
                except IndexError:
                    result = False
                
        # Check Down By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0], pos[1]-1))
        chunk = self.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            connected_nodes.append((pos[0], pos[1]-1))
        else:
            print(f"Not a possible move - block: {block}")

        # Check Up By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0], pos[1]+1))
        chunk = self.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            connected_nodes.append((pos[0], pos[1]+1))
        else:
            print(f"Not a possible move - block: {block}")
        
        return connected_nodes

class Node():
    def __init__(self, parent):
        pass
