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
            if self.color == COLOR_WHITE:
                if (pos_none[0] + 1, pos_none[1]) not in idx_black:
                    print()

        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, the system will return error.
        # Add your decision into candidate_list, Records the chess board
        # You need add all the positions which is valid
        # candidate_list example: [(3,3),(4,4)]
        # You need append your decision at the end of the candidate_list,
        # we will choice the last element of the candidate_list as the position you choose
        # If there is no valid position, you must return an empty list.
