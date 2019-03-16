from collections import defaultdict
# Assumption: N>=1
def solution(N):
    memo = [None] * (N)
    if N > 0:
        memo[N-1] = 1
        if N > 1:
            memo[N-2] = 2
    #Index i in memo represents the number of steps that I plan to jump to
    for i in range(0, N-2)[::-1]:
        memo[i] = memo[i+1] + memo[i+2]
    return memo[0]

#O(N), O(N)
print(solution(1))

def alt_solution(N, X):
    memo = [0] * (N)
    #Index i in memo represents the number of steps that I plan to jump to
    for i in range(0, N)[::-1]:

        for step in X:
            next_val = i + step
            if next_val == N:
                memo[i] += 1
            elif next_val < N:
                memo[i] += memo[next_val]
    return memo[0]

print(alt_solution(4, [1,3]))





