import heapq
def solution(array):
    smaller_half = []
    larger_half = []
    #Handle if either equals the other
    results = []
    for num in array:
        if smaller_half:
            if -smaller_half[0] >= num:
                heapq.heappush(smaller_half, -num)
            else:
                heapq.heappush(larger_half, num)
        elif larger_half:
            if larger_half[0] <= num:
                heapq.heappush(larger_half, num)
            else:
                heapq.heappush(smaller_half, -num)
        else:
            heapq.heappush(smaller_half, -num)

        # Balancing
        if len(smaller_half) >= 2+len(larger_half):
            heapq.heappush(larger_half, -heapq.heappop(smaller_half))
        elif len(larger_half) >= 2 + len(smaller_half):
            heapq.heappush(smaller_half, -heapq.heappop(larger_half))
        print(smaller_half)
        print(larger_half)
        #import pdb;pdb.set_trace()

        #Get result
        if len(smaller_half) == 1 + len(larger_half):
            median = -smaller_half[0]
        elif len(larger_half) == 1 + len(smaller_half):
            median = larger_half[0]
        else:
            median = (-smaller_half[0] + larger_half[0]) / 2
        results.append(median)
    return results

print(solution([2, 1, 5, 7, 2, 0, 5]))





