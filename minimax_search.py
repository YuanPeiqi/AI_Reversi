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
weight = [[-500, 30, -200, -30, -30, -200, 30, -500],
          [30, 50, -10, -5, -5, -10, 50, 30],
          [-200, -10, -5, 3, 3, -5, -10, -200],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-200, -10, -5, 3, 3, -5, -10, -200],
          [30, 50, -10, -5, -5, -10, 50, 30],
          [-500, 30, -50, -30, -30, -200, 30, -500]]


# weight = [[-500, -100, -200, -30, -30, -200, -100, -500],
#           [-100, -300, -10, -5, -5, -10, -300, -100],
#           [-200, -10, -5, -3, -3, -5, -10, -200],
#           [-30, -5, -3, 1, 1, -3, -5, -30],
#           [-30, -5, -3, 1, 1, -3, -5, -30],
#           [-200, -10, -5, -3, -3, -5, -10, -200],
#           [-100, -300, -10, -5, -5, -10, -300, -100],
#           [-500, -100, -50, -30, -30, -200, -100, -500]]


class Position(object):
    def __init__(self, priority, pos):
        self.priority = priority
        self.pos = pos

    def __str__(self):
        return '(\'' + str(self.priority) + '\',' + str(self.pos) + ')'


def sort(queue):
    list_return = []
    for item in queue:
        list_return.append(Position(weight[item[0]][item[1]], item))
    return sorted(list_return, key=lambda x: x.priority)


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


def find_valid_position(chessboard, color):
    candidate_list = []
    idx_none = np.where(chessboard == COLOR_NONE)
    idx_none = list(zip(idx_none[0], idx_none[1]))
    for pos_none in idx_none:
        if search(pos_none[0], pos_none[1], chessboard, color):
            candidate_list.append(pos_none)
    return candidate_list


# def alpha_beta_search(chessboard, candidate):
#     def max_value(current_chessboard, current_candidate, depth, alpha, beta):
#         if depth > 9:
#             ret = 0
#             for i in range(8):
#                 for j in range(8):
#                     ret += weight[i][j] * current_chessboard[i][j]
#             return ret, None
#         temp_chessboard = copy.deepcopy(chessboard)
#         v1, move = -infinity, None
#         for a in current_candidate:
#             v2, _ = min_value(temp_chessboard, state, depth+1, alpha, beta)
#             if v2 > v1:
#                 v1, move = v2, a
#                 alpha = max(alpha, v1)
#             if v1 >= beta:
#                 return v1, move
#         return v1, move
#
#     def min_value(state, alpha, beta):
#         if len(state) == 0:
#             return self.utility, None
#         v, move = infinity, None
#         for a in game.actions(state):
#             v2, _ = max_value(game.result(state, a), alpha, beta)
#             # TODO: update *v*, *move* and *beta*
#             if v2 < v:
#                 v, move = v2, a
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return v, move
#         return v, move
#     return max_value(candidate, -infinity, +infinity)


# def final_moves_utility(chessboard, my_color):
#     cnt_white = 0
#     cnt_black = 0
#     for i in range(8):
#         for j in range(8):
#             if chessboard[i][j] == COLOR_WHITE:
#                 if i == 0 and j == 0:
#                     cnt_white += 10
#                 cnt_white += 1
#             if chessboard[i][j] == COLOR_BLACK:
#                 if i == 0 and j == 0:
#                     cnt_black += 10
#                 cnt_black += 1
#     return (cnt_black - cnt_white) if my_color == COLOR_WHITE else (cnt_white - cnt_black)


def alpha_beta(depth, chessboard, my_turn, current_color, alpha, beta, cnt, my_color):
    if chessboard[0][0] != 0:
        weight[0][1] = -200
        weight[1][0] = -200
        weight[1][1] = -100
    if chessboard[7][0] != 0:
        weight[7][1] = -200
        weight[6][0] = -200
        weight[6][1] = -100
    if chessboard[0][7] != 0:
        weight[0][6] = -200
        weight[1][7] = -200
        weight[1][6] = -100
    if chessboard[7][7] != 0:
        weight[7][6] = -200
        weight[6][7] = -200
        weight[6][6] = -100
    if depth > 6 or cnt > 60:
        utility = 0
        for i in range(8):
            for j in range(8):
                if my_color == COLOR_WHITE:
                    utility += weight[i][j] * chessboard[i][j]
                else:
                    utility -= weight[i][j] * chessboard[i][j]
        return utility, (-1, -1)
    ans = (-1, -1)
    temp = copy.deepcopy(chessboard)
    total = 0
    if my_turn:
        for pos in range(64):
            pos_x = int(pos / 8)
            pos_y = pos % 8
            if chessboard[pos_x][pos_y] == COLOR_NONE:
                flag = False
                for k in range(8):
                    t = 0
                    x = pos_x + dr[k]
                    y = pos_y + dc[k]
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        while chessboard[x][y] == -current_color:
                            t += 1
                            x += dr[k]
                            y += dc[k]
                            if x > 7 or y > 7 or x < 0 or y < 0:
                                break
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        if t != 0 and chessboard[x][y] == current_color:
                            while True:
                                x -= dr[k]
                                y -= dc[k]
                                chessboard[x][y] = current_color
                                if x == pos_x and y == pos_y:
                                    break
                            flag = True
                if flag:
                    total += 1
                    v, _ = alpha_beta(depth + 1, chessboard, my_turn ^ 1, -current_color, alpha, beta, cnt + 1,
                                      my_color)
                    if v > alpha:
                        if depth == 0:
                            ans = (pos_x, pos_y)
                        alpha = v
                    chessboard = copy.deepcopy(temp)
                    if beta <= alpha:
                        break

    if not total:
        my_turn = 0
    if not my_turn:
        for pos in range(64):
            pos_x = int(pos / 8)
            pos_y = pos % 8
            if chessboard[pos_x][pos_y] == COLOR_NONE:
                flag = False
                for k in range(8):
                    t = 0
                    x = pos_x + dr[k]
                    y = pos_y + dc[k]
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        while chessboard[x][y] == -current_color:
                            t += 1
                            x += dr[k]
                            y += dc[k]
                            if x > 7 or y > 7 or x < 0 or y < 0:
                                break
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        if t != 0 and chessboard[x][y] == current_color:
                            while True:
                                x -= dr[k]
                                y -= dc[k]
                                chessboard[x][y] = current_color
                                if x == pos_x and y == pos_y:
                                    break
                            flag = True
                if flag:
                    v, _ = alpha_beta(depth + 1, chessboard, my_turn ^ 1, -current_color, alpha, beta, cnt + 1,
                                      my_color)
                    if beta > v:
                        beta = v
                    chessboard = copy.deepcopy(temp)
                    if beta <= alpha:
                        break
    if my_turn:
        return alpha, ans
    else:
        return beta, ans


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
        self.utility = 0

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        self.candidate_list = find_valid_position(chessboard, self.color)
        idx_none = np.where(chessboard == COLOR_NONE)
        idx_none = list(zip(idx_none[0], idx_none[1]))
        num = len(idx_none)
        _, move = alpha_beta(0, chessboard, 1, self.color, -1000000000, 1000000000, 64 - num, self.color)
        if move != (-1, -1):
            # self.candidate_list.remove(move)
            self.candidate_list.append(move)
            self.candidate_list.append(move)
            self.candidate_list.append(move)
        return self.candidate_list
        # if self.candidate_list:
        #     index = np.random.randint(0, 10, size=1)
        #     self.candidate_list.append(self.candidate_list[index[0]])
        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, the system will return error.
        # Add your decision into candidate_list, Records the chess board
        # You need add all the positions which is valid
        # candidate_list example: [(3,3),(4,4)]
        # You need append your decision at the end of the candidate_list,
        # we will choice the last element of the candidate_list as the position you choose
        # If there is no valid position, you must return an empty list.


if __name__ == "__main__":
    my_ai_b = AI(8, -1, 10)
    print(my_ai_b.go(np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 1, -1, 1, -1, 0, 1],
         [0, 1, -1, -1, 1, -1, -1, 0]])))
    my_ai_w = AI(8, 1, 10)
    print(my_ai_w.go(np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 1, 1, 1, -1, 0],
         [0, 0, 0, -1, 1, 0, -1, 0], [0, 0, 0, 0, -1, 0, -1, 1], [0, 0, 1, 1, 1, -1, -1, -1],
         [0, 0, -1, 0, -1, 1, -1, 0]])))
    print(my_ai_b.go(np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, -1, 0],
         [0, 0, -1, -1, -1, -1, 1, -1], [0, 0, 0, 1, 1, 0, -1, -1], [0, 0, 1, 1, 1, 1, 1, -1], [0, 1, 1, 1, 1, 1, 1, -1]])))
