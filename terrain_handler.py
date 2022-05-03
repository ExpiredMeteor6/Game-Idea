import opensimplex
import random

#opensimplex.seed(1453)
opensimplex.seed(random.randint(0, 1000))

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
        #If second row, use noise generation for hills/land variation
        elif self.x_y[1] == 1:
            self.dirt_noise_generation()
        
        elif self.x_y[1] == 2:
            self.stone_noise_generation()

        elif self.x_y[1] > 2 and self.x_y[1] < 3:
            self.CHUNK = [[2 for x in range (8)] for y in range (8)]
        else:
            self.CHUNK = [[3 for x in range (8)] for y in range (8)]
            self.ore_generation()
    
    def dirt_noise_generation(self):
        self.CHUNK = [[2 for x in range (8)] for y in range (8)]
        for i in range(self.CHUNK_SIZE):
            height = opensimplex.noise2(x=((self.x_y[0] * self.CHUNK_SIZE + i) * 0.1 + 0.01), y=0)
            self.CHUNK[self.convertNoiseToInt(height, 7)][i] = 1

        self.fill_air()
    
    def stone_noise_generation(self):
        self.CHUNK = [[0 for x in range (8)] for y in range (8)]
        for i in range(self.CHUNK_SIZE):
            height = opensimplex.noise2(x=((self.x_y[0] * self.CHUNK_SIZE + i) * 0.3 + 100), y=0)
            self.CHUNK[self.convertNoiseToInt(height, 7)][i] = 3

        self.fill_dirt_stone()
    
    def ore_generation(self):
        for x in range(self.CHUNK_SIZE):
            for y in range(self.CHUNK_SIZE):
                cur_noise = opensimplex.noise2(x=((x + self.x_y[0] * self.CHUNK_SIZE) * 1.5 + 0.1), y=((y + self.x_y[1] * self.CHUNK_SIZE) * 1.5 + 0.1))
            if cur_noise > 0:
                self.CHUNK[x][y] = 4
        

    def convertNoiseToInt(self, noise, variation):
        return int((noise + 1) / 2 * variation)

    def fill_air(self):
        for i in range(self.CHUNK_SIZE):
            next = False
            x = 0
            while next == False:
                if self.CHUNK[x][i] == 2:
                    self.CHUNK[x][i] = 0
                else:
                    next = True
                x +=1
    
    def fill_dirt_stone(self):
        #Fills dirt above the 'created' stone line
        for i in range(self.CHUNK_SIZE):
            next = False
            x = 0
            while next == False:
                if self.CHUNK[x][i] == 0:
                    self.CHUNK[x][i] = 2
                else:
                    next = True
                x +=1

        #Fills stone beneath the 'created stone line
        for i in range(self.CHUNK_SIZE):
            next = False
            x = 0
            while next == False:
                if self.CHUNK[7-x][i] == 0:
                    self.CHUNK[7-x][i] = 3
                else:
                    next = True
                x +=1
    
    def block_rotation(self, ycoord, xcoord):
        rotation = opensimplex.noise2(x=((ycoord * self.CHUNK_SIZE * xcoord) * 0.3 + 100), y=0)
        return self.convertNoiseToInt(rotation, 4)