from collections import defaultdict
"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""

#Edge case: 1 word is a subset of the other
def solution(words, string):
    #Build a trie

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

    #Construct words

    tree = build_tree(words)
    import pdb;pdb.set_trace()
    ptr = tree
    for c in string:
        if c not in ptr:
            return None
        ptr = ptr[c]
        if type(ptr) == str:
            return ptr


print(solution(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond'))
