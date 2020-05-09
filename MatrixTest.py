# initialization

grid = []

for x in range(5):
    grid.append([False] * 5)

print(grid)

# rendering

for x in len(grid):
    for y in len(grid[0]):
        if grid[x][y] == True:
            # draw a block in the right place
            # render_rect(X * 50, Y * 50, )
            pygame.draw.rect(WINDOW_SURFACE_NAME, RED, (x*50, y*50, 50, 50))