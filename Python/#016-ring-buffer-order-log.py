"""
You run an e-commerce website and want to record the last N order ids
in a log. Implement a data structure to accomplish this, with the
following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed
to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

class OrderLog:

    def __init__(self, size: int):
        self.size = size
        self.log = [0] * size
        self.cur_index = 0

    def record(self, order_id: int):
        self.log[self.cur_index] = order_id
        self.cur_index = (self.cur_index + 1) % self.size

    def get_last(self, i: int):
        return self.log[(self.cur_index - i + self.size) % self.size]


if __name__ == '__main__':

    log = OrderLog(5)

    for num in range(5):
        log.record(num)

    assert log.cur_index == 0
    assert log.get_last(0) == 0
    assert log.get_last(1) == 4
