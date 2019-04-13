"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
"""
from collections import deque
def solution(matrix, start, end):
    #BFS. Helps me find optimal distance, maintains a queue
    q = deque()
    lr = [1,-1,0,0]
    ud = [0,0,1,-1]
    matrix[start[0]][start[1]] = 0
    q.append(start)
    while q:
        i,j= q.popleft()
        if i == end[0] and j == end[1]:
            return matrix[i][j]
        #Not wall or visited
        for k in range(4):
            new_r = i + lr[k]
            new_c = j + ud[k]
            if new_r < 0 or new_r >= len(matrix) or new_c < 0 or new_c >= len(matrix[0]) or matrix[new_r][new_c]!=False:
                continue

            else:
                matrix[new_r][new_c] = matrix[i][j] + 1
                q.append((new_r, new_c))
    return None

mat = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]
print(solution(mat, (3,0), (0,0)))


#Base case: if starting value is blocked

