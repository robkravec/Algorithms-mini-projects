"""
SelectionSort

This function sorts an input list in place by iteratively finding the
minimum element of the "unsorted" portion of the list and adding it to 
the end of the "sorted" portion of the list.

INPUTS
listToSort: an input list that may be sorted or unsorted

OUTPUTS
listToSort: the input list sorted in place
"""
def SelectionSort(listToSort):
    # Calculate length of input list, which will be used for 2 different 
    # for loops
    list_length = len(listToSort)
    
    # Iteratively increase length of "sorted" part of list by 1, 
    # starting at k = 0
    for idx in range(list_length - 1):
        k = idx
        # Initialize minimum index and value in "unsorted" part of list
        min_idx = k
        min_val = listToSort[k]
        # Find minimum index and value in "unsorted" part of list
        for idx_unsorted in range(k, list_length):
            if listToSort[idx_unsorted] < min_val:
                min_val = listToSort[idx_unsorted]
                min_idx = idx_unsorted
        # Instead of moving each value down one spot to insert minimum element,
        # simply perform a swap of the minimum value and the first element in 
        # the "unsorted" portion of the list
        listToSort[idx], listToSort[min_idx] = \
        listToSort[min_idx], listToSort[idx]
    
    return listToSort

"""
InsertionSort

This function sorts an input list in place by iteratively placing the
first element of the "unsorted" portion of the list into the correct (sorted) 
location of the "sorted" portion of the list.

INPUTS
listToSort: an input list that may be sorted or unsorted

OUTPUTS
listToSort: the input list sorted in place
"""
def InsertionSort(listToSort):
    # Calculate length of input list
    list_length = len(listToSort)
    
    # Loop through each element of the input array and insert element into 
    # correct location
    for idx in range(1, list_length):
        
        # Bubble current element through sorted part of list
        for idx2 in reversed(range(1, idx + 1)):
            if listToSort[idx2] < listToSort[idx2 - 1]:
                listToSort[idx2], listToSort[idx2 - 1] = \
                listToSort[idx2 - 1], listToSort[idx2]
            # Move to next iteration as soon as one bubble is rejected
            else:
                break
                
    return listToSort

"""
BubbleSort

This function sorts an input list in place by iteratively going through
the list swapping elements when the element on the right is larger than the
element on the left.

INPUTS
listToSort: an input list that may be sorted or unsorted

OUTPUTS
listToSort: the input list sorted in place
"""
def BubbleSort(listToSort):
    
    # Calculate length of input list
    list_length = len(listToSort)
    
    # Initialize number of swaps in a given iteration
    num_swaps = 1
    k = 0
    
    # Iteratively bubble list until no swaps occur during an iteration
    while num_swaps > 0:
        num_swaps = 0
        # Cycle through list looking for swap opportunities
        for idx in range(list_length - k - 1):
            if listToSort[idx] > listToSort[idx + 1]:
                num_swaps += 1
                listToSort[idx], listToSort[idx + 1] = \
                listToSort[idx + 1], listToSort[idx]
                
        # After each iteration, we can shorten the list we check by one element
        k += 1
    
    return listToSort

"""
MergeSort

This function sorts an input list by recursively breaking the list in half,
sorting each half, and then strategically merging the halves
to create a sorted list. The sorting is not done in place, but the results
are copied back to the input list.

INPUTS
listToSort: an input list that may be sorted or unsorted

OUTPUTS
listToSort: the input list, sorted
"""
def MergeSort(listToSort):

    # Base case 1: If list has one element, return
    if len(listToSort) == 1:
        return listToSort
    
    # Base case 2: If list has two elements, swap elements if needed and then 
    # return
    if len(listToSort) == 2:
        if listToSort[0] > listToSort[1]:
            listToSort[0], listToSort[1] = listToSort[1], listToSort[0]
        return listToSort
    
    # Recursively call MergeSort to sort each half
    k = len(listToSort) // 2
    left_half = MergeSort(listToSort[:k])
    right_half = MergeSort(listToSort[k:])
    
    # Merge sorted halves
    sorted_array = []
    while len(left_half) > 0 or len(right_half) > 0:
        if len(left_half) == 0:
            sorted_array.append(right_half.pop(0))
        elif len(right_half) == 0:
            sorted_array.append(left_half.pop(0))
        else:
            if left_half[0] < right_half[0]:
                sorted_array.append(left_half.pop(0))
            else:
                sorted_array.append(right_half.pop(0))
    
    # Copy sorted array values to listToSort
    listToSort[:] = sorted_array.copy()

    return listToSort

"""
QuickSort

This function sorts an input list by (1) choosing a pivot value, (2)
partitioning the list into values less than the pivot value vs. greater
than or equal to the pivot value, (3) recursively sorting both parts of 
the list. Sort a list with the call QuickSort(listToSort), 
or additionally specify i and j.

INPUTS
listToSort: an input list that may be sorted or unsorted

OUTPUTS
listToSort: the input list sorted in place
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
        
    # Base case 1: If list has zero or one element, return
    if i == j - 1 or i == j:
        return listToSort
    
    # Base case 2: If list has two elements, swap elements if 
    # needed and then return
    if i == j - 2:
        if listToSort[i] > listToSort[j - 1]:
            listToSort[i], listToSort[j - 1] = listToSort[j - 1], listToSort[i]
        return listToSort
    
    # Save values of i and j prior to partitioning
    a = i
    b = j
    
    # Choose partition value. For simplicity, I'll choose the middle index
    pivot = (i + j - 1) // 2
    pivot_val = listToSort[pivot]
    
    # Partition until i >= j - 1. i can only moved to the right when 
    # listToSort[i] < pivot_val. j can only move to the left when 
    # listToSort[j] > pivot_val 
    while i < j - 1:
        if listToSort[i] < pivot_val:
            i += 1
        elif listToSort[j - 1] > pivot_val:
            j -= 1
        # Switch elements if both i and j are stuck with special case for 
        # both being stuck on pivot value
        else:
            if listToSort[i] == pivot_val and listToSort[j - 1] == pivot_val:
                i += 1
                pivot = j - 1
            else:
                listToSort[i], listToSort[j - 1] = listToSort[j - 1], \
                listToSort[i]
                # Keep track of pivot location if elements are swapped
                if i == pivot:
                    pivot = j - 1
                elif j - 1 == pivot:
                    pivot = i    
    
    # Recursively sort both parts of list
    QuickSort(listToSort, i=a, j=pivot)
    QuickSort(listToSort, i=pivot, j=b)
    
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
