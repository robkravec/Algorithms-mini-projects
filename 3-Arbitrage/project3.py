# Import math and p3tests.
import math
from p3tests import *

################################################################################
"""

resetCurrency function

Resets adjacency list from a Currency object

INPUTS
adjList: An adjacency list from Currency object 

There is no explicit return value. The input will be "reset" such that all 
vertices have vert.prev = None and vert.dist = math.inf
"""
def resetCurrency(adjList):
    for vert in adjList:
        vert.prev = None
        vert.dist = math.inf
    return

################################################################################

"""

bellmanFord function

Performs a specified number of iterations of the Bellman-Ford algorithm.

INPUTS:
numiter: Number of iterations to run Bellman-Ford algorithm
adjList: An adjacency list from Currency object 
adjMat: A weighted adjacency matrix representing exchange rates between
currencies
tol: Tolerance to check for changes from one iteration of the algorithm to the
next

OUTPUTS:
adjList: A modified adjacency list
"""

def bellmanFord(numiter, adjList, adjMat, tol):
    for i in range(numiter):
        # For each vertex in the adjacency list, make an offer to every neighbor
        for vert in adjList:
            for neigh in vert.neigh:
                dist = adjMat[vert.rank][neigh.rank]
                # Update neighbor information if the offer is accepted
                if neigh.dist > vert.dist + dist + tol:
                    neigh.dist = vert.dist + dist 
                    neigh.prev = vert
    return adjList

################################################################################

"""
detectArbitrage

Detects negative cost cycles in a set of exchange rates.

INPUTS:
adjList: An adjacency list of Vertex objects 
adjMat: A weighted adjacency matrix representing exchange rates between
currencies
tol: Tolerance to check for changes from one iteration of the algorithm to the
next

OUTPUTS:
List of vertex ranks corresponding to a negative cost cycle

"""
def detectArbitrage(adjList, adjMat, tol=1e-15):

    # Reset all vertices in adjacency list
    resetCurrency(adjList)

    # Set first vertex distance to 0
    adjList[0].dist = 0

    # Perform V - 1 iterations of the Bellman-Ford algorithm
    first_iters = bellmanFord(len(adjList) - 1, adjList, adjMat, tol)
    first_dists = [vert.dist for vert in first_iters]

    # Perform one more iteration
    final_iter = bellmanFord(1, adjList, adjMat, tol)
    final_dists = [vert.dist for vert in final_iter]

    # Find one vertex that changed distance value in final iteration
    changed_dist = None
    for idx in range(len(adjList)):
        if first_dists[idx] != final_dists[idx]:
            changed_dist = idx
            break

    ### Find vertex ranks corresponding to negative cost cycle
    # If there was no vertex that changed distance, return an empty list
    if changed_dist is None:
        return []
    # Otherwise, initialize a list and keep adding to it until a repeat vertex 
    # is observed
    neg_cyc = []
    current = adjList[changed_dist]
    while True:
        if current.rank in neg_cyc:
            neg_cyc.append(current.rank)
            break
        else:
            neg_cyc.append(current.rank)
            current = current.prev
    # Trim down the list to only contain the negative cost cycle
    while neg_cyc[0] != current.rank:
        del neg_cyc[0]

    # Return the list of ranks in proper (reversed) order
    return neg_cyc[::-1]

################################################################################

"""
rates2mat

Takes rates matrix from Currency class object and creates adjacency 
matrix with correctly weighted edges.

INPUTS:
rates: rates matrix from Currency class object

OUTPUTS:
An unnamed adjacency matrix with correctly weighted edges

"""
def rates2mat(rates):
    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
