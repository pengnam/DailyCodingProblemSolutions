"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
"""

from collections import deque
class Log:
    def __init__(self, N):
        self.count = 0
        self.N = N
        self.buf = deque()
    def record(self, order_id):
        self.buf.append(order_id)
        self.count += 1
        if self.count > self.N:
            self.buf.popleft()
            self.count -= 1
    def get_last(self, i):
        return self.buf[-i]

import pdb;pdb.set_trace()

