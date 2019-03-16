from collections import defaultdict
def solution(s, k):
    seen = defaultdict(int)
    n = len(s)
    b = 0
    longest = 0
    distinct = 0
    """
    abcdefghi
     |     |
     b     i
     b and i inclusive
     hence, length is i - b + 1
    """
    for i in range(n):
        c = s[i]
        if seen[c] == 0:
            distinct += 1
        seen[c] += 1
        while distinct > k:
            import pdb;pdb.set_trace()
            to_remove = s[b]
            seen[to_remove] -= 1
            if seen[to_remove] == 0:
                distinct -= 1
            b += 1

        longest = max(longest, i - b + 1)
    return longest


print(solution("abcba", 2))
