import opensimplex
import random

#Sets perlin noise seed to a random number between 0 and 1000
opensimplex.seed(random.randint(0, 1000))

class Chunk:
    def __init__ (self):
        self.CHUNK_SIZE = 8
        self.x_y = (0, 0)
        self.CHUNK = []
        self.image = None

    #Sets chunk x, y to coordinates passed in
    def convert_map_to_chunks(self, x, y, MAP):
        self.x_y = (x, y)
        self.CHUNK = MAP[x][y]      

    #Converts noise to an integer value, (variation is how many variations of the texture that there can be ie 4 rotations of a dirt block)
    def convertNoiseToInt(self, noise, variation):
        return int((noise + 1) / 2 * variation)
    
    #Using perlin noise (opensimplex library to generate a more realistic pseudo random block rotation)
    def block_rotation(self, ycoord, xcoord):
        rotation = opensimplex.noise2(x=((xcoord + self.x_y[0] * self.CHUNK_SIZE) * 1.5 + 0.05), y=((ycoord + self.x_y[1] * self.CHUNK_SIZE) * 1.5 + 0.05))
        return self.convertNoiseToInt(rotation, 4)