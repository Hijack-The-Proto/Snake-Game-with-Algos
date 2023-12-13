import argparse

def create_argument_parser():
    parser = argparse.ArgumentParser(description='Snake Game. Choose what Algorythem you would like to use, or choose nothing to play Snake yourself.')
    parser.add_argument('--brute-force', help='Solves snake using a brute force approach', action='store_true', dest='bruteForce', default=False)
    parser.add_argument('--bfs', help='Trys to solve snake by using a Bredth First Search approach', action='store_true', dest='bfs_search', default=False)
    parser.add_argument('--greedy', help='Trys to solve snake by using a Greedy Best First Search approach', action='store_true', dest='greedy_search', default=False)
    parser.add_argument('--a-star', help='Trys to solve snake by using the A* Search approach', action='store_true', dest='a_star', default=False)
    return parser