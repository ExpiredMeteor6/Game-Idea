from tracemalloc import start
import pygame
import copy
import time
from pathfinding import PathFinder, Node, ConnectionAssessor
from thread_handler import Threader

class Entity:
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, level):
        self.render = render
        self.get_player_location = get_player_location
        self.raymarch_func = raymarch_func
        self.position = [x, y]
        self.get_block_coords = get_block_coords
        self.get_entity_location = get_entity_location

        
    
    def on_key_press(self, key):
        pass

    def on_key_release(self, key):
        pass

    def get_texture(self):
        pass

    def tick(self):
        pass

class Player(Entity):
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, level):
        super().__init__(x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, level)
        
        self.Player_Size = 32

        self.moving = 0
        self.speed = 4

        self.player_img_right = pygame.image.load('Images/blob_right.png')
        self.player_img_left = pygame.image.load('Images/blob_left.png')
        self.player_img_down_right = pygame.image.load('Images/blob_down_right.png')
        self.player_img_down_left = pygame.image.load('Images/blob_down_left.png')
        #self.blue_projectile = pygame.image.load('Images/blue_projectile.png')

        self.player_img_right = pygame.transform.scale(self.player_img_right, (self.Player_Size, self.Player_Size))
        self.player_img_left = pygame.transform.scale(self.player_img_left, (self.Player_Size, self.Player_Size))
        self.player_img_down_right = pygame.transform.scale(self.player_img_down_right, (self.Player_Size, self.Player_Size))
        self.player_img_down_left = pygame.transform.scale(self.player_img_down_left, (self.Player_Size, self.Player_Size))
        #self.blue_projectile = pygame.transform.scale(self.blue_projectile, (self.Player_Size, self.Player_Size))

        self.state = 0
        self.count = 0
        self.JUMPING = False
        self.count_at_activation = 0
        self.jump_decay = 0
        self.ON_GROUND = False
        self.downward_momentum = 0

        self.render = render

        self.dead = False
        self.finish_coords = self.render.finish_coords
        self.finished = False

    def get_texture(self):
        if self.state == 0:
            texture = self.player_img_right
        if self.state == 1:
            texture = self.player_img_left
        if self.state == 2:
            texture = self.player_img_down_right
        if self.state == 3:
            texture = self.player_img_down_left
        else:
            pass
        return texture
    
    def is_dead(self):
        if self.position[1] >= 1000:
            self.dead = True

    def get_world_position(self):
        self.world_position = [self.position[0] - self.render.movement_horizontal, self.position[1] - self.render.movement_vertical]
        return self.world_position

    def on_key_press(self, key):
        if key == pygame.K_d:
            self.moving = 1
            if self.state == 1 or self.state == 3:
                self.state = 0
        if key == pygame.K_a:
            self.moving = -1
            if self.state == 0 or self.state == 2:
                self.state = 1
        if key == pygame.K_SPACE:
            if self.count_at_activation == 0 and self.ON_GROUND == True:
                self.JUMPING = True
                self.count_at_activation = self.count
        
    def on_key_release(self, key):
        if key == pygame.K_d and self.moving == 1:
            self.moving = 0
        if key == pygame.K_a and self.moving == -1:
            self.moving = 0
    
    def convert_local_coords_to_global(self):
        node = self.get_block_coords((self.get_world_position()[0] + int(self.render.movement_horizontal) + 16, self.get_world_position()[1] + int(self.render.movement_vertical)))
        end_node = [node[0][0]*8 + node[1][0], node[0][1]*8 + node[1][1]]
        return end_node

    def check_reached_finish(self):
        if self.convert_local_coords_to_global() == self.finish_coords:
            self.finished = True
    
    def tick(self):
        self.count += 1

        self.is_dead()
        self.check_reached_finish()

        
        pos = copy.copy(self.position)
        pos[0] += 30
        pos[1] += 32
        can_move1 = self.raymarch_func(pos, (0, 1))

        pos = copy.copy(self.position)
        pos[1] += 32
        can_move2 = self.raymarch_func(pos, (0, 1))

        if can_move1 == 0 or can_move2 == 0:
            self.ON_GROUND = True
        else:
            self.ON_GROUND = False
        
        if self.JUMPING == False:
            pos = copy.copy(self.position)
            pos[0] += 30
            pos[1] += 32
            can_move1 = self.raymarch_func(pos, (0, 1))

            pos = copy.copy(self.position)
            pos[1] += 32
            can_move2 = self.raymarch_func(pos, (0, 1))

            self.position[1] += min(can_move1, can_move2, self.downward_momentum)

            if min(can_move1, can_move2, 10) == 0:
                self.downward_momentum = 0
            else:
                if self.downward_momentum < 14:
                    self.downward_momentum += 2
        else:
            pos = copy.copy(self.position)
            pos[0] += 30
            pos[1] += 10
            can_move1 = self.raymarch_func(pos, (0, -1))

            pos = copy.copy(self.position)
            pos[1] += 10
            can_move2 = self.raymarch_func(pos, (0, -1))

            self.position[1] -= min(can_move1, can_move2, 12 - self.jump_decay)

            if can_move1 == 0 or can_move2 == 0:
                self.jump_decay = 12
            
            if self.jump_decay == 12:
                self.JUMPING = False
                self.count_at_activation = 0
                self.jump_decay = 0
            else:
                self.jump_decay += 1


        if self.moving == 1:
            pos = copy.copy(self.position)
            pos[0] += 32
            can_move1 = self.raymarch_func(pos, (1, 0))

            pos = copy.copy(self.position)
            pos[0] += 32
            pos[1] += 31
            can_move2 = self.raymarch_func(pos, (1, 0))
            if min(can_move1, can_move2) >= 8:
                self.render.movement_horizontal -= self.moving / 4

        if self.moving == -1:
            pos = copy.copy(self.position)
            can_move1 = self.raymarch_func(pos, (-1, 0))

            pos = copy.copy(self.position)
            pos[1] += 31
            can_move2 = self.raymarch_func(pos, (-1, 0))
            if min(can_move1, can_move2) >= 8:
                self.render.movement_horizontal -= self.moving / 4

        if self.moving != 0 and self.count % 10 == 0:
            self.bounce()
        
        if self.moving == 0:
            if self.state == 2:
                self.state = 0
            elif self.state == 3:
                self.state = 1
    
    def idle(self):
        pass

    def bounce(self):
        if self.state == 0:
            self.state = 2
        elif self.state == 2:
            self.state = 0
        
        if self.state == 1:
            self.state = 3
        elif self.state == 3:
            self.state = 1
        

class Cloud(Entity):
    def __init__():
        super().__init__()
        pass

class Enemy(Entity):
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, level):
        super().__init__(x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, level)
        self.Player_Size = 32

        self.enemy_img_right = pygame.image.load('Images/red_blob_right.png')
        self.enemy_img_left = pygame.image.load('Images/red_blob_left.png')
        self.enemy_img_down_right = pygame.image.load('Images/red_blob_down_right.png')
        self.enemy_img_down_left = pygame.image.load('Images/red_blob_down_left.png')

        self.enemy_img_right = pygame.transform.scale(self.enemy_img_right, (self.Player_Size, self.Player_Size))
        self.enemy_img_left = pygame.transform.scale(self.enemy_img_left, (self.Player_Size, self.Player_Size))
        self.enemy_img_down_right = pygame.transform.scale(self.enemy_img_down_right, (self.Player_Size, self.Player_Size))
        self.enemy_img_down_left = pygame.transform.scale(self.enemy_img_down_left, (self.Player_Size, self.Player_Size))

        self.state = 0
        self.moving = 0
        self.speed = 4
        self.count = 0
        self.JUMPING = False
        self.count_at_activation = 0
        self.jump_decay = 0
        self.ON_GROUND = False
        self.downward_momentum = 0
        self.route = []
        self.get_player_world_position = get_player_location

        self.pathfinder = None
        self.level = level
        self.dead = False
        self.movement_pixels = 6
        
    
    def get_texture(self):
        if self.state == 0:
            texture = self.enemy_img_right
        if self.state == 1:
            texture = self.enemy_img_left
        if self.state == 2:
            texture = self.enemy_img_down_right
        if self.state == 3:
            texture = self.enemy_img_down_left
        else:
            pass
        return texture
    
    def is_dead(self):
        if self.position[1] >= 1000:
            self.dead = True
    
    def convert_local_coords_to_global(self, move):
        #print(self.get_player_world_position())
        move = True
        if move == True:
            start_node = self.get_block_coords((self.get_entity_location(1)[0] + int(self.render.movement_horizontal) * self.render.BLOCK_SIZE + 16, self.get_entity_location(1)[1] + int(self.render.movement_vertical) * self.render.BLOCK_SIZE))
            end_node = self.get_block_coords((self.get_player_world_position()[0] + int(self.render.movement_horizontal) + 16, self.get_player_world_position()[1] + int(self.render.movement_vertical)))

            start_pos = (start_node[0][0]*8 + start_node[1][0], start_node[0][1]*8 + start_node[1][1])
            end_pos = (end_node[0][0]*8 + end_node[1][0], end_node[0][1]*8 + end_node[1][1])
            return start_pos, end_pos
        else:
            start_node = self.get_block_coords(self.get_entity_location(1))
            end_node = self.get_block_coords(self.get_player_location())

            start_pos = (start_node[0][0]*8 + start_node[1][0] + int(self.render.movement_horizontal), start_node[0][1]*8 + start_node[1][1] + int(self.render.movement_vertical))
            end_pos = (end_node[0][0]*8 + end_node[1][0] + int(self.render.movement_horizontal), end_node[0][1]*8 + end_node[1][1] + int(self.render.movement_vertical))
            return start_pos, end_pos
        
    def get_offset_pos(self):
        pos = copy.copy(self.position)
        pos[0] += self.render.movement_horizontal * self.render.BLOCK_SIZE
        pos[1] += self.render.movement_vertical * self.render.BLOCK_SIZE
        return pos

    def on_key_press(self, key):
        if key == pygame.K_RIGHT:
            self.moving = 1
            if self.state == 1 or self.state == 3:
                self.state = 0
        if key == pygame.K_LEFT:
            self.moving = -1
            if self.state == 0 or self.state == 2:
                self.state = 1
        if key == pygame.K_UP:
            if self.count_at_activation == 0 and self.ON_GROUND == True:
                self.JUMPING = True
                self.count_at_activation = self.count
        
    def on_key_release(self, key):
        if key == pygame.K_RIGHT and self.moving == 1:
            self.moving = 0
        if key == pygame.K_LEFT and self.moving == -1:
            self.moving = 0


    def tick(self):
        if self.route == None:
            pass
        else:
            #print(self.route)
            if len(self.route) > 0:
                node = self.route[0]
                start_end_nodes = self.convert_local_coords_to_global(True)

                if start_end_nodes[0][0] < start_end_nodes[1][0]:
                    self.moving = 1
                    if self.state == 1 or self.state == 3:
                        self.state = 0
                if start_end_nodes[0][0] > start_end_nodes[1][0]:
                    self.moving = -1
                    if self.state == 0 or self.state == 2:
                        self.state = 1
                if start_end_nodes[0][1] > start_end_nodes[1][1]:
                    if self.count_at_activation == 0 and self.ON_GROUND == True:
                        self.JUMPING = True
                        self.count_at_activation = self.count

                if node == start_end_nodes[1]:
                    print(f"reached {node}")
                    self.route.remove(node)
                    self.moving = 0
                
            



                #relic either remove or develop later
                '''
                else:
                    print(node)
                    if start_end_nodes[1] in self.route:
                        print("test")
                        pos_in_list = self.route.index(node)
                        print(f"Pos_in_list = {pos_in_list}")
                        if pos_in_list > 0:
                            for i in range(pos_in_list):
                                print("skipped node")
                                self.route.remove(self.route[0])
                    else:
                        if node[0] < start_end_nodes[1][0]:
                            self.moving = 1
                            if self.state == 1 or self.state == 3:
                                self.state = 0
                        if node[0] > start_end_nodes[1][0]:
                            self.moving = -1
                            if self.state == 0 or self.state == 2:
                                self.state = 1
                        if node[1] > start_end_nodes[1][1]:
                            if self.count_at_activation == 0 and self.ON_GROUND == True:
                                self.JUMPING = True
                                self.count_at_activation = self.count

                        if node == start_end_nodes[1]:
                            print(f"correction reached {node}")
                            self.route.remove(node)
                            self.moving = 0
                            '''
        self.is_dead()

        self.count += 1
        
        pos = self.get_offset_pos()
        pos[0] += 30
        pos[1] += 32
        can_move1 = self.raymarch_func(pos, (0, 1))

        pos = self.get_offset_pos()
        pos[1] += 32
        can_move2 = self.raymarch_func(pos, (0, 1))
  
        if self.pathfinder == None and self.count % 20 == 0:
            nodes = self.convert_local_coords_to_global(False)
            #nodes = [(0, 0), (10, 10)]
            self.pathfinder = Threader(nodes[0], nodes[1], self.level)
            self.pathfinder.start_thread()

        if self.pathfinder != None:
            if self.pathfinder.is_done():
                self.route = self.pathfinder.get_result()
                self.pathfinder.destroy()
                self.pathfinder = None


        if can_move1 == 0 or can_move2 == 0:
            self.ON_GROUND = True
        else:
            self.ON_GROUND = False
        
        if self.JUMPING == False:
            pos = self.get_offset_pos()
            pos[0] += 30
            pos[1] += 32
            can_move1 = self.raymarch_func(pos, (0, 1))

            pos = self.get_offset_pos()
            pos[1] += 32
            can_move2 = self.raymarch_func(pos, (0, 1))
            self.position[1] += min(can_move1, can_move2, self.downward_momentum)

            if min(can_move1, can_move2, 10) == 0:
                self.downward_momentum = 0
            else:
                if self.downward_momentum < 14:
                    self.downward_momentum += 2
        else:
            pos = self.get_offset_pos()
            pos[0] += 30
            pos[1] += 10
            can_move1 = self.raymarch_func(pos, (0, -1))

            pos = self.get_offset_pos()
            pos[1] += 10
            can_move2 = self.raymarch_func(pos, (0, -1))

            self.position[1] -= min(can_move1, can_move2, 12 - self.jump_decay)

            if can_move1 == 0 or can_move2 == 0:
                self.jump_decay = 12
            
            if self.jump_decay == 12:
                self.JUMPING = False
                self.count_at_activation = 0
                self.jump_decay = 0
            else:
                self.jump_decay += 1

        if self.moving == 1:
            pos = self.get_offset_pos()
            pos[0] += 32
            can_move1 = self.raymarch_func(pos, (1, 0))

            pos = self.get_offset_pos()
            pos[0] += 32
            pos[1] += 31
            can_move2 = self.raymarch_func(pos, (1, 0))
            if min(can_move1, can_move2) >= self.movement_pixels:
                self.position[0] += self.movement_pixels

        if self.moving == -1:
            pos = self.get_offset_pos()
            can_move1 = self.raymarch_func(pos, (-1, 0))

            pos = self.get_offset_pos()
            pos[1] += 31
            can_move2 = self.raymarch_func(pos, (-1, 0))
            if min(can_move1, can_move2) >= self.movement_pixels:
                self.position[0] -= self.movement_pixels
        
        if self.moving != 0 and self.count % 20 == 0:
            self.bounce()
        
        if self.moving == 0:
            if self.state == 2:
                self.state = 0
            elif self.state == 3:
                self.state = 1
    
    def bounce(self):
        if self.state == 0:
            self.state = 2
        elif self.state == 2:
            self.state = 0
        
        if self.state == 1:
            self.state = 3
        elif self.state == 3:
            self.state = 1
    

class Pet(Entity):
    def __init__():
        pass
