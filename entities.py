import pygame
import copy
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

    
    def get_texture(self):
        if self.state == 0:
            texture = self.player_img_right
        if self.state == 1:
            texture = self.player_img_left
        else:
            pass
        return texture

    def on_key_press(self, key):
        if key == pygame.K_d:
            self.moving = 1
            self.state = 1
        if key == pygame.K_a:
            self.moving = -1
            self.state = 0
        if key == pygame.K_SPACE:
            pass
    
    def on_key_release(self, key):
        if key == pygame.K_d and self.moving == 1:
            self.moving = 0
        if key == pygame.K_a and self.moving == -1:
            self.moving = 0
    
    def tick(self):
        pos = copy.copy(self.position)
        pos[0] += 32
        pos[1] += 32
        can_move1 = self.raymarch_func(pos, (0, 1))

        pos = copy.copy(self.position)
        pos[1] += 32
        can_move2 = self.raymarch_func(pos, (0, 1))

        self.position[1] += min(can_move1, can_move2, 16)
        
        if self.moving == 1:
            pos = copy.copy(self.position)
            pos[0] += 32
            can_move1 = self.raymarch_func(pos, (1, 0))

            pos = copy.copy(self.position)
            pos[0] += 32
            pos[1] += 32
            can_move2 = self.raymarch_func(pos, (1, 0))
            if min(can_move1, can_move2) >= 8:
                self.render.movement_horizontal += self.moving / 4
        
        if self.moving == 1:
            pos = copy.copy(self.position)
            can_move1 = self.raymarch_func(pos, (1, 0))

            pos = copy.copy(self.position)
            pos[1] += 32
            can_move2 = self.raymarch_func(pos, (1, 0))
            if min(can_move1, can_move2) >= 8:
                self.render.movement_horizontal += self.moving / 4
        

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