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
    
    #Finds the shortest path to the player from the given entity (A* pathfinding)
    def find_route(self):
        open_nodes = [self.startnode]

        iterations = 0
        while True:
            iterations += 1
            #If this case is true, give up (stop process) as path finding is out of range
            if iterations > 1000:
                self.done = True
                self.route = None
                return self.route
            current = None
            cheapest_node = None

            for node in open_nodes:
                if cheapest_node == None:
                    cheapest_node = node
                elif node.h < cheapest_node.h:
                    cheapest_node = node
            current = cheapest_node

            #Covers for any unexpected errors, current should never be None and never has been. This is to avoid any issues if this case is ever met
            if current == None:
                print("Path Finding Failed")
                self.done = True
                self.route = None
                return self.route
            
            #If the is node is the same node that the player is in, end by adding that node to the list
            #Then find this nodes parent and that parent nodes parent until a list of nodes has been created
            #Then reverse the list to produce the final path
            if current.nodepos == self.endpos:
                node = current
                while True:
                    if node.nodepos == self.startpos:
                        self.route.append(node.nodepos)
                        break

                    self.route.append(node.nodepos)
                    node = node.parent
                
                self.done = True
                return self.route[::-1]
            

            open_nodes.remove(current)

            #All nodes that can be accessed from this current node
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
        
    #When called, returns self.done (True if process complete and False if process not complete)
    def is_done(self):
        return self.done



class ConnectionAssessor():
    MAP = None

    def __init__(self, level):
        #If MAP is none the level is loaded by the file handler class
        if ConnectionAssessor.MAP == None:
            ConnectionAssessor.MAP = File_Handler().load(level)
        #All blocks the pathfinder can go through
        self.traversable_blocks = [0, 5, 6, 7, 8, 9, 12]
   
    #Converts the position into the block number given as a chunkx, cunky, blockx, blocky
    def convert_pos_to_block_numbers(self, pos):
        chunk_x = pos[0] // 8
        chunk_y = pos[1] // 8
        block_x = pos[0] % 8
        block_y = pos[1] % 8
        return chunk_x, chunk_y, block_x, block_y
   
   #Gets all connected nodes to the node passed in by its position
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

        # Check Right By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]+1, pos[1]))
        chunk = ConnectionAssessor.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        #Checks if block is traversable then appends the node to the connected nodes list
        if block in self.traversable_blocks:
            result = True
            count = 1
            while pos[1]+count >= 0 and result == True:
                chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0]+1, pos[1]+count))
                chunk = self.MAP[chunk_x*4+chunk_y]
                row = chunk[block_y]
                block = row[block_x]

                if block in self.traversable_blocks:
                    count += 1

                else:
                    connected_nodes.append((pos[0]+1, pos[1]))
                    result = False 
                    count = 1
            
            #Stops pathfinding if it will fall down a deep pit
            if pos[1]+count >= 0:
                pass
        else:
            connected_nodes.append((pos[0]+1, pos[1]))
            result = False 

        # Check Down By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0], pos[1]-1))
        chunk = ConnectionAssessor.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            connected_nodes.append((pos[0], pos[1]-1))
        else:
            pass

        # Check Up By One Block  
        chunk_x,chunk_y,block_x,block_y = self.convert_pos_to_block_numbers((pos[0], pos[1]+1))
        chunk = ConnectionAssessor.MAP[chunk_x*4+chunk_y]
        row = chunk[block_y]
        block = row[block_x]

        if block in self.traversable_blocks:
            connected_nodes.append((pos[0], pos[1]+1))
        else:
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
    
    #Pythagoras theorem to get the distance between 2 nodes
    def distance_between_nodes(self, posA, posB):
        distance = math.sqrt((posA[0]-posB[0])**2 + (posA[1]-posB[1])**2)
        return distance
