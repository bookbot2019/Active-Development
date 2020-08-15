import pygame, sys
from pygame.locals import *
import base64
from TetrisFont import Tetrisfont
from RGBTitle import RGBTitle
from TetrisLogo import logo
from BSOD import Cancer
from BSODFont import Death
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DOWN = pygame.USEREVENT
class Game:
    def __init__(self):
        self.running = True
        self.initialize_shapes()
        self.shape_rotation = 0

    def initialize_shapes(self):
        # initialize shapes with all rotations
        # shapes is a dictionary with a key:value pair of shape name:another dictionary
        # and inside that dictionary are key:value pairs of rotation:list of coords

        # initialize shapes with no rotations
        self.shapes = { "L" : { 0:  [[4, 0], [5, 0], [4, 1], [4, 2]],
                                90: [[0, -4], [0, -5], [1, -4], [2, -4]],
                                180:[[-4, 0], [-5, 0], [-4, -1], [-4, -2]],
                                270:[[0, 4], [0, 5], [-1, 4], [-2, 4]]},
                        "T" : { 0:  [[4, 1], [5, 1], [6, 1], [5, 0]],
                                90: [[1, -4], [1, -5], [1, -6], [0, -5]],
                                180:[[-4, -1], [-5, -1], [-6, -1], [-5, 0]],
                                270:[[-1, 4], [-1, 5], [-1, 6], [0, 5]]},
                        "S" : { 0: [[4, 0], [5, 0], [4, 1], [5, 1]],
                                90:[[0, -4], [0, -5], [1, -4], [1, -5]],
                                180:[[-4, 0], [-5, 0], [-4, -1], [-5, -1]],
                                270:[[0, 4], [0, 5], [-1, 4], [-1, 5]]}


    def run(self):
        # The main gameplay loop

        self.load_assets()
        self.initialize_game()
        
        clock = pygame.time.Clock()
        
        while self.running:
            self.handle_events()
            self.update(clock.tick())
            self.draw()
        
    def random_shape(self):
        # Returns a list of coordinates for a random shape
        r = randint(0,2)     
        if r == 0:
            # L shape
            new_shape = [[4, 0], [5, 0], [4, 1], [4, 2]]
        elif r == 1:
            # T shape
            new_shape = [[4, 1], [5, 1], [6, 1], [5, 0]]
        elif r == 2:
            # Square shape
            new_shape = [[4, 0], [5, 0], [4, 1], [5, 1]]  
        return new_shape
    
    def spawn_new_shape(self):
        # Modify self.grid to spawn a random shape 
        self.current_shape = self.random_shape()
        # s = self.random_shape()
        # for coord in s:
            # self.grid[coord[0]][coord[1]] = True 

    def handle_events(self):
    
        for event in pygame.event.get():
            if event.type == DOWN:
                
                '''
                for x, y in self.current_shape:
                    if self.grid[x][y+1] and not (x, y+1) in self.current_shape:
                        print('There\'s something below us!')
                for x, y in self.current_shape:
                    self.grid[x][y] = False
                for x, y in self.current_shape:
                    if y+1 < len(self.grid[0]):
                        self.grid[x][y+1] = True
                        print(self.current_shape)
                        '''

                # Erase stuff in the grid that overlaps self.current_shape
                for x, y in self.current_shape:
                    self.grid[x][y] = False
                # Check if by moving any part of the shape we'll go off the grid.
                # If so, we hit the bottom and need a new shape
                for x, y in self.current_shape:
                    if y+1 >= len(self.grid[0]):
                        self.spawn_new_shape()
                # Move y of all coordinates in self.current_shape down 1
                for c in self.current_shape:
                    c[1] += 1
                for x, y in self.current_shape:
                    self.grid[x][y] = True
                
                '''
                for x in range(len(self.grid)):
                    for y in reversed(range(len(self.grid[0]))):
                        print(x, y)
                        if self.grid[x][y] == True:
                            self.grid[x][y] = False
                            if y+1 < len(self.grid[0]): 
                                    self.grid[x][y+1] = True
                '''
                    
            if event.type == QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    def draw(self):
        # Handle game rendering
        self.windowSurface.fill(BLACK)
        pygame.draw.rect(self.windowSurface,WHITE,(550,0, 250, 600), 2)
        for x in range(0,600,50):
            pygame.draw.line(self.windowSurface,WHITE,(1,x),(550,x), 2)
            pygame.draw.line(self.windowSurface,WHITE,(x,1),(x,550), 2)


        self.title.render(self.windowSurface)
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] == True:
                    # draw a block in the right place
                    
                    pygame.draw.rect(self.windowSurface, RED, (x*50+2, y*50+2, 48, 48))
                    # need to change to random shape
        pygame.display.update()

    def update(self, deltaTime):
        
        pass

    def load_assets(self):
        # Load assets needed for the game.  This should only be called once.
        pygame.init()
        pygame.time.set_timer(DOWN, 500)
        with open('Tetrisfont.ttf', 'wb') as imagef:
            imagef.write(base64.b64decode(Tetrisfont))
        self.Font = pygame.font.Font('Tetrisfont.ttf', 48)
        with open('Logo.png', 'wb') as imagef:
            imagef.write(base64.b64decode(logo))
        with open('BSODFont.ttf', 'wb') as imagef:
            imagef.write(base64.b64decode(Death))
        self.BSODFont = pygame.font.Font('BSODFont.ttf', 48)
        with open('BSOD.png', 'wb') as imagef:
            imagef.write(base64.b64decode(Cancer))

        self.windowSurface = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Tetris')

        self.a = pygame.image.load('Logo.png')
        pygame.display.set_icon(self.a)
        
        
    
    def initialize_game(self):
        # Set up the board for play.  This can happen multiple times to restart the game.
        self.score = 0
        self.title = RGBTitle(self.Font, "Tetris", (200, 550), [WHITE, RED, GREEN, BLUE, GREEN, RED])

        grid_width = 11
        grid_height = 20
        self.grid = [[0 for x in range(grid_width)] for y in range(grid_height)] 

        self.spawn_new_shape()
if __name__ == '__main__':
    g = Game()
    g.run()
