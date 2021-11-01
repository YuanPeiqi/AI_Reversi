import numpy as np
import minimax_search_0 as my_ai
import minimax_search_normal as other_ai


dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]


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


def play_game_1():
    chessboard = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, -1, 0, 0, 0],
                           [0, 0, 0, -1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]])
    AI_myself = my_ai.AI(8, -1, 10)
    AI_other = other_ai.AI(8, 1, 10)
    cnt = 0
    black_list = AI_myself.go(chessboard)
    white_list = AI_other.go(chessboard)
    while black_list or white_list:
        # 偶数黑旗走
        if cnt % 2 == 0:
            if not black_list:
                cnt += 1
                continue
            black_move = black_list.pop()
            action(black_move, chessboard, -1)
            print(black_move)
        # 奇数白旗走
        if cnt % 2 == 1:
            if not white_list:
                cnt += 1
                continue
            white_move = white_list.pop()
            action(white_move, chessboard, 1)
            print(white_move)
        cnt += 1
        black_list = AI_myself.go(chessboard)
        white_list = AI_other.go(chessboard)
        print()
        print("Step: " + str(cnt))
        print("=========================================")
        for line in chessboard:
            string = ""
            print("-----------------------------------------")
            for chess in line:
                if chess == 1:
                    string += " ██ |"
                elif chess == -1:
                    string += " △ |"
                else:
                    string += "    |"
            print("|" + string)
        print("=========================================")

    white_cnt = 0
    black_cnt = 0
    for line in chessboard:
        string = ""
        print("-----------------------------------------")
        for chess in line:
            if chess == 1:
                string += " ██ |"
                white_cnt += 1
            elif chess == -1:
                string += " △ |"
                black_cnt += 1
            else:
                string += "    |"
        print("|" + string)
    print("=========================================")
    if white_cnt < black_cnt:
        return "My AI is black (△), the other AI is white (██)\nWhite Win!!!"
    elif white_cnt > black_cnt:
        return "My AI is black (△), the other AI is white (██)\nBlack Win!!!"
    else:
        return "My AI is black (△), the other AI is white (██)\nGame Draw"


def play_game_2():
    chessboard = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, -1, 0, 0, 0],
                           [0, 0, 0, -1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]])
    AI_myself = other_ai.AI(8, -1, 10)
    AI_other = my_ai.AI(8, 1, 10)
    cnt = 0
    black_list = AI_myself.go(chessboard)
    white_list = AI_other.go(chessboard)
    while black_list or white_list:
        # 偶数黑旗走
        if cnt % 2 == 0:
            if not black_list:
                cnt += 1
                continue
            black_move = black_list.pop()
            action(black_move, chessboard, -1)
            print(black_move)
        # 奇数白旗走
        if cnt % 2 == 1:
            if not white_list:
                cnt += 1
                continue
            white_move = white_list.pop()
            action(white_move, chessboard, 1)
            print(white_move)
        cnt += 1
        black_list = AI_myself.go(chessboard)
        white_list = AI_other.go(chessboard)
        print()
        print("Step: " + str(cnt))
        print("=========================================")
        for line in chessboard:
            string = ""
            print("-----------------------------------------")
            for chess in line:
                if chess == 1:
                    string += " ██ |"
                elif chess == -1:
                    string += " △ |"
                else:
                    string += "    |"
            print("|" + string)
        print("=========================================")

    white_cnt = 0
    black_cnt = 0
    for line in chessboard:
        string = ""
        print("-----------------------------------------")
        for chess in line:
            if chess == 1:
                string += " ██ |"
                white_cnt += 1
            elif chess == -1:
                string += " △ |"
                black_cnt += 1
            else:
                string += "    |"
        print("|" + string)
    print("=========================================")
    if white_cnt < black_cnt:
        return "My AI is white (██), the other AI is black (△)\nWhite Win!!!"
    elif white_cnt > black_cnt:
        return "My AI is white (██), the other AI is black (△)\nBlack Win!!!"
    else:
        return "My AI is white (██), the other AI is black (△)\nGame Draw"


if __name__ == "__main__":
    game1 = play_game_1()
    game2 = play_game_2()
    print(game1)
    print(game2)
