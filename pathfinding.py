import pygame
from render import Render
from file_handler import File_Handler
import math

class PathFinder():
    def __init__(self, startpos, endpos):
        self.startpos = startpos
        self.endpos = endpos
        self.ConnectionAssessor = ConnectionAssessor()

        self.startnode = Node(None, endpos, startpos)
    
    def find_route(self):
        open_nodes = [self.startnode]

        while True:
            current = None
            cheapest_node = None

            for node in open_nodes:
                if cheapest_node == None:
                    cheapest_node = node
                elif node.h < cheapest_node.h:
                    cheapest_node = node

            if current == None:
                print("Path Finding Failed")
                break

            open_nodes.remove(current)

            current_connections = self.ConnectionAssessor.get_connected_nodes(current.nodepos)
            


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

        #possibly work on this later on
        '''if block in self.traversable_blocks:
            result = True
            count = 1
            while pos[1]-count >= 0 and result == True:
                chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]+1, pos[1]-count))
                chunk = self.MAP[chunk_x*4+chunk_y]
                row = chunk[block_y]
                block = row[block_x]

                if block in self.traversable_blocks:
                    pass
                    count += 1
                else:
                    connected_nodes.append((pos[0]+1, pos[1]))
                    result = False '''
        if block in self.traversable_blocks:
            connected_nodes.append((pos[0]+1, pos[1]))
        else:
            print(f"Not a possible move - block: {block}")

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
    def __init__(self, parent, endpos, nodepos):
        if parent == None:
            self.h = 0
        else:
            self.h = parent.h + 1

        self.f = self.distance_between_nodes(endpos, nodepos)
        self.g = self.h + self.f
        self.parent = parent
        self.nodepos = nodepos
    
    def distance_between_nodes(self, posA, posB):
        distance = math.sqrt((posA[0]-posB[0])**2 + (posA[1]-posB[1])**2)
        return distance
