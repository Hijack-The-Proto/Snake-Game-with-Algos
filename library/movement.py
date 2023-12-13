from . import searchalgos
from .globalvars import *

def search_move(path, snake, score_board):
    if path == 'bad':
        return
    move = path[0]
    path.pop(0)
    snake.turn(move)
    snake.move(score_board)
    return

def reconstruct_path(came_from: Dict[LOCATION, LOCATION], start: LOCATION, goal: LOCATION) -> List[LOCATION]:

    current: LOCATION = goal
    path: List[LOCATION] = []
    if current not in came_from: # This checks to make sure a viable path was found. 
        print('ERROR')
        return 'bad'

    while current != start:
        path.append(current)
        current = came_from[current]
        
    path.append(start)
    path.reverse() #reverse the list so we can read it out start to goal for the snake to follow.
    print('\npath dump: \n')
    print(path)
    return path

def convertToMovement(path):
    if path == 'bad':
        return path
    moves = []
    start = path[0]

    for i in range(1, len(path), 1):
        if path[i] == (start[0]+UP[0], start[1]+UP[1]):
            moves.append(UP)
            start = path[i]
        elif path[i] == (start[0]+DOWN[0], start[1]+DOWN[1]):
            moves.append(DOWN)
            start = path[i]
        elif path[i] == (start[0]+RIGHT[0], start[1]+RIGHT[1]):
            moves.append(RIGHT)
            start = path[i]
        elif path[i] == (start[0]+LEFT[0], start[1]+LEFT[1]):
            moves.append(LEFT)
            start = path[i]


    return moves

def generate_moves(food, board, snake, args):
    snake.convert_nums()
    food_location = (int(food.position[0]/GRIDSIZE), int(food.position[1]/GRIDSIZE))
    board.walls = snake.body
    print('Food Location: {0} snake head {1}'.format(food_location, snake.head))
    if args.bfs_search:
        path = convertToMovement(reconstruct_path(searchalgos.breadth_first_search(board, snake.head, food_location), snake.head, food_location))
    elif args.greedy_search:
        path = convertToMovement(reconstruct_path(searchalgos.greedy_best_first_search(board, snake.head, food_location), snake.head, food_location))
    elif args.a_star:
        path = convertToMovement(reconstruct_path(searchalgos.a_star_search(board, snake.head, food_location, snake), snake.head, food_location))
    return path
