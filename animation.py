from render import Render

class Idle:
    def __init__(self):
        self.render = Render()
        self.normal = self.render.player_img_right
        self.down = self.render.player_img_down_right
    
    def player_idle(self, player_state):
        if player_state == 0:
            pass