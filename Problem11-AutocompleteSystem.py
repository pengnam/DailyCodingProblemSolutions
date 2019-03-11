"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
"""

"""
Considerations:
    1. Intuitively, an edge case is when the word is the only remaining word in the branch. However, there are other base cases.
    1. Some words are prefixes for other words, hence an edge case should be when the length of the word is 0 or when there is only one val left
"""
from collections import defaultdict
def solution(s, queries):
    tree =  build_tree(queries)
    ptr = tree
    for c in s:
        if type(ptr) != dict:
            return s if ptr.startswith(s) else None

        if c not in ptr:
            return None
        else:
            ptr = ptr[c]
    #Either reached the end (exact match between prefix and remaining word) or there are multiple matches
    result = []
    def retrieve(node):
        if type(node) == str:
            result.append(node)
        else:
            for key, val in node.items():
                retrieve(val)
    retrieve(ptr)
    return result





def build_tree(vals, level=0):
    if len(vals) <= 1:
        return vals[0]
    pointers = {}
    container = defaultdict(list)


    for val in vals:
        if level < len(val):
            container[val[level]].append(val)
        else:
            #There should only be 1 such value
            container[""].append(val)

    for key, elements in container.items():
        pointers[key] = build_tree(elements, level = level+1)
    return pointers


A = solution("dea", ["dear", "deed", "dead", "dea"])
import pdb;pdb.set_trace()




