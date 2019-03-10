"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""
#Observations:
#There are a limited amount of possible decodings, i.e. 1 - 26
#0 has to follow a 1
#Maximum of 2 contiguous integers are treated as a possible decoding

#Exhaustive search
#Number of ways to count integers from 1-26 from a sequence of integers
#O(2^n)

#But there are overlapping subtrees

def solution(message):
    n = len(message)
    memo = [0] * n
    if message[n-1] != "0":
        memo[n-1] = 1
    if n > 1 and 10 <= int(message[-2:]) <= 26:
        memo[n-2] = 1
    for i in range(n-1)[::-1]:
        #taking current element as a value
        if message[i] != "0":
            memo[i] += memo[i+1]
        #taking current element and previous element as values
        if i < n-2 and 10 <=int(message[i:i+2]) <=26:
            memo[i] += memo[i+2]
    return memo[0]


print(solution("111"))
print("Should be 3")
print(solution("210"))
print("Should be 1")
print(solution("77"))
print("Should be 1")

print(solution("1"))
print("Should be 1")

