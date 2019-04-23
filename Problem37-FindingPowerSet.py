def solution(array):
    result = [[]]
    for num in array:
        for i in range(len(result)):
            r = result[i]
            new_r = r.copy()
            new_r.append(num)
            result.append(new_r)
    return result


print(solution([1,2,3]))


