import pygame
from .globalvars import *

class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls: List[GRIDLOCATION] = []
        self.weights: Dict[GRIDLOCATION, float] = {}
    
    def in_bounds(self, id: GRIDLOCATION) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id: GRIDLOCATION) -> bool:
        return id not in self.walls
    
    def neighbors(self, id: GRIDLOCATION) -> Iterator[GRIDLOCATION]:
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results
    
    def cost(self, from_node: GRIDLOCATION, to_node: GRIDLOCATION) -> float:
        return self.weights.get(to_node, 1)
    
'''
class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.weights: Dict[GRIDLOCATION, float] = {}
    
    def cost(self, from_node: GRIDLOCATION, to_node: GRIDLOCATION) -> float:
        return self.weights.get(to_node, 1)
'''

def drawGrid(surface): #draws a grid pattern on the background to help visualize the snakes rows and colemns 
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (66, 66, 66), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (104, 104, 104), rr)

def generateGridCoordinates(): #generates all coordinate points on the grid board, this is used to generate the starting point. 
    for i in range(int(GRID_WIDTH)):
        for j in range(int(GRID_HEIGHT)):
            GRID.append((i*GRIDSIZE,j*GRIDSIZE))