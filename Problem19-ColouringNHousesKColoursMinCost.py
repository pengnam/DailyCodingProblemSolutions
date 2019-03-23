"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.


"""
def solution(cost_matrix):
    N = len(cost_matrix)
    K = len(cost_matrix[0])
    memo = cost_matrix[N-1][:]
    for i in range(N-1)[::-1]:
        new_memo = [0] * K
        for j in range(K):
            new_memo[j] = min(memo[k] for k in range(K) if k != j) + cost_matrix[i][j]
        memo = new_memo
    return min(memo)
print(solution([[4,0,3],[8,3,8],[4,5,0],[3,4,4],[8,8,0]]))



