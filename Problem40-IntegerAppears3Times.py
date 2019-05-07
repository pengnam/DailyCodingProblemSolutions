def solution(array):
    val = 0
    holder = [0] * len(array)
    for a in array:
        val = val ^ a

        for i, c in enumerate(reversed(bin(val)[2:])):
            holder[len(array)-i] += int(c)
            print(val)

solution([1,2,20])




