# Import math and other p2 files.
import math
from p2tests import *

"""
resetMaze function

INPUTS
maze: A Maze object representing the maze

There is no explicit return value. The input will be "reset" to have
an empty path and all vertices set such that vert.prev = None, 
vert.dist = None, and vert.visited = False
"""
def resetMaze(maze):
    maze.path = []
    for vert in maze.adjList:
        vert.prev = None
        vert.dist = None
        vert.visited = False
    return

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # Reset maze if it has already been solved
    if len(maze.path) > 0:
        resetMaze(maze)

    # Initialize appropriate data structure based on algorithm choice
    if alg == 'DFS':
        storage = Stack()
    else:
        storage = Queue()

    # Push start into storage and update start attributes
    maze.start.visited = True
    maze.start.dist = 0
    storage.push(maze.start)

    # Search until the exit is found
    exit_found = False
    while not exit_found:
        current = storage.pop()
        for neighbor in current.neigh:
            if not neighbor.visited: 
                storage.push(neighbor)
                neighbor.visited = True
                neighbor.dist = current.dist + 1
                neighbor.prev = current
            # Stop searching when the exit is found
            if neighbor.rank == maze.exit.rank:
                exit_found = True
                current = neighbor
                break

    # Once exit has been found, follow vertex.prev values to trace out
    # the full path
    full_path = False
    while not full_path:
        maze.path.append(current.rank)
        if current.rank == maze.start.rank:
            full_path = True
        current = current.prev
    # Since we discover the path from the exit to the start, we need to reverse
    maze.path = maze.path[::-1]

    return maze.path

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
