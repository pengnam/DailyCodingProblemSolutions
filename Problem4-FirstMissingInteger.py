def solution(array):
    n = len(array)
    for i in range(n):
        if 0 < array[i] <= n:
            ptr = array[i] - 1
            while  0 <= ptr < n and array[ptr] != ptr+1:
                next_ptr = array[ptr] - 1
                array[ptr] = ptr+1
                if (0 <= next_ptr < n):
                    ptr = next_ptr
                else:
                    break
        else:
            array[i] = -1
    for i in range(n):
        if array[i] != i+1:
            return i + 1
assert solution([3, 4, -1, 1]) == 2
assert solution([1, 2, 0]) == 3

