# Import p4tests.
from p4tests import *

# Additional imports
import numpy as np

################################################################################

"""
ED: the edit distance function

The goal of the edit distance function is to convert one input string (src)
into a different input string (dest) in the fewest possible number of edits.
This function returns both the minimum number of edits required to make this
transformation, as well as the specific edits required. Note that there may
be multiple ways to achieve the desired transformation in the minimum number
of edits, and this function will only return one of them.

INPUTS:
src - Starting string
dest - Destination string (that src will be converted into)
prob - The type of problem that we're trying to solve, either 'ED' for edit
distance or 'ASM' for approximate string matching

OUTPUTS:
dist - The minimum number of edits required to transform src into dest
edits - A list of edits, starting from the end of src, required to turn src
into dest. Each entry in the list is a 3-tuple
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')
        
    # Modify inputs to have leading spaces
    src = " " + src
    dest = " " + dest

    # Initialize dp table
    row_dim = len(src)
    col_dim = len(dest)
    dp = np.zeros((row_dim, col_dim))
    
    # Initialize edits list
    edits = []
    
    ### Base cases
    # Only fill in top row for 'ED'
    for idx in np.arange(col_dim):
        if prob == 'ED':
            if dest[idx] != " ":
                dp[0, idx] = dp[0, idx - 1] + 1
            else:
                dp[0, idx] = dp[0, idx - 1]
    # Fill in first column for both 'ED' and 'ASM'
    for idx in np.arange(row_dim):
        if src[idx] != " ":
            dp[idx, 0] = dp[idx - 1, 0] + 1
        else:
            dp[idx, 0] = dp[idx - 1, 0]
        
    # Fill in table by row, starting from top
    for row in np.arange(row_dim - 1):
        for col in np.arange(col_dim - 1):
            if src[row + 1] == dest[col + 1]:
                dp[row + 1][col + 1] = dp[row][col]
            else:
                dp[row + 1][col + 1] = 1 + \
                min(dp[row][col], dp[row][col + 1], dp[row + 1][col])
                    
    # Reconstruct edits, starting with answer in bottom right
    base = False
    row = row_dim - 1
    col = col_dim - 1
    # Document edits until a base case is hit
    while not base:
        # Letters match
        if src[row] == dest[col]:
            row -= 1
            col -= 1
        else:
            # Substitution
            if dp[row - 1][col - 1] <= dp[row - 1][col] and \
            dp[row - 1][col - 1] <= dp[row][col - 1] and row > 0 and col > 0:
                edits.append(('sub', dest[col], row - 1))
                row -= 1
                col -= 1
            # Deletion
            elif dp[row - 1][col] <= dp[row - 1][col - 1] and \
            dp[row - 1][col] <= dp[row][col - 1] and row > 0:
                edits.append(('delete', src[row], row - 1))
                row -= 1
            # Insertion
            else:
                edits.append(('insert', dest[col], row))
                col -= 1
        # Check for base case after each iteration
        if row < 0 or col < 0:
            base = True
          
    # Return edit distance and edits
    return dp[row_dim - 1][col_dim - 1], edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
