def solution(node):
    # Edge case: Can I assume the size of tree > 1
    # 1. Traverse to find the largest, inorder predecessor
    # 2. Keep a second pointer

    #If there isn't a ptr on the right, means the head node is the largest, one on left will be the largest
    if not node:
        return None
    elif node.right:
        second_largest = node
        ptr = node.right
        while ptr.right:
            second_largest = second_largest.right
            ptr = ptr.right

        if ptr.left:
            second_largest = ptr.left
            while second_largest.right:
                second_largest = second_largest.right
        return second_largest
    elif node.left:
        #Iterate to the end of this as well
        result = node.left
        while result.right:
            result = result.right
        return result
    return None


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "< " + str(self.val) + " >"

def main():
    """
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
    """
    BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    print(solution(BST))


    """
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
    """
    BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14)))
    print(solution(BST))

    """
        8
       /
      3
     / \
    1   6
       / \
      4   7
    """
    BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))))
    print(solution(BST))

if __name__ == "__main__":
    main()

