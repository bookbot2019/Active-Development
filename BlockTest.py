print("Need Help Making Blocks Into Variables For Ease Of Use.")
import pygame, sys
from pygame.locals import *
import base64
from TetrisFont import Tetrisfont
from RGBTitle import RGBTitle
from TetrisLogo import logo
from BSOD import Cancer
from BSODFont import Death

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DOWN = pygame.USEREVENT
class Game:
    def __init__(self):
        self.running = True

    def run(self):
        # The main gameplay loop

        self.load_assets()
        self.initialize_game()
        
        clock = pygame.time.Clock()
        
        while self.running:
            self.handle_events()
            self.update(clock.tick())
            self.draw()
        
    
    def handle_events(self):
    
        for event in pygame.event.get():
            if event.type == DOWN:
                for ix, x in enumerate(self.grid):
                    for iy, y in enumerate(self.grid[0]):
                        print (y, end='')
                print('') # create a new line
                for x in range(len(self.grid)):
                    for y in reversed(range(len(self.grid[0]))):
                        if self.grid[x][y] == True:
                            self.grid[x][y] = False
                            if y+1 < len(self.grid[0]): 
                                    self.grid[x][y+1] = True
                            # print(x, y+1)t
                    
            if event.type == QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    def shapes(self):
        self.list1 = [(x*50+2, y*50+2)]
    def draw(self, list1):
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
                    # render_rect(X * 50, Y * 50, )
                    pygame.draw.rect(self.windowSurface, RED, (list1, 48, 48))
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
        grid_height = 11
        self.grid = [[0 for x in range(grid_width)] for y in range(grid_height)] 

        # self.grid = []
        # for x in range(11):
        #     self.grid.append([False] * 11)
        # self.grid[5][5] = True
      
        # print(self.grid)
        # print(len(self.grid))
        # print(len(self.grid[0]))
if __name__ == '__main__':
    g = Game()
    g.run()