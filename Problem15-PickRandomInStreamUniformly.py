import random
"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
class Stream:
    def __init__(self):
        self.val = 0
        self.count = 0

    def next_val(self):
        return self.count
    def retrieve(self):
        self.count += 1
        next_val = self.next_val()
        if random.random() < float(1)/self.count:
            self.val = next_val
        return next_val

    def get_random_element(self):
        return self.val
if __name__ == "__main__":

    s = Stream()
    print("DONE")
    for _ in range(1000):
        print("here: ", s.retrieve())
        print(s.get_random_element())
