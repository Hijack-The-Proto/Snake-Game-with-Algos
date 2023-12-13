from .graphs import *
from .queue import *
from .heuristics import *

def breadth_first_search(graph: Graph, start: LOCATION, goal: LOCATION):
    frontier = Queue()
    frontier.put(start)
    came_from: Dict[LOCATION, Optional[LOCATION]] = {}
    came_from[start] = None
    
    while not frontier.empty():
        current: LOCATION = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return came_from

def greedy_best_first_search(graph: Graph, start: LOCATION, goal: LOCATION):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: Dict[LOCATION, Optional[LOCATION]] = {}
    came_from[start] = None
    
    while not frontier.empty():
        current: LOCATION = frontier.get()
        print(current)
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                priority = greedy_heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from

def a_star_search(graph: Graph, start: LOCATION, goal: LOCATION, snake):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: Dict[LOCATION, Optional[LOCATION]] = {}
    cost_so_far: Dict[LOCATION, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    invert = False
    
    
    while not frontier.empty():
        current: LOCATION = frontier.get()
        print(current)
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal, start)
                if invert: frontier.put(next, priority*-1)
                else: frontier.put(next, priority)
                came_from[next] = current
    
    return came_from

def brute_force_search(snake):
    snake_head = snake.get_head_position()
    #Using some hard coding of edges, will fix later using the GRIDSIZE global variables

    #This segment takes care of the base cases of movment. the snake shoudl zigzag down the screen while keeping the farthest left column open
    if SCREEN_WIDTH-GRIDSIZE == snake_head[0] and snake.direction != DOWN: #Checking snake.direction lets us know what our last move was, eleminating the need for any vairables to be passed to this function
        snake.turn(DOWN)
    elif snake_head[0] > 20 and snake.direction != RIGHT:
        snake.turn(LEFT)
    if 20 == snake_head[0] and snake.direction != DOWN and snake_head[1] != 0.0: #This if check needed to ignore going down when the snake reached to top and turned right to begin the loop
        snake.turn(DOWN)
    elif 1 < snake_head[0] < SCREEN_WIDTH-GRIDSIZE and snake.direction != LEFT: # the 1 < here is to let the loop ignore any movement in the 0 column while the snake returns to the top of the board.
        snake.turn(RIGHT)

    #These dictate the loop the snake takes. when the snake reaches the lewest left point in its zig zag, regardless of what row it started on, 
    #it will turn left to begin going up to restart the loop. 
    if (20.0, SCREEN_HEIGHT-GRIDSIZE) == snake_head:
        snake.turn(LEFT)
    elif (0.0, SCREEN_HEIGHT-GRIDSIZE) == snake_head:
        snake.turn(UP)
    elif (0.0, 0.0) == snake_head:
        snake.turn(RIGHT)
    return snake 
