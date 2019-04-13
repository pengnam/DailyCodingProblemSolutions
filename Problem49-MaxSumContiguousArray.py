def solution(array):
    #Sliding window #Not relevant
    #Sum ending at current i
    result = 0
    curr = 0
    for i in array:
        curr = max(curr + i, i)
        result = max(result, curr)
    return result







print(solution( [34, -50, 42, 14, -5, 86]) == 137)
print(solution( [-5, -1, -8, -9]) == 0)
