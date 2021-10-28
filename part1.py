from filecmp import cmp
import heapq
import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
weight = [[-90, 60, -20, -10, -10, -20, 60, -90],
          [60, 80, -10, -5, -5, -10, 80, 60],
          [-20, -10, -5, -3, -3, -5, -10, -20],
          [-10, -5, -3, 1, 1, -3, -5, -10],
          [-10, -5, -3, 1, 1, -3, -5, -10],
          [-20, -10, -5, -3, -3, -5, -10, -20],
          [60, 80, -10, -5, -5, -10, 80, 60],
          [-90, 60, -20, -10, -10, -20, 60, -90]]


class Position(object):
    def __init__(self, priority, pos):
        self.priority = priority
        self.pos = pos

    def __lt__(self, other):  # operator <
        return self.priority < other.priority

    def __ge__(self, other):  # operator >=
        return self.priority >= other.priority

    def __le__(self, other):  # operator <=
        return self.priority <= other.priority

    def __cmp__(self, other):
        # call global(builtin) function cmp for int
        return cmp(self.priority, other.priority)

    def __str__(self):
        return '(\'' + str(self.priority) + '\',' + str(self.pos) + ')'


def sort(queue):
    heap = []
    for item in queue:
        heapq.heappush(heap, Position(weight[item[0]][item[1]], item))
    list_return = []
    while heap:
        list_return.append(heapq.heappop(heap).pos)
    return list_return


def search(row, col, chessboard, current_color):
    flag = False
    for i in range(8):
        r = row + dr[i]
        c = col + dc[i]
        if 8 > r >= 0 and 8 > c >= 0:
            if chessboard[r][c] == -current_color:
                flag = nextSearch(r, c, i, chessboard, current_color)
        if flag:
            return True
    return False


def nextSearch(r, c, i, chessboard, current_color):
    if 8 > r + dr[i] >= 0 and 8 > c + dc[i] >= 0:
        r = r + dr[i]
        c = c + dc[i]
        if chessboard[r][c] == -current_color:
            return nextSearch(r, c, i, chessboard, current_color)
        elif chessboard[r][c] == current_color:
            return True
        else:
            return False


# don't change the class name
class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
        self.candidate_list = []

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        # ==================================================================
        # Write your algorithm here
        # Here is the simplest sample:Random decision
        idx_none = np.where(chessboard == COLOR_NONE)
        idx_none = list(zip(idx_none[0], idx_none[1]))
        for pos_none in idx_none:
            if search(pos_none[0], pos_none[1], chessboard, self.color):
                self.candidate_list.append(pos_none)
        self.candidate_list = sort(self.candidate_list)
        # if self.candidate_list:
        #     index = np.random.randint(0, 10, size=1)
        #     self.candidate_list.append(self.candidate_list[index[0]])
        return self.candidate_list
        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, the system will return error.
        # Add your decision into candidate_list, Records the chess board
        # You need add all the positions which is valid
        # candidate_list example: [(3,3),(4,4)]
        # You need append your decision at the end of the candidate_list,
        # we will choice the last element of the candidate_list as the position you choose
        # If there is no valid position, you must return an empty list.
