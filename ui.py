import pygame

class Button():
    def __init__(self, render, colour, hovering_colour, text_colour, text, pos):
        self.render = render
        self.text_colour = text_colour
        self.screen = self.render.screen
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.colour = colour
        self.hovering_colour = hovering_colour
        self.font = pygame.font.SysFont('Comic Sans', 80)
        self.raw_text = text
        self.text = self.font.render(self.raw_text, True, self.text_colour)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def button_update(self):
        self.screen.blit(self.text, self.rect)
    
    def change_button_colour(self, mousepos):
        if mousepos[0] in range(self.rect.left, self.rect.right) and mousepos[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.raw_text, True, self.hovering_colour)
        else:
            self.text = self.font.render(self.raw_text, True, self.colour)
    
    def check_clicked(self, mousepos):
        if mousepos[0] in range(self.rect.left, self.rect.right) and mousepos[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False

class Image_Button():
    def __init__(self, render, image, pos):
        self.render = render
        self.screen = self.render.screen
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def button_update(self):
        self.screen.blit(self.image, self.rect)
    
    def check_clicked(self, mousepos):
        if mousepos[0] in range(self.rect.left, self.rect.right) and mousepos[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False


class Text():
    def __init__(self, render, text_colour, text, size, pos):
        self.render = render
        self.screen = self.render.screen
        self.text_colour = text_colour
        self.raw_text = text
        self.size = size
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.font = pygame.font.SysFont('Comic Sans', self.size)

        self.text = self.font.render(self.raw_text, True, self.text_colour)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def paste_text(self):
        self.screen.blit(self.text, self.rect)

class Display_Image():
    def __init__(self, render, image, pos):
        self.render = render
        self.screen = self.render.screen
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def paste_img(self):
        self.screen.blit(self.image, self.rect)
    
    