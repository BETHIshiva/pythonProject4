# Given K sorted lists of integers, KSortedArray[] of size N each. The task is to find the smallest range that includes at least one element from each of the K lists. If more than one such ranges are found, return the first such range found.
# import heapq
# Input:N = 5, K = 3
# KSortedArray[][] = {{1 3 5 7 9},{0 2 4 6 8},{2 3 5 7 11}}Output: 1 2
import sys
from heapq import heappop, heappush


# A class to store a heap node
class Node:
    def __init__(self, value, list_num, index):
        # `value` stores the element
        self.value = value

        # `list_num` stores the lists number of the element
        self.list_num = list_num

        # `index` stores the column number of the lists from which element was taken
        self.index = index

    # Override the `__lt__()` function to make `Node` class work with min-heap
    def __lt__(self, other):
        return self.value < other.value


# Function to compute the minimum range that includes at least one element
# from each of the given `M` lists
def findMinimumRange(lists):
    # invalid input
    if not lists:
        return -1, -1

    # `high` will be the maximum element in a heap
    high = -sys.maxsize

    # stores minimum and maximum elements found so far in a heap
    p = (0, sys.maxsize)

    # create an empty min-heap
    pq = []

    # push the first element of each lists into the min-heap
    # along with the lists number and their index in the lists
    for i in range(len(lists)):
        if not lists[i]:  # invalid input
            return -1, -1
        heappush(pq, Node(lists[i][0], i, 0))
        high = max(high, lists[i][0])

    # run till the end of any lists is reached
    while True:

        # remove the root node
        top = heappop(pq)

        # retrieve root node information from the min-heap
        low = top.value
        i = top.list_num
        j = top.index

        # update `low` and `high` if a new minimum is found
        if high - low < p[1] - p[0]:
            p = (low, high)

        # return on reaching the end of any lists
        if j == len(lists[i]) - 1:
            return p

        # take the next element from the "same" lists and
        # insert it into the min-heap
        heappush(pq, Node(lists[i][j + 1], i, j + 1))

        # update high if the new element is greater
        high = max(high, lists[i][j + 1])


if __name__ == '__main__':
    lists = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [2, 3, 5, 7, 11]]
    print(findMinimumRange(lists))