import copy
import random
import numpy as np

infinity = 2147483647
COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
weight = [[-500, 70, -30, 30, 30, -30, 70, -500],
          [70, 150, -10, -5, -5, -10, 150, 70],
          [-30, -10, -5, 10, 10, -5, -10, -30],
          [30, -5, 10, 1, 1, 10, -5, 30],
          [30, -5, 10, 1, 1, 10, -5, 30],
          [-30, -10, -5, 10, 10, -5, -10, -30],
          [70, 150, -10, -5, -5, -10, 150, 70],
          [-500, 70, -30, 30, 30, -30, 70, -500]]


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


def stator(current_chessboard, color):
    if current_chessboard[0][0] == color:
        weight[0][1] = -200
        weight[1][0] = -200
        weight[1][1] = -100
        weight[0][3] = -50
        weight[0][4] = -30
        weight[3][0] = -50
        weight[4][0] = -30
    if current_chessboard[7][0] == color:
        weight[7][1] = -200
        weight[6][0] = -200
        weight[6][1] = -100
        weight[4][0] = -50
        weight[3][0] = -30
        weight[7][3] = -50
        weight[7][4] = -30
    if current_chessboard[0][7] == color:
        weight[0][6] = -200
        weight[1][7] = -200
        weight[1][6] = -100
        weight[0][4] = -50
        weight[0][3] = -30
        weight[3][7] = -50
        weight[4][7] = -30
    if current_chessboard[7][7] == color:
        weight[7][6] = -200
        weight[6][7] = -200
        weight[6][6] = -100
        weight[7][4] = -50
        weight[7][3] = -30
        weight[4][7] = -50
        weight[3][7] = -30


def alpha_beta_search(chessboard, color):
    def max_value(current_chessboard, current_candidate, depth, alpha, beta, current_color):
        stator(current_chessboard, color)
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
        stator(current_chessboard, color)
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


# def alpha_beta(depth, chessboard, my_turn, current_color, alpha, beta, cnt, my_color):
#     if chessboard[0][0] != 0:
#         weight[0][1] = -200
#         weight[1][0] = -200
#         weight[1][1] = -100
#     if chessboard[7][0] != 0:
#         weight[7][1] = -200
#         weight[6][0] = -200
#         weight[6][1] = -100
#     if chessboard[0][7] != 0:
#         weight[0][6] = -200
#         weight[1][7] = -200
#         weight[1][6] = -100
#     if chessboard[7][7] != 0:
#         weight[7][6] = -200
#         weight[6][7] = -200
#         weight[6][6] = -100
#     if depth > 5 or cnt > 60:
#         utility = 0
#         for i in range(8):
#             for j in range(8):
#                 if my_color == COLOR_WHITE:
#                     utility += weight[i][j] * chessboard[i][j]
#                 else:
#                     utility -= weight[i][j] * chessboard[i][j]
#         return utility, (-1, -1)
#     ans = (-1, -1)
#     temp = copy.deepcopy(chessboard)
#     total = 0
#     if my_turn:
#         for pos in range(64):
#             pos_x = int(pos / 8)
#             pos_y = pos % 8
#             if chessboard[pos_x][pos_y] == COLOR_NONE:
#                 flag = False
#                 for k in range(8):
#                     t = 0
#                     x = pos_x + dr[k]
#                     y = pos_y + dc[k]
#                     if 0 <= x <= 7 and 0 <= y <= 7:
#                         while chessboard[x][y] == -current_color:
#                             t += 1
#                             x += dr[k]
#                             y += dc[k]
#                             if x > 7 or y > 7 or x < 0 or y < 0:
#                                 break
#                     if 0 <= x <= 7 and 0 <= y <= 7:
#                         if t != 0 and chessboard[x][y] == current_color:
#                             while True:
#                                 x -= dr[k]
#                                 y -= dc[k]
#                                 chessboard[x][y] = current_color
#                                 if x == pos_x and y == pos_y:
#                                     break
#                             flag = True
#                 if flag:
#                     total += 1
#                     v, _ = alpha_beta(depth + 1, chessboard, my_turn ^ 1, -current_color, alpha, beta, cnt + 1,
#                                       my_color)
#                     if v > alpha:
#                         if depth == 0:
#                             ans = (pos_x, pos_y)
#                         alpha = v
#                     chessboard = copy.deepcopy(temp)
#                     if beta <= alpha:
#                         break
#
#     if not total:
#         my_turn = 0
#     if not my_turn:
#         for pos in range(64):
#             pos_x = int(pos / 8)
#             pos_y = pos % 8
#             if chessboard[pos_x][pos_y] == COLOR_NONE:
#                 flag = False
#                 for k in range(8):
#                     t = 0
#                     x = pos_x + dr[k]
#                     y = pos_y + dc[k]
#                     if 0 <= x <= 7 and 0 <= y <= 7:
#                         while chessboard[x][y] == -current_color:
#                             t += 1
#                             x += dr[k]
#                             y += dc[k]
#                             if x > 7 or y > 7 or x < 0 or y < 0:
#                                 break
#                     if 0 <= x <= 7 and 0 <= y <= 7:
#                         if t != 0 and chessboard[x][y] == current_color:
#                             while True:
#                                 x -= dr[k]
#                                 y -= dc[k]
#                                 chessboard[x][y] = current_color
#                                 if x == pos_x and y == pos_y:
#                                     break
#                             flag = True
#                 if flag:
#                     v, _ = alpha_beta(depth + 1, chessboard, my_turn ^ 1, -current_color, alpha, beta, cnt + 1,
#                                       my_color)
#                     if beta > v:
#                         beta = v
#                     chessboard = copy.deepcopy(temp)
#                     if beta <= alpha:
#                         break
#     if my_turn:
#         return alpha, ans
#     else:
#         return beta, ans


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

    # alpha_beta_0
    # def go(self, chessboard):
    #     # Clear candidate_list, must do this step
    #     self.candidate_list.clear()
    #     self.candidate_list = find_valid_position(chessboard, self.color)
    #     idx_none = np.where(chessboard == COLOR_NONE)
    #     idx_none = list(zip(idx_none[0], idx_none[1]))
    #     num = len(idx_none)
    #     _, move = alpha_beta(0, chessboard, 1, self.color, -1000000000, 1000000000, 64 - num, self.color)
    #     if move != (-1, -1):
    #         # self.candidate_list.remove(move)
    #         self.candidate_list.append(move)
    #         self.candidate_list.append(move)
    #         self.candidate_list.append(move)
    #     return self.candidate_list

    # alpha_beta_1
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        self.candidate_list = find_valid_position(chessboard, self.color)
        _, move = alpha_beta_search(chessboard, self.color)
        if move is not None:
            self.candidate_list.remove(move)
            self.candidate_list.append(move)
        return self.candidate_list

# if __name__ == "__main__":
# my_ai_b = AI(8, -1, 10)
# print(my_ai_b.go(np.array(
#     [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0, 0, 0], [0, 0, 0, 1, -1, 0, 0, 0],
#      [0, 0, 0, -1, -1, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])))
# print(my_ai_b.go(np.array(
#     [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 0, -1, -1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0],
#      [0, 1, -1, -1, 1, 0, 0, 0], [0, -1, -1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])))

# my_ai_w = AI(8, 1, 10)
# stator([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 1, 1, -1, 1, 1],
#         [0, 0, 1, 1, -1, 1, -1, 0], [0, 0, 1, -1, -1, -1, 0, 0], [-1, -1, -1, -1, -1, -1, 0, 0],
#         [1, -1, 0, 0, -1, 0, 0, 0]], 1)
# for item in weight:
#     print(item)
# print(weight)
# print(my_ai_w.go(np.array(
#     [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 1, 1, -1, 1, 1],
#      [0, 0, 1, 1, -1, 1, -1, 0], [0, 0, 1, -1, -1, -1, 0, 0], [-1, -1, -1, -1, -1, -1, 0, 0],
#      [0, -1, 0, 0, -1, 0, 0, 0]])))
# print(my_ai_b.go(np.array(
#     [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, -1, 0],
#      [0, 0, -1, -1, -1, -1, 1, -1], [0, 0, 0, 1, 1, 0, -1, -1], [0, 0, 1, 1, 1, 1, 1, -1],
#      [0, 1, 1, 1, 1, 1, 1, -1]])))
