def solution(array):
    n = len(array)
    result = [1] * n
    left_product = array[0]
    for i in range(1,n):
        result[i] = left_product * result[i]
        left_product = left_product * array[i]
    right_product = array[-1]
    for i in range(n-2,-1, -1):
        result[i] = right_product * result[i]
        right_product = array[i] * right_product
    return result


print(solution([1,2,3,4,5]))
print(solution([2]))
#Base cases:
#1 element, 0 element
