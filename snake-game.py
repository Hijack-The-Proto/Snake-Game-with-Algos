from __future__ import annotations
import pygame
import time
import math
from library import *

def main():
    parser = argumentparser.create_argument_parser()
    args = parser.parse_args()
    grid.generateGridCoordinates() 
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((45,45,45))

    snake = snakecharacter.Snake()
    food = cfood.Food()
    score_board = score.Score()
    board = grid.SquareGrid(int(GRID_WIDTH), int(GRID_HEIGHT))

    myfont = pygame.font.SysFont("monospace", 16)

    time_elapsed = 0

    if args.bfs_search or args.greedy_search or args.a_star: # finds the initial path for bfs
        MOVE_QUEUE = movement.generate_moves(food, board, snake, args)
    else:
        MOVE_QUEUE = [(0,0)]

    while True:
        game_time = clock.tick(FPS)
        snake.handle_keys()
        surface.fill((45,45,45))

        time_elapsed += game_time
        if time_elapsed > snake.snake_speed: #Set the pace that the snake moves at so that it can be sped up as the game prgresses
            
            if args.bruteForce:
                searchalgos.brute_force_search(snake)
                snake.move(score_board)
            elif args.bfs_search or args.greedy_search or args.a_star:
                if not MOVE_QUEUE or len(MOVE_QUEUE) > 20:
                    MOVE_QUEUE = movement.generate_moves(food, board, snake, args)
                    print('CHECK')
                movement.search_move(MOVE_QUEUE, snake, score_board)
                if MOVE_QUEUE == 'bad':
                    print('survive')
            else:
                snake.move(score_board)
            time_elapsed = 0


        if snake.get_head_position() == food.position:
            if snake.length < snake.max_length:
                snake.length+=1
            score_board.score+=1
            food.randomize_position(snake.positions)
            snake.snake_speed = math.ceil(snake.snake_speed * 0.99)
            if args.bfs_search or args.greedy_search:
                MOVE_QUEUE = movement.generate_moves(food, board, snake, args)

        snake.draw(surface)
        food.draw(surface)
        if MOVE_QUEUE == 'bad':
            screen.blit(surface, (0,0))
            error_text = myfont.render('ERROR: NO PATH AVAILABLE', 1, (255,255,255))
            screen.blit(error_text, (5, 10))
            pygame.display.update()
            time.sleep(10)
            snake.reset(score_board)
            MOVE_QUEUE = movement.generate_moves(food, board, snake, args)


        screen.blit(surface, (0,0))
        text = myfont.render('Score {0} {1}'.format(score_board.score, snake.snake_speed), 1, (255,255,255))
        screen.blit(text, (5, 10))
        pygame.display.update()


    return

if __name__ == '__main__':
    main()