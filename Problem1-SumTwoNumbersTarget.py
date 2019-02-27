"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
def solution(array, k):
    hold = set()
    for val in array:
        if k - val in hold:
            return True
        else:
            hold.add(val)
    return False


print(solution([10,15,3,7], 17))
print(solution([12,4,9,17], 2))

