# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm

Implements Prim's algorithm to find a minimum spanning tree

INPUTS:
adjList - an adjacency list from a Map object
adjMat - an adjacency matrix from a Map object

There is no explicit output. vert.prev values are updated to denote the 
mimimum spanning tree

"""
def prim(adjList, adjMat):
    # Reset vertex attributes
    for vert in adjList:
        vert.visited = False
        vert.cost = math.inf
        vert.prev = None
    
    # Choose first vertex in adjList as start vertex
    adjList[0].cost = 0
    
    # Create priority queue
    Q = PriorityQueue(adjList)
    
    while not Q.isEmpty():
        # Visit next vertex in priority queue
        v = Q.deleteMin()
        v.visited = True
        # For each unvisited neighbor, make an offer
        for neigh in v.neigh:
            if not neigh.visited:
                if neigh.cost > adjMat[v.rank][neigh.rank]:
                    neigh.cost = adjMat[v.rank][neigh.rank]
                    neigh.prev = v
    return

################################################################################

"""
Kruskal's Algorithm

Implements Kruskal's algorithm to find a minimum spanning tree

INPUTS:
adjList - an adjacency list from a Map object
edgeList - a sorted list of edges from a Map object

OUTPUTS:
X - list of edges in the minimum spanning tree
"""
def kruskal(adjList, edgeList):
    # Create singleton set for each vertex in adjacency list
    for vert in adjList:
        makeset(vert)
        
    # Initialize empty MST
    X = []
    
    # Add edges to MST if they are not already in the same disjoint set
    for edge in edgeList:
        u, v = edge.vertices
        if not find(u).isEqual(find(v)):
            X.append(edge)
            union(u, v)
    
    # Return edges in MST
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.

INPUTS:
v - a vertex

There is no explict output. The parent and height of v are simply set.
"""
def makeset(v):
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here. To be explicit, path compression
means that we set each vertex in the disjoint set to have the root as its
parent.

INPUTS:
v - a vertex

OUTPUTS:
v.pi - the parent of the vertex, which is the root
"""
def find(v):
    # Keep returning the vertex parent until we reach the root
    if not v.isEqual(v.pi):
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.

INPUTS:
u, v - two vertices

There is no explicit output. The parent of either u or v is updated by 
assigning the root with greater height to be the parent of the root with 
smaller height. If the heights of the roots of u and v are the same, then the 
tie is arbitrarily broken, and the height of the chosen root is increased by 1.
"""
def union(u,v):
    # Find the roots of each vertex
    ru = find(u)
    rv = find(v)

    # If vertices are already in the same set, return
    if ru.isEqual(rv):
        return

    # Make shorter set point to taller set
    if ru.height > rv.height:
        rv.pi = ru 
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # Arbitrarily break ties, and increase height by 1
        ru.pi = rv
        rv.height += 1
    
    return

################################################################################

"""
TSP

Implement approximate solution to traveling salesman problem, using DFS on
MST generating from Prim's algorithm or Kruskal's algorithm.

INPUTS:
adjList - an adjacency list from a Map object
start - start vertex from a Map object

OUTPUTS:
tour - low cost TSP tour, starting and ending with the start vertex

"""
def tsp(adjList, start):
    # Iterate through vertices and set them all to unvisited
    for vert in adjList:
        vert.visited = False
        
    # Initialize tour and stack
    tour = []
    s = [start]
    start.visited = True
    
    # Perform DFS on MST to generate tour for TSP
    while s:
        current = s.pop()
        tour.append(current.rank)
        for vert in current.mstN:
            if not vert.visited:
                vert.visited = True
                s.append(vert)
    
    # Make sure that tour ends at start vertex
    tour.append(start.rank)
    
    # Return tour
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
