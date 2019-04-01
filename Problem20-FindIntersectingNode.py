"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
#Edge cases: no intersecting -> return null
#Assume no intersecting
"""
def solution(A, B):
    def invert(node):
        if not node:
            return node
        if not node.next_node:
            return node
        else:
            val = node.next_node
            result = invert(val)
            val.next_node = node
            return result
    A = invert(A)
    #B = invert(B)

    while A.val == B.val:
        A = A.next_node
        B = B.next_node

    return A.val


#Failed as after inverting the first node, its difficult to invert the next node
"""
class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

def solution(A,B):
    while  A:
        A.visited = True
        A = A.next_node
    while  B:
        if hasattr(B,'visited'):
            return B.val
        B = B.next_node
common = Node(8,Node(10))

A = Node(3,Node(7,common))
B = Node(99, Node(1, common))
print(solution(A,B))
