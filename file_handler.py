import os
import json

class File_Handler:
    def __init__(self):
        self.MAP = []

        self.levels = {0: 'Level Saves/test.json'}

    def load(self, level):
        with open(self.levels[0], "r") as lvlmap:
            map_list = json.load(lvlmap)
        return map_list
