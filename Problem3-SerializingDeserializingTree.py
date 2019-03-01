class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    vals = []
    def encode(node):
        if isinstance(node, Node):
            vals.append(node.val)
            encode(node.left)
            encode(node.right)
        else:
            vals.append("#")
    encode(node)
    return " ".join(vals)

def deserialize(encoded_string):
    def decode(val_iterable):
        val = next(val_iterable)
        if val == "#":
            return None
        else:
            return Node(val, decode(val_iterable), decode(val_iterable))
    tokens = encoded_string.split(" ")
    token_iterable = iter(tokens)

    return decode(token_iterable)



#Problem integers become strings





node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
