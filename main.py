import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)


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
        idx_white = np.where(chessboard == COLOR_WHITE)
        idx_black = np.where(chessboard == COLOR_BLACK)
        idx_none = list(zip(idx_none[0], idx_none[1]))
        idx_white = list(zip(idx_white[0], idx_white[1]))
        idx_black = list(zip(idx_black[0], idx_black[1]))
        for pos_none in idx_none:
            # 白色棋子
            if self.color == COLOR_WHITE:
                for pos_white in idx_white:
                    flag = False
                    if pos_white[0] == pos_none[0]:
                        start = min(pos_white[0], pos_none[0])
                        check = True
                        # 当前位置与当前白色棋子相邻，不合法
                        if abs(pos_white[1] - pos_none[1]) == 1:
                            check = False
                        # 当前位置与当前白色棋子中间有不为黑色的棋格，不合法
                        for i in range(1, abs(pos_white[1] - pos_none[1])):
                            if chessboard[pos_none[0]][start + i] != COLOR_BLACK:
                                check = False
                                break
                        # 如果当前白色棋子合法，则当前位置合法
                        if check:
                            flag = True

                    elif pos_white[1] == pos_none[1]:
                        start = min(pos_white[1], pos_none[1])
                        check = True
                        # 当前位置与当前白色棋子相邻，不合法
                        if abs(pos_white[0] - pos_none[0]) == 1:
                            check = False
                        # 当前位置与当前白色棋子中间有不为黑色的棋格，不合法
                        for i in range(1, abs(pos_white[0] - pos_none[0])):
                            if chessboard[start + i][pos_none[1]] != COLOR_BLACK:
                                check = False
                                break
                        # 如果当前白色棋子合法，则当前位置合法
                        if check:
                            flag = True

                    elif abs(pos_white[0] - pos_none[0]) == abs(pos_white[1] - pos_none[1]):
                        x = (pos_none[0] - pos_white[0]) / abs(pos_none[0] - pos_white[0])
                        y = (pos_none[1] - pos_white[1]) / abs(pos_none[1] - pos_white[1])
                        start_x = pos_white[0]
                        start_y = pos_white[1]
                        check = True
                        # 当前位置与当前白色棋子相邻，不合法
                        if abs(pos_white[0] - pos_none[0]) == 1:
                            check = False
                        # 当前位置与当前白色棋子中间有不为黑色的棋格，不合法
                        for _ in range(1, abs(pos_white[0] - pos_none[0])):
                            start_x = start_x + x
                            start_y = start_y + y
                            if chessboard[start_x][start_y] != COLOR_BLACK:
                                check = False
                                break
                        # 如果当前白色棋子合法，则当前位置合法
                        if check:
                            flag = True
                    # 如果有白棋子可以使当前位置合法，则加入list
                    if flag:
                        self.candidate_list.append(pos_none)
                        break
            else:
                for pos_black in idx_black:
                    flag = False
                    if pos_black[0] == pos_none[0]:
                        start = min(pos_black[0], pos_none[0])
                        check = True
                        # 当前位置与当前白色棋子相邻，不合法
                        if abs(pos_black[1] - pos_none[1]) == 1:
                            check = False
                        # 当前位置与当前白色棋子中间有不为黑色的棋格，不合法
                        for i in range(1, abs(pos_black[1] - pos_none[1])):
                            if chessboard[pos_none[0]][start + i] != COLOR_WHITE:
                                check = False
                                break
                        # 如果当前白色棋子合法，则当前位置合法
                        if check:
                            flag = True

                    elif pos_black[1] == pos_none[1]:
                        start = min(pos_black[1], pos_none[1])
                        check = True
                        # 当前位置与当前白色棋子相邻，不合法
                        if abs(pos_black[0] - pos_none[0]) == 1:
                            check = False
                        # 当前位置与当前白色棋子中间有不为黑色的棋格，不合法
                        for i in range(1, abs(pos_black[0] - pos_none[0])):
                            if chessboard[start + i][pos_none[1]] != COLOR_WHITE:
                                check = False
                                break
                        # 如果当前白色棋子合法，则当前位置合法
                        if check:
                            flag = True

                    elif abs(pos_black[0] - pos_none[0]) == abs(pos_black[1] - pos_none[1]):
                        x = (pos_none[0] - pos_black[0]) / abs(pos_none[0] - pos_black[0])
                        y = (pos_none[1] - pos_black[1]) / abs(pos_none[1] - pos_black[1])
                        start_x = pos_black[0]
                        start_y = pos_black[1]
                        check = True
                        # 当前位置与当前白色棋子相邻，不合法
                        if abs(pos_black[0] - pos_none[0]) == 1:
                            check = False
                        # 当前位置与当前白色棋子中间有不为黑色的棋格，不合法
                        for _ in range(1, abs(pos_black[0] - pos_none[0])):
                            start_x = start_x + x
                            start_y = start_y + y
                            if chessboard[start_x][start_y] != COLOR_WHITE:
                                check = False
                                break
                        # 如果当前白色棋子合法，则当前位置合法
                        if check:
                            flag = True
                    # 如果有白棋子可以使当前位置合法，则加入list
                    if flag:
                        self.candidate_list.append(pos_none)
                        break

        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, the system will return error.
        # Add your decision into candidate_list, Records the chess board
        # You need add all the positions which is valid
        # candidate_list example: [(3,3),(4,4)]
        # You need append your decision at the end of the candidate_list,
        # we will choice the last element of the candidate_list as the position you choose
        # If there is no valid position, you must return an empty list.
