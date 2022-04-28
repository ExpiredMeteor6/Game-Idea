from chunk import Chunk
from msilib.schema import Class
import opensimplex
opensimplex.seed(1453)


class Chunk:
    def __init__ (self):
        self.CHUNK_SIZE = 8
        self.x_y = (0, 0)
        self.CHUNK = []
    
    def generate_chunk(self, x, y):
        self.x_y = (x, y)
        #If top row, set to air
        if self.x_y[1] == 0:
            self.CHUNK = [[0 for x in range (8)] for y in range (8)]
        #If second row, use noise generation
        elif self.x_y[1] == 1:
            self.noise_generation()
        else:
            self.CHUNK = [[2 for x in range (8)] for y in range (8)]
    
    def noise_generation(self):
        self.CHUNK = [[2 for x in range (8)] for y in range (8)]
        for i in range(self.CHUNK_SIZE):
            height = opensimplex.noise2(x=self.x_y[0], y=0)
            self.CHUNK[self.convertNoiseToInt(height, 7)][i] = 1

        self.fill_air()
        
    def convertNoiseToInt(self, noise, variation):
        return int((noise + 1) / 2 * variation)
    
    def fill_air(self):
        for row in range(self.CHUNK_SIZE):
            for item in range(self.CHUNK_SIZE):
                if self.CHUNK[row][item] == 2:
                    self.CHUNK[row][item] = 0
                else:
                    return