from tracemalloc import start
import pygame
import copy
import time
from pathfinding import PathFinder, Node, ConnectionAssessor
from thread_handler import Threader
import math

class Entity:
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level):
        self.render = render
        self.get_player_location = get_player_location
        self.raymarch_func = raymarch_func
        self.position = [x, y]
        self.get_block_coords = get_block_coords
        self.get_entity_location = get_entity_location
        self.level = level
        self.traversable_blocks = self.render.traversable_blocks
        self.killing_blocks = self.render.killing_blocks
        self.get_block = get_block
        self.dead = False

    def on_key_press(self, key):
        pass

    def on_key_release(self, key):
        pass

    def get_texture(self):
        pass

    def tick(self):
        pass
    
    def on_collide(self, entity):
       pass
        
class Player_Projectile(Entity):
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level):
        super().__init__(x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level)

        self.blue_projectile = self.render.load_entity_texture('Images/blue_projectile.png')
        self.blue_projectile_splat = self.render.load_entity_texture('Images/blue_projectile_splat.png')

        self.blue_projectile = self.render.scale_entity_texture(self.blue_projectile)
        self.blue_projectile_splat = self.render.scale_entity_texture(self.blue_projectile_splat)

        self.dead = False
        self.made_contact = False
        self.direction = False

        self.count = 0
        self.gravity = 0
        self.state = 0
        self.count_since_contact = 0

        self.entity_type = "Projectile"
    

    #Each entity state codes for a specific texture, the below function returns the texture of the entity when called
    def get_texture(self):
        if self.state == 0:
            return self.blue_projectile
        else:
            return self.blue_projectile_splat
    
    #Check if entity has made contact with a non traversable block
    def made_contact_with_block(self):
        if self.direction == True:
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE + 24, self.position[1] + 8])
            if block in self.traversable_blocks and block not in self.killing_blocks:
                pass
            else:
                self.made_contact = True
            
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE + 24, self.position[1] + 24])
            if block in self.traversable_blocks and block not in self.killing_blocks:
                pass
            else:
                self.made_contact = True
            
        else:
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE, self.position[1] + 8])
            if block in self.traversable_blocks and block not in self.killing_blocks:
                pass
            else:
                self.made_contact = True
            
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE, self.position[1] + 24])
            if block in self.traversable_blocks and block not in self.killing_blocks:
                pass
            else:
                self.made_contact = True

    #Move the y position of the entity down (gravity) and the x position either left or right dependent on direction of travel
    def move(self):
        if self.direction == False:
            self.position[0] -= 10
        else:
            self.position[0] += 10
        self.position[1] += self.gravity
    
    #The tick function when called by the main game loop, causes the entity to update
    def tick(self):
        self.count += 1
        #Every 2 ticks increase gravity by 0.5 (gains speed as projectile falls)
        if self.count % 2 == 0:
            self.gravity += 0.5
        #Check if projectile has made contact with block
        if self.made_contact == False:
            self.made_contact_with_block()
        if self.made_contact == True:
            if self.count_since_contact == 0:
                #Plays collision sound effect
                self.render.splat.set_volume(self.render.sound_effect_volume / 20)
                self.render.splat.play()

            self.state = 1
            if self.count_since_contact == 4:
                self.dead = True
            else:
                self.count_since_contact += 1
        else:
            self.move()

    #If the entity has collided with another entity, the main game loop calls this function which sets the entities state to the death state
    def on_collide(self, entity):
        if entity.entity_type == "Enemy":
            entity.shot = True
    
class Lava_Drop_Projectile(Entity):
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level):
        super().__init__(x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level)

        self.lava_drop_projectile = self.render.load_entity_texture('Images/lava_drop_projectile.png')
        self.lava_drop_projectile_splat = self.render.load_entity_texture('Images/lava_drop_projectile_splat.png')
        self.lava_drop_projectile = self.render.scale_entity_texture(self.lava_drop_projectile)
        self.lava_drop_projectile_splat = self.render.scale_entity_texture(self.lava_drop_projectile_splat)

        self.dead = False
        self.made_contact = False
        self.direction = False

        self.count = 0
        self.gravity = 0
        self.state = 0
        self.count_since_contact = 0

        self.entity_type = "Lava Drop"
    
    #Each entity state codes for a specific texture, the below function returns the texture of the entity when called
    def get_texture(self):
        if self.state == 0:
            return self.lava_drop_projectile
        else:
            return self.lava_drop_projectile_splat
    
    #Check if entity has made contact with a non traversable block
    def made_contact_with_block(self):
        if self.direction == True:
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE + 24, self.position[1] + 8])
            if block in self.traversable_blocks:
                pass
            else:
                self.made_contact = True
            
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE + 24, self.position[1] + 24])
            if block in self.traversable_blocks:
                pass
            else:
                self.made_contact = True
            
        else:
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE, self.position[1] + 8])
            if block in self.traversable_blocks:
                pass
            else:
                self.made_contact = True
            
            block = self.get_block([self.position[0] + self.render.movement_horizontal * self.render.BLOCK_SIZE, self.position[1] + 24])
            if block in self.traversable_blocks:
                pass
            else:
                self.made_contact = True

    #Move the y position of the entity down (gravity)
    def move(self):
        self.position[1] += self.gravity
    
    #The tick function when called by the main game loop, causes the entity to update
    def tick(self):
        self.count += 1
        #Every 2 ticks increase gravity by 0.5 (gains speed as projectile falls)
        if self.count % 2 == 0:
            self.gravity += 0.5
        #Check if projectile has made contact with block
        if self.made_contact == False:
            self.made_contact_with_block()

        if self.made_contact == True:
            self.state = 1
            if self.count_since_contact == 4:
                self.dead = True
            else:
                self.count_since_contact += 1
        else:
            self.move()

    #If the entity has collided with another entity, the main game loop calls this function which sets the entities state to the death state
    def on_collide(self, entity):
        if entity.entity_type == "Player":
            entity.shot = True
            self.made_contact = True
        
        if entity.entity_type == "Projectile":
            entity.made_contact = True
            self.made_contact = True


class Player(Entity):
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level):
        super().__init__(x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level)

        self.moving = 0

        self.player_img_right = self.render.load_entity_texture('Images/blob_right.png')
        self.player_img_left = self.render.load_entity_texture('Images/blob_left.png')
        self.player_img_down_right = self.render.load_entity_texture('Images/blob_down_right.png')
        self.player_img_down_left = self.render.load_entity_texture('Images/blob_down_left.png')
        self.player_img_right_explosion = self.render.load_entity_texture('Images/blob_right_explosion.png')
        self.player_img_left_explosion = self.render.load_entity_texture('Images/blob_left_explosion.png')
        

        self.player_img_right = self.render.scale_entity_texture(self.player_img_right)
        self.player_img_left = self.render.scale_entity_texture(self.player_img_left)
        self.player_img_down_right = self.render.scale_entity_texture(self.player_img_down_right)
        self.player_img_down_left = self.render.scale_entity_texture(self.player_img_down_left)
        self.player_img_right_explosion = self.render.scale_entity_texture(self.player_img_right_explosion)
        self.player_img_left_explosion = self.render.scale_entity_texture(self.player_img_left_explosion)

        self.state = 0
        self.count = 0
        self.JUMPING = False
        self.count_at_activation = 0
        self.jump_decay = 0
        self.ON_GROUND = False
        self.downward_momentum = 0

        self.render = render
        self.shot = False

        self.dead = False
        self.finish_coords = self.render.finish_coords
        self.finished = False
        self.shoot = False
        self.time_till_next_shot = 15
        self.count_since_death = 0

        self.entity_type = "Player"


    #Each entity state codes for a specific texture, the below function returns the texture of the entity when called
    def get_texture(self):
        if self.state == 0:
            texture = self.player_img_right
        if self.state == 1:
            texture = self.player_img_left
        if self.state == 2:
            texture = self.player_img_down_right
        if self.state == 3:
            texture = self.player_img_down_left
        if self.state == 4:
            texture = self.player_img_right_explosion
        if self.state == 5:
            texture = self.player_img_left_explosion
        else:
            pass
        return texture
    
    #Checks if the player is dead then sets the players state accordingly
    def is_dead(self):
        if self.position[1] >= 1000:
            self.dead = True

        self.get_world_position()
        if self.get_block([self.world_position[0] + 16 + self.render.movement_horizontal, self.world_position[1]+ 5]) in self.render.killing_blocks:
            if self.state == 0 or self.state == 2:
                self.state = 4

                #Plays death sound effect
                self.render.splat.set_volume(self.render.sound_effect_volume)
                self.render.splat.play()

            elif self.state == 1 or self.state == 3:
                self.state = 5

                #Plays death sound effect
                self.render.splat.set_volume(self.render.sound_effect_volume)
                self.render.splat.play()
            
        if self.shot == True:
            if self.state == 0 or self.state == 2:
                self.state = 4

                #Plays death sound effect
                self.render.splat.set_volume(self.render.sound_effect_volume)
                self.render.splat.play()

            elif self.state == 1 or self.state == 3:
                self.state = 5
            
                #Plays death sound effect
                self.render.splat.set_volume(self.render.sound_effect_volume)
                self.render.splat.play()
            
    #Finds the actual world position of the entity (where its located on the map not the screen) 
    def get_world_position(self):
        self.world_position = [self.position[0] - self.render.movement_horizontal, self.position[1] - self.render.movement_vertical]
        return self.world_position

    def on_key_press(self, key):
        if key == pygame.K_d:
            if self.state == 4 or self.state == 5:
                pass
            else:
                self.moving = 1
                if self.state == 1 or self.state == 3:
                    self.state = 0
        if key == pygame.K_a:
            if self.state == 4 or self.state == 5:
                pass
            else:
                self.moving = -1
                if self.state == 0 or self.state == 2:
                    self.state = 1
        if key == pygame.K_SPACE:
            if self.state == 4 or self.state == 5:
                pass
            else:
                if self.count_at_activation == 0 and self.ON_GROUND == True:
                    self.JUMPING = True
                    self.count_at_activation = self.count
    
    def on_mouse_button_click(self, mouse_button):
        if mouse_button == 1:
            if self.shoot == True:
                return False
            else:
                #Play spit sound effect when projectile is shot
                self.render.spit.set_volume(self.render.sound_effect_volume)
                self.render.spit.play()

                self.shoot = True
                return self.shoot

    #When movement key is released stop moving horizontally (self.moving = 0)   
    def on_key_release(self, key):
        if key == pygame.K_d and self.moving == 1:
            self.moving = 0
        if key == pygame.K_a and self.moving == -1:
            self.moving = 0
    
    #Converts the players screen position into a node within the map (block coordinate, used for enemy A* Pathfinding) 
    def convert_local_coords_to_global(self):
        node = self.get_block_coords((self.get_world_position()[0] + int(self.render.movement_horizontal) + 16, self.get_world_position()[1] + int(self.render.movement_vertical)))
        end_node = [node[0][0]*8 + node[1][0], node[0][1]*8 + node[1][1]]
        return end_node

    #Checks if the players coordinated match that of the block containing the finish flag, if thats the case it sets self.finished to True allowing the game to end and the level completed screen to be shown
    def check_reached_finish(self):
        if self.convert_local_coords_to_global() == self.finish_coords:
            self.finished = True
    
    #If the entity has collided with another entity, the main game loop calls this function which sets the players state to the death states
    #Player death is then detected in the tick function and processed there
    def on_collide(self, entity):
        if entity.entity_type == "Enemy":
            if entity.state == 4 or entity.state == 5:
                pass
            else:
                if self.state == 0 or self.state == 2:
                    self.state = 4
                elif self.state == 1 or self.state == 3:
                    self.state = 5
    
    #The tick function when called by the main game loop, causes the players character to update
    #Checks if player is dead or has reached the finish line
    #Updates the position of the player (allowing movement)
    #Reduces time till next shot each time this entity is 'ticked' (entity.tick function is called) until time_till_next_shot = 0 allowing the player to use the shooting function again
    #Updates players texture when moving (dependent on direction)
    #Every 10 ticks, calls the bounce function
    def tick(self):
        self.count += 1

        self.is_dead()
        self.check_reached_finish()

        if self.state == 4 or self.state == 5:
            if self.count_since_death == 10:
                self.dead = True
            else:
                self.count_since_death += 1

        else:
            pos = copy.copy(self.position)
            pos[0] += 30
            pos[1] += 32
            can_move1 = self.raymarch_func(pos, (0, 1))

            pos = copy.copy(self.position)
            pos[1] += 32
            can_move2 = self.raymarch_func(pos, (0, 1))

            if self.shoot == True:
                #Enable line below for no delay between shots
                #self.shoot = False
                if self.time_till_next_shot == 0:
                    self.shoot = False
                    self.time_till_next_shot = 15
                else:
                    self.time_till_next_shot -= 1

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
                #11 because blob is 22 pixels tall, tiles are 32, so 10 + 1
                pos[1] += 11
                can_move1 = self.raymarch_func(pos, (1, 0))

                pos = copy.copy(self.position)
                pos[0] += 32
                pos[1] += 31
                can_move2 = self.raymarch_func(pos, (1, 0))
                if min(can_move1, can_move2) >= 8:
                    self.render.movement_horizontal -= self.moving / 4

            if self.moving == -1:
                pos = copy.copy(self.position)
                #11 because blob is 22 pixels tall, tiles are 32, so 10 + 1
                pos[1] += 11
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

    #When the player moves this bounce function runs causing the character to look like hes bouncing up and down (gives the illusion of a more complex movement)
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
    def __init__(self, x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block, level):
        super().__init__(x, y, render, raymarch_func, get_player_location, get_block_coords, get_entity_location, get_block,level)

        self.enemy_img_right = self.render.load_entity_texture('Images/red_blob_right.png')
        self.enemy_img_left = self.render.load_entity_texture('Images/red_blob_left.png')
        self.enemy_img_down_right = self.render.load_entity_texture('Images/red_blob_down_right.png')
        self.enemy_img_down_left = self.render.load_entity_texture('Images/red_blob_down_left.png')
        self.red_blob_img_right_explosion = self.render.load_entity_texture('Images/red_blob_right_explosion.png')
        self.red_blob_img_left_explosion = self.render.load_entity_texture('Images/red_blob_left_explosion.png')

        self.enemy_img_right = self.render.scale_entity_texture(self.enemy_img_right)
        self.enemy_img_left = self.render.scale_entity_texture(self.enemy_img_left)
        self.enemy_img_down_right = self.render.scale_entity_texture(self.enemy_img_down_right)
        self.enemy_img_down_left = self.render.scale_entity_texture(self.enemy_img_down_left)
        self.red_blob_img_right_explosion = self.render.scale_entity_texture(self.red_blob_img_right_explosion)
        self.red_blob_img_left_explosion = self.render.scale_entity_texture(self.red_blob_img_left_explosion)

        self.state = 0
        self.moving = 0
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
        self.count_since_death = 0
        self.shot = False

        self.entity_type = "Enemy"
        self.entity_num = 0
        
    
    #Each entity state codes for a specific texture, the below function returns the texture of the entity when called
    def get_texture(self):
        if self.state == 0:
            texture = self.enemy_img_right
        if self.state == 1:
            texture = self.enemy_img_left
        if self.state == 2:
            texture = self.enemy_img_down_right
        if self.state == 3:
            texture = self.enemy_img_down_left
        if self.state == 4:
            texture = self.red_blob_img_right_explosion
        if self.state == 5:
            texture = self.red_blob_img_left_explosion
        else:
            pass
        return texture
    
    def is_dead(self):
        if self.position[1] >= 1000:
            if self.state == 0 or self.state == 2:
                self.state = 4
            elif self.state == 1 or self.state == 3:
                self.state = 5
        
        if self.shot == True:
            if self.state == 0 or self.state == 2:
                self.state = 4

                #Plays death sound effect
                self.render.splat.set_volume(self.render.sound_effect_volume)
                self.render.splat.play()

            elif self.state == 1 or self.state == 3:
                self.state = 5
                
                #Plays death sound effect
                self.render.splat.set_volume(self.render.sound_effect_volume)
                self.render.splat.play()
    
    def convert_local_coords_to_global(self, move):
        #print(self.get_player_world_position())
        move = True
        if move == True:
            start_node = self.get_block_coords((self.get_entity_location(self.entity_num)[0] + int(self.render.movement_horizontal) * self.render.BLOCK_SIZE + 16, self.get_entity_location(self.entity_num)[1] + int(self.render.movement_vertical) * self.render.BLOCK_SIZE))
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

    def on_collide(self, entity):
        if entity.entity_type == "Projectile":
            entity.made_contact = True
            self.shot = True

    def tick(self):
        if self.state == 4 or self.state == 5:
            if self.count_since_death == 10:
                self.dead = True
            else:
                self.count_since_death += 1
        else:
            if self.route == None:
                self.moving = 0
            else:
                if len(self.route) > 0:
                    node = self.route[0]
                    start_end_nodes = self.convert_local_coords_to_global(True)

                    if start_end_nodes[0][0] < start_end_nodes[1][0]:
                        self.moving = 1
                        #MOVE RIGHT
                        if self.state == 1 or self.state == 3:
                            self.state = 0
                    if start_end_nodes[0][0] > start_end_nodes[1][0]:
                        self.moving = -1
                        #MOVE LEFT
                        if self.state == 0 or self.state == 2:
                            self.state = 1
                    if start_end_nodes[0][1] > start_end_nodes[1][1]:
                        if self.count_at_activation == 0 and self.ON_GROUND == True:
                            self.JUMPING = True
                            self.count_at_activation = self.count
                            #JUMP

                    if node == start_end_nodes[1]:
                        #WHEN ENEMY REACHES NODE, REMOVE FROM LIST
                        self.route.remove(node)
                        #STOP MOVING
                        self.moving = 0
                    
                
            self.count += 1
            self.is_dead()

            pos = self.get_offset_pos()
            pos[0] += 30
            pos[1] += 32
            can_move1 = self.raymarch_func(pos, (0, 1))

            pos = self.get_offset_pos()
            pos[1] += 32
            can_move2 = self.raymarch_func(pos, (0, 1))
    
            if self.pathfinder == None and self.count % 20 == 0:
                nodes = self.convert_local_coords_to_global(False)
                if math.sqrt((nodes[0][0] - nodes[1][0])**2 + (nodes[0][1] - nodes[1][1])**2) < 8:
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
                pos[0] += 2
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
                pos[0] += 2
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
                
                self.position[0] += min(can_move1, can_move2, self.movement_pixels)

            if self.moving == -1:
                pos = self.get_offset_pos()
                can_move1 = self.raymarch_func(pos, (-1, 0))

                pos = self.get_offset_pos()
                pos[1] += 31
                can_move2 = self.raymarch_func(pos, (-1, 0))
                self.position[0] -= min(can_move1, can_move2, self.movement_pixels)
            
            if self.moving != 0 and self.count % 20 == 0:
                self.bounce()
            
            if self.moving == 0:
                if self.state == 2:
                    self.state = 0
                elif self.state == 3:
                    self.state = 1
    
    #When the enemy moves this bounce function runs causing the character to look like hes bouncing up and down (gives the illusion of a more complex movement)
    def bounce(self):
        if self.state == 0:
            self.state = 2
        elif self.state == 2:
            self.state = 0
        
        if self.state == 1:
            self.state = 3
        elif self.state == 3:
            self.state = 1