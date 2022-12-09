from file_handler import File_Handler
import math

class PathFinder():
    def __init__(self, startpos, endpos, level):
        self.startpos = startpos
        self.endpos = endpos
        self.ConnectionAssessor = ConnectionAssessor(level)

        self.startnode = Node(None, endpos, startpos)
        self.route = []
        self.done = False
    
    def find_route(self):
        open_nodes = [self.startnode]

        iterations = 0
        while True:
            iterations += 1
            if iterations > 1000:
                print("Path Finding Out Of Range")
                self.done = True
                break
            current = None
            cheapest_node = None

            for node in open_nodes:
                if cheapest_node == None:
                    cheapest_node = node
                elif node.h < cheapest_node.h:
                    cheapest_node = node
            current = cheapest_node

            if current == None:
                print("Path Finding Failed")
                self.done = True
                break

            if current.nodepos == self.endpos:
                node = current
                while True:
                    if node.nodepos == self.startpos:
                        self.route.append(node.nodepos)
                        break

                    self.route.append(node.nodepos)
                    '''print(node.nodepos)'''
                    
                    
                    '''this pos then parents then parents and so on, then reverse list'''
                    node = node.parent
                
                self.done = True
                return self.route[::-1]
            

            open_nodes.remove(current)

            current_connections = self.ConnectionAssessor.get_connected_nodes(current.nodepos)

            for item in current_connections:
                node = Node(current, self.endpos, item)
                for opennode in open_nodes:
                    if node.nodepos == opennode.nodepos:
                        if node.h < opennode.h:
                            open_nodes.remove(opennode)
                            open_nodes.append(node)
                        break
                open_nodes.append(node)
        
    
    def is_done(self):
        return self.done



class ConnectionAssessor():
    def __init__(self, level):
        self.level = level

    MAP = None

    def __init__(self):
        if ConnectionAssessor.MAP == None:
            ConnectionAssessor.MAP = File_Handler().load(self.level)
        self.traversable_blocks = [0, 6]
   
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
            pass
            '''print(f"Not a possible move - block: {block}")'''

        # Check Right By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]+1, pos[1]))
        chunk = ConnectionAssessor.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        #possibly work on this later on
        if block in self.traversable_blocks:
            result = True
            count = 1
            while pos[1]+count >= 0 and result == True:
                chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]+1, pos[1]+count))
                chunk = self.MAP[chunk_x*4+chunk_y]
                row = chunk[block_y]
                block = row[block_x]

                #print(f"block {block}")
                #print(pos[0]+1, pos[1]+count)

                if block in self.traversable_blocks:
                    count += 1

                else:
                    connected_nodes.append((pos[0]+1, pos[1]))
                    result = False 
                    count = 1
            if pos[1]+count >= 0:
                #print("Not going down there bozo")
                pass
        else:
            connected_nodes.append((pos[0]+1, pos[1]))
            result = False 

        '''
        if block in self.traversable_blocks:
            connected_nodes.append((pos[0]+1, pos[1]))
        else:
            pass
                print(f"Not a possible move - block: {block}")'''

        # Check Down By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0], pos[1]-1))
        chunk = ConnectionAssessor.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            connected_nodes.append((pos[0], pos[1]-1))
        else:
            '''print(f"Not a possible move - block: {block}")'''
            pass

        # Check Up By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0], pos[1]+1))
        chunk = ConnectionAssessor.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            connected_nodes.append((pos[0], pos[1]+1))
        else:
            '''print(f"Not a possible move - block: {block}")'''
            pass
        
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
