import json

class File_Handler:
    def __init__(self):
        self.MAP = []

        self.levels = {0: 'Level Saves/Saved-Level-1.json',
                        1: 'Level Saves/Saved-Level-2.json'}

    #Loads the map coded for by the level number, read mode and create a python list from the json file
    def load(self, level):
        with open(self.levels[level], "r") as lvlmap:
            map_list = json.load(lvlmap)
        return map_list
