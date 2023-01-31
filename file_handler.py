import os
import json

class File_Handler:
    def __init__(self):
        self.MAP = []

        self.levels = {0: 'Level Saves/Saved-Level-1.json',
                        1: 'Level Saves/Saved-Level-2.json'}

    def load(self, level):
        with open(self.levels[level], "r") as lvlmap:
            map_list = json.load(lvlmap)
        return map_list
