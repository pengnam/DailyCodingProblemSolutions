import copy
from collections import defaultdict
def solution(flights, starting):
    if not flights:
        return [starting]
    #Preprocessing:
    #Process graph

    adj_graph = defaultdict(list)

    for s,e in flights:
        adj_graph[s].append(e)

    for l in adj_graph.values():
        l.sort()
    import pdb;pdb.set_trace()
    def empty(g):
        for v in g.values():
            if v:
                return False
        return True

    def helper(start, current_graph):
        if empty(current_graph):
            return [start]
        for next_dest in adj_graph[start]:
            new_d = copy.deepcopy(current_graph)
            new_d[start].remove(next_dest)
            partial = helper(next_dest, new_d)
            if partial:
                return [start] + partial
        return None
    return helper(starting, adj_graph)





print(solution([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))






