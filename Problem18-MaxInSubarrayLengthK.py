"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8]
"""
from collections import deque
def solution(array, k):
    #Maintain a DS that does not store any value of a smaller index or smaller value
    d = deque()
    for idx, val in enumerate(array):#Check
        while d and d[0][0] <= idx - k:
            d.popleft()
        while d and d[-1][1] <= val:
            d.pop()
        d.append((idx, val))
        if idx + 1 >= k:
            max_idx, max_val = d[0]
            print(max_val)
    return

print(solution([10, 5, 2, 7, 8, 7] , 3))





