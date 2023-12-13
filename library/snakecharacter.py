import random
import sys
import pygame

from .globalvars import *


class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [random.choice(GRID)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.rotation = [(0,0)]
        self.new_direction = self.direction
        self.color = (0, 128, 0)
        self.initial_snake_speed = 50 # larger is slower
        self.snake_speed = self.initial_snake_speed
        self.max_length = int(GRID_WIDTH*GRID_HEIGHT)-15 #FIX ME: make this variable depending on the amount of spaces on the board at the start of the game. 

        self.head = (int(self.positions[0][0]/GRIDSIZE), int(self.positions[0][1]/GRIDSIZE))
        self.body = [self.head]

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if (point[0] * -1, point[1] * -1) == self.direction and self.length != 1:
            return
        else:
            self.new_direction = point

    def move(self, score_board):
        current = self.get_head_position()
        x, y = self.new_direction
        self.direction = self.new_direction
        new_head_position = (((current[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (current[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new_head_position in self.positions[2:]:
            self.reset(score_board)
        else:
            self.positions.insert(0, new_head_position)
            self.rotation.insert(0, self.direction)
            if len(self.positions) > self.length:
                self.positions.pop()
                self.rotation.pop()
    def reset(self, score_board):
        self.length = 1
        score_board.score = 0
        self.snake_speed = self.initial_snake_speed
        self.positions = [random.choice(GRID)]
        self.rotation = [(0,0)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])


    def draw(self, surface): #We create two rectangles, one representing the body position, and one lagging behind by 5 pixels to fill the gaps in the snake body. this is visually more appealing. 
        for p in range(len(self.positions)):
            r = pygame.Rect((self.positions[p][0]+1, self.positions[p][1]+1), (GRIDSIZE-2, GRIDSIZE-2))
            r_lag = pygame.Rect((self.positions[p][0]+1+((self.rotation[p][0]*-1)*5), self.positions[p][1]+1+((self.rotation[p][1]*-1)*5)), (GRIDSIZE-2, GRIDSIZE-2))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, self.color, r_lag)
            #pygame.draw.rect(surface, (93,216,228), r, 1)
    
    def convert_nums(self):
        self.head = (int(self.positions[0][0]/GRIDSIZE), int(self.positions[0][1]/GRIDSIZE))
        self.body = []
        for elm in self.positions:
            x, y = int(elm[0]/GRIDSIZE), int(elm[1]/GRIDSIZE)
            self.body.append((x, y))
        
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
