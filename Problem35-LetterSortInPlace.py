# Sorting values


def solution(array):
    #Iterate through order
    i = 0 #first unsorted position
    for t in ["R", "G"]:
        for j in range(i, len(array)):
            c = array[j]
            if c == t:
                array[i],array[j] = array[j], array[i]
                i += 1
    print(array)


print(solution(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
