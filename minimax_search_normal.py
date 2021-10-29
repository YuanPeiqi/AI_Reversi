import copy
import random
import time
import numpy as np

infinity = 2147483647
COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]


weight = [[-500, 50, -100, -30, -30, -100, 50, -500],
          [50, 100, -10, -5, -5, -10, 100, 50],
          [-100, -10, -5, 3, 3, -5, -10, -100],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-100, -10, -5, 3, 3, -5, -10, -100],
          [50, 100, -10, -5, -5, -10, 100, 50],
          [-500, 50, -100, -30, -30, -100, 50, -500]]
# weight = [[1 for i in range(8)] for j in range(8)]


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


# 找到当前所有合法位置
def find_valid_position(chessboard, color):
    candidate_list = []
    idx_none = np.where(chessboard == COLOR_NONE)
    idx_none = list(zip(idx_none[0], idx_none[1]))
    for pos_none in idx_none:
        if search(pos_none[0], pos_none[1], chessboard, color):
            candidate_list.append(pos_none)
    return candidate_list


# 棋子下在当前位置
def action(move, chessboard, current_color):
    chessboard[move[0]][move[1]] = current_color
    for i in range(8):
        r = move[0] + dr[i]
        c = move[1] + dc[i]
        flag = False
        while 8 > r >= 0 and 8 > c >= 0:
            if chessboard[r][c] == 0:
                flag = False
                break
            elif chessboard[r][c] == -current_color:
                flag = True
                r += dr[i]
                c += dc[i]
            else:
                break
        if flag and 8 > r >= 0 and 8 > c >= 0:
            r -= dr[i]
            c -= dc[i]
            while r != move[0] or c != move[1]:
                chessboard[r][c] = current_color
                r -= dr[i]
                c -= dc[i]


def stator_0(current_chessboard, color):
    if current_chessboard[0][0] != 0:
        weight[0][1] = -200
        weight[1][0] = -200
        weight[1][1] = -100
    if current_chessboard[7][0] != 0:
        weight[7][1] = -200
        weight[6][0] = -200
        weight[6][1] = -100
    if current_chessboard[0][7] != 0:
        weight[0][6] = -200
        weight[1][7] = -200
        weight[1][6] = -100
    if current_chessboard[7][7] != 0:
        weight[7][6] = -200
        weight[6][7] = -200
        weight[6][6] = -100


def alpha_beta_search(chessboard, color):
    def max_value(current_chessboard, current_candidate, depth, alpha, beta, current_color):
        stator_0(current_chessboard, color)
        if depth > 3:
            ret = 0
            for i in range(8):
                for j in range(8):
                    if color == COLOR_WHITE:
                        if current_chessboard[i][j] == COLOR_WHITE:
                            ret += weight[i][j]
                        elif current_chessboard[i][j] == COLOR_BLACK:
                            ret -= weight[i][j]
                    else:
                        if current_chessboard[i][j] == COLOR_WHITE:
                            ret -= weight[i][j]
                        elif current_chessboard[i][j] == COLOR_BLACK:
                            ret += weight[i][j]
            return ret, None
        v, move = -infinity, None
        if not current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            v2, _ = min_value(temp_chessboard, find_valid_position(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 > v:
                v, move = v2, None
            alpha = max(alpha, v)
            if alpha >= beta:
                return v, move
        for a in current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            action(a, temp_chessboard, current_color)
            v2, _ = min_value(temp_chessboard, find_valid_position(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 > v:
                v, move = v2, a
            alpha = max(alpha, v)
            if alpha >= beta:
                return v, move
        return v, move

    def min_value(current_chessboard, current_candidate, depth, alpha, beta, current_color):
        stator_0(current_chessboard, color)
        if depth > 3:
            ret = 0
            for i in range(8):
                for j in range(8):
                    if color == COLOR_WHITE:
                        if current_chessboard[i][j] == COLOR_WHITE:
                            ret += weight[i][j]
                        elif current_chessboard[i][j] == COLOR_BLACK:
                            ret -= weight[i][j]
                    else:
                        if current_chessboard[i][j] == COLOR_WHITE:
                            ret -= weight[i][j]
                        elif current_chessboard[i][j] == COLOR_BLACK:
                            ret += weight[i][j]
            return ret, None
        v, move = infinity, None
        if not current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            v2, _ = max_value(temp_chessboard, find_valid_position(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 < v:
                v, move = v2, None
            beta = min(beta, v)
            if beta <= alpha:
                return v, move
        for a in current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            action(a, temp_chessboard, current_color)
            v2, _ = max_value(temp_chessboard, find_valid_position(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 < v:
                v, move = v2, a
            beta = min(beta, v)
            if beta <= alpha:
                return v, move
        return v, move

    return max_value(chessboard, find_valid_position(chessboard, color), 0, -infinity, +infinity, color)


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

    # alpha_beta_1
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        start_time = time.perf_counter()
        self.candidate_list.clear()
        self.candidate_list = find_valid_position(chessboard, self.color)
        _, move = alpha_beta_search(chessboard, self.color)
        if move is not None:
            self.candidate_list.remove(move)
            self.candidate_list.append(move)
        time_elapsed = time.perf_counter()-start_time
        print("Normal total time is: " + str(time_elapsed) + "s")
        return self.candidate_list
