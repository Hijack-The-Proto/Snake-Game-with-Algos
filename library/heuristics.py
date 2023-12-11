import math
from .globalvars import *

def heuristic(current: GRIDLOCATION, goal: GRIDLOCATION, start) -> float:

    dx1 = current[0] - goal[0]
    dy1 = current[1] - goal[1]
    dx2 = start[0] - goal[0]
    dy2 = start[1] - goal[1]
    cross = abs(dx1*dy2 - dx2*dy1)
    return cross*0.001

def greedy_heuristic(a: GRIDLOCATION, b: GRIDLOCATION):
    (x1, y1) = a
    (x2, y2) = b
    num  = math.sqrt((abs(x1 - x2)**2) + (abs(y1 - y2)**2))
    #print(num)
    return num
