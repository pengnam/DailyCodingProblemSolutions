def solution(str1, str2):
    m = len(str1)
    n = len(str2)
    memo = [[None] * n for _ in range(m)]

    def helper(i,j):
        #Think about whether they should return 0
        if i >= m:
            return n - j
        elif j >= n:
            return m - i
        elif memo[i][j] != None:
            return memo[i][j]

        if str1[i] == str2[j]:
            result = helper(i+1,j+1)
        else:
            result = min(helper(i+1,j), helper(i,j+1), helper(i+1,j+1))
            result += 1
        memo[i][j] = result
        return result
    return helper(0,0)

print(solution("kitten","sittings"))
