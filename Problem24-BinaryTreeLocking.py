"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
"""


class BinaryTreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.locked = False

    def checkAncestorsHaveLock(self):
        curr = self.parent
        while curr:
            if curr.locked:
                return True
        return False
    def checkDecendentsHaveLock(self):
        #Should just use or
        result = False
        if not left:
            result = self.left.checkDescendentsHaveLock()
        if not result and not right:
            result = self.right.checkDescdentsHaveLock()
        return result
    def lock(self):
        if self.lock or self.checkAncestorsHaveLock()or self.checkDescendentsHaveLock():
            return False
        else:
            self.lock = True
            return True
    def unlock(self):
        if self.lock or self.checkAncestorsHaveLock()or self.checkDescendentsHaveLock():
            return False
        else:
            self.lock = False
            return True






