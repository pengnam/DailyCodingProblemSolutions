"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

"""

1 - 2 - 3 - 4 - 5

if k == 4:
    1 - 3 - 4- 5

"""


def solution(node, k):
    before_k = node
    before_end = node
    for _ in range(k):
        before_k = before_k.next

    while not before_end.next:
        before_end = before_end.next
        before_k = before_k.next

    before_k.next = before_k.next.next
    return node



class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        string = "["
        node = self
        while node:
            string += "{} ->".format(node.val)
            node = node.next
        string += "None]"
        return string


def get_nodes(values):
    next_node = None
    for value in values[::-1]:
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node


def get_list(head):
    node = head
    nodes = list()
    while node:
        nodes.append(node.val)
        node = node.next
    return nodes
assert get_list(solution(
    get_nodes([0, 3, 7, 8, 10]), 2)) == [0, 3, 7, 10]
assert get_list(solution(
    get_nodes([7, 8, 10]), 1)) == [7, 8]
