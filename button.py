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
        self.font = pygame.font.SysFont('Arial', 80)
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