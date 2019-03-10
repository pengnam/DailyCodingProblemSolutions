def solution(array):
    #Check for 0 length arrays
    n = len(array)
    memo = [0] * n
    memo[0] = max(0,array[0])
    memo[1] = max(memo[0], array[1])
    for i in range(2, n):
        memo[i] = max(memo[i-1], memo[i])
        memo[i] = max(memo[i-2] + max(0,array[i]), memo[i])
    return memo[-1]
def alternative_solution(array):
    n = len(array)
    memo = [0] * 2
    memo[0] = max(0,array[0])
    memo[1] = max(memo[0], array[1])
    result = max(memo[0], memo[1])
    for i in range(2, n):
        result  = max(memo[1], 0)
        result = max(memo[0] + max(0,array[i]), result)
        memo[0], memo[1] = memo[1], result
    return result
print(alternative_solution( [2, 4, 6, 2, 5]) )
assert(alternative_solution( [2, 4, 6, 2, 5]) == 13)
assert(alternative_solution([5, 1, 1, 5]) == 10)

