import numpy as np


a = [1]


class Position(object):
    def __init__(self, priority, pos):
        self.priority = priority
        self.pos = pos

    def __str__(self):
        return '(\'' + str(self.priority) + '\',' + str(self.pos) + ')'


position = Position(0, (0, 0))


def x():
    a[0] += 1


if __name__ == "__main__":
    print(a)
    x()
    print(a)
