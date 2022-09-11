import os
import json

class File_Handler:
    def __init__(self):
        self.MAP = []

    def load(self):
        with open('Level Saves/test.json', "r") as lvlmap:
            map_list = json.load(lvlmap)
        return map_list
