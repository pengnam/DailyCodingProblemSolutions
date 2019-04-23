def solution(n):
    def isValid(board, row, col):
        #Checks if a given board[row][col] is valid
        #Only checks left
        offset = 0
        for i in reversed(range(col)):
            offset += 1
            if board[row][i]:#Hor
                return False
            elif row-offset >= 0 and board[row-offset][i]:#Upper diag
                return False
            elif row+offset < n and board[row+offset][i]:#Lower diag
                return False
        return True


    def helper(i, board):
        if i >= n:
            return True
        for r in range(n):
            if isValid(board, r, i):
                board[r][i] = 1
                res = helper(i+1, board)
                if res:
                    return res
                else:
                    board[r][i] = 0


    board = [[0] * n for _ in range(n)]

    res = helper(0, board)
    if not res:
        return False
    for r in board:
        print(r)


print(solution(10))



