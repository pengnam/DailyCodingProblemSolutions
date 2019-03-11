class Node:
    def __init__(self, val):
        self.val = val
    def append(self, next_node):
        #assumption: called only once
        self.both = next_node.get_pointer() ^ self.both
    def get(self, prev):
        return self.both ^ prev


class LinkedList:
    def __init__(self):
        self.start = None
    def add(self, element):
        if not self.start:
            self.start = get_pointer(element)
            self.end = self.start

        dereference_pointer(self.end).append(element)
        self.end = get_pointer(element)

    def get(self, index):
        current = self.start
        for i in range(index):
            current = dereference_pointer(self.start).get(current)
        return current

# Edge case not handled: if get is pass the index
