from typing import Protocol, Dict, List, Iterator, Tuple, TypeVar, Optional

#Global Variables

GRIDSIZE = 20

GRID_WIDTH = 25
GRID_HEIGHT = 25

SCREEN_WIDTH = GRID_WIDTH * GRIDSIZE
SCREEN_HEIGHT = GRID_HEIGHT * GRIDSIZE

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

FPS = 60

T = TypeVar('T')
GRIDLOCATION = Tuple[int, int]
LOCATION = TypeVar('LOCATION')

GRID = []
MOVE_QUEUE = []