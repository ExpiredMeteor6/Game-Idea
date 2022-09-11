import pygame
import copy
import time
class Entity:
    def __init__(self, x, y, render, raymarch_func):
        self.render = render
        self.raymarch_func = raymarch_func
        self.position = [x, y]
    
    def on_key_press(self, key):
        pass

    def on_key_release(self, key):
        pass

    def get_texture(self):
        pass

    def tick(self):
        pass

class Player(Entity):
    def __init__(self, x, y, render, raymarch_func):
        super().__init__(x, y, render, raymarch_func)

        self.Player_Size = 32

        self.moving = 0
        self.speed = 4

        self.player_img_right = pygame.image.load('Images/blob_right.png')
        self.player_img_left = pygame.image.load('Images/blob_left.png')
        self.player_img_down_right = pygame.image.load('Images/blob_down_right.png')
        self.player_img_down_left = pygame.image.load('Images/blob_down_left.png')

        self.player_img_right = pygame.transform.scale(self.player_img_right, (self.Player_Size, self.Player_Size))
        self.player_img_left = pygame.transform.scale(self.player_img_left, (self.Player_Size, self.Player_Size))
        self.player_img_down_right = pygame.transform.scale(self.player_img_down_right, (self.Player_Size, self.Player_Size))
        self.player_img_down_left = pygame.transform.scale(self.player_img_down_left, (self.Player_Size, self.Player_Size))

        self.state = 0
        self.count = 0
        self.JUMPING = False
        self.count_at_activation = 0
        self.jump_decay = 0
        self.ON_GROUND = False
        self.downward_momentum = 0

    
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
    
    def tick(self):
        self.count += 1
        
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

        if self.moving != 0 and self.count % 5 == 0:
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

class Enemy:
    def __init__():
        pass

class Pet:
    def __init__():
        pass