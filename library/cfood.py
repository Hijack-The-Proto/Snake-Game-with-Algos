import pygame
import random
from .globalvars import *

class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (255, 0, 0)
        self.randomize_position([(0,0)])

    def randomize_position(self, snake): 
        tmp = [elem for elem in GRID if elem not in snake]
        self.position = random.choice(tmp)

    def draw(self, surface):
        r = pygame.Rect((self.position[0]+1, self.position[1]+1), (GRIDSIZE-2, GRIDSIZE-2))
        pygame.draw.rect(surface, self.color, r)
