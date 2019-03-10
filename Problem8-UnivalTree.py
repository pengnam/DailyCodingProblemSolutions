"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.


"""
def solution(node):
    def helper(node):
        if node == None:
            return 0, False
        nodeLeft = None
        nodeRight = None
        result = 0
        if node.left:
            count, nodeLeft = helper(node.left)
            result += count
        if node.right:
            count, nodeRight = helper(node.right)
            result += count
        if nodeLeft and nodeRight:

            unival = node.left.val == node.val and node.right.val == node.val
            if unival:
                result += 1

            return result, unival
        elif nodeLeft:
            return result, node.left.val == node.val
        elif nodeRight:
            return result, node.right.val == node.val
        elif nodeLeft == False and nodeRight == False:
            return result, False
        else:
            return 1, True
    result, _ = helper(node)

    return result

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


result = Node(0)
result.left = Node(1)
result.right = Node(0)
result.right.left = Node(1)
result.right.left.left = Node(1)
result.right.left.right= Node(1)
result.right.right = Node(0)

print(solution(result))




