# **![LOGO](C:\Users\Administrator\Desktop\校徽+中英文火炬\组合4：火炬+英文校名-左右\LOGO.png)Reversed-Reversi**

<center>Project I Report of for</center>

<center>CS303 Artificial intelligence</center>

<center>Department of Computer Science and Engineering, SUSTech

<center>Peiqi YUAN

<center>11912526

















## **1. Preliminaries**

### 1.1 Background

Artificial intelligence is one of the most active research fields in recent years. Chess is an important branch of artificial intelligence research and with the development of game algorithms, more and more AI "chess players" have been created, such as AlphaGo. Reversi is a widespread and popular foreign board game. The game, which has simple and changeable rules, is full of interesting and recreational. Reversi is played by flipping each other's pieces between the piece you just played and any of your old pieces, and after the board is full filled, the player with more pieces left wins the game. Reversed-Reversi, the game in our project, has the same rules as Reversi except for the way to determine the winner, which is that fewer pieces in the end means victory. Although the game rules are simple, the amount of data in the search tree is extremely huge. The purpose of this project is to build a Reversed-Reversi artificial intelligence based on game algorithms, and make some adjustments and optimizations in order to be able to play against human players automatically and achieve a relatively high level of intelligence.

### 1.2 Software & Hardware

The programming language used in this project is ***Python* *(Version 3.8)*** with ***Anaconda3 (Version 5.3.1)*** and the editor is ***PyCharm Professional (Version 2020.3.2)***.

All coding and local experiments were conducted (with single thread) on a machine with an ***Intel® Core™ i5-9300H CPU @ x64 2.40GHz***, and ***8.00GB of RAM***. The operating system of the machine is *Windows 10 Home (Version 20H2)*.

Official online battle platform is deployed (with single thread) on a server with ***Intel® Xeon Gold 6240 CPU @ x64  2.60GHz***.

### 1.3 Algorithms

The core algorithm of this project consists of two parts, greedy algorithm and Minimax algorithm. Based on these two main algorithms, I constructed a series of dynamic evaluation functions of chess games situation, including the evaluation of action power (number of valid positions), dynamic evaluation of position value as well as evaluation of the early, middle and late stages of a chess game. In addition, in order to improve the computation efficiency, the project invokes Alpha-Beta pruning to speed up Minimax algorithm.

### 1.4 Application

###### Games:

Game AI is always a search problem, and Minimax algorithm is a basic game algorithm based on search. So the Minimax algorithm is commonly used in games and programs where two players take turns performing one step at a time, such as board games and card games. The well-known Gobang, Chinese chess and so on all belong to this kind of program. The algorithm is a zero-sum algorithm, in which one side chooses the one that maximizes its advantage among the alternatives, while the other side chooses the one that minimizes its opponent's advantage.



## **2. Methodology**

In this part, I will introduce some function notations and their usage as well as meaning of parameters. After that, I am going to replace my functions with these notations later on. Besides, I will also explain the design of some main functions and the details of their implementation. In addition, I will list some important data structures to to help you understand these functions easily.

### 2.1 Notations

- ```python
  W(x, y)
  ```

The function is to get the weight from the weight table (better game, higher weight, as shown in figure 1) for a specified position on the chessboard. The parameters are the horizontal and vertical coordinates of a chess grid.

![image-20211102173054441](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211102173054441.png)



- ```python
  find_valid_position(chessboard, color)
  ```

The function is an enumerating function to find all alternative position on the current chessboard for one side. The parameters are the current chessboard and the color of the piece to be queried.



- ```python
  action(move, chessboard, color)
  ```

The function is to invoke a move, flip opposing pieces and change the current chessboard. The parameters are the coordinate of a move, the current chessboard and the color of the piece.



- ```python
  utility(chessboard, color)
  ```

The function is to analyze the current utility of one side in the game and uitlity is a comprehensive evaluation index, compared with the weight. The parameters are the current chessboard and the color of the piece to be evaluated.



- ```
  stator(chessboard)
  ```

The function is to dynamically change the chessboard weights . The only parameter is the current chessboard.



- ```python
  alpha_beta_search(chessboard, color, depth)
  ```

The main function implements Minimax algorithm with the optimization of alpha-beta pruning. The parameters are the current chessboard, the color of the side which is going to have a move and the depth of the search tree.

### 2.2 Data Structure

- ###### **Candidate List:** 

  Implemented by **a priority queue** with weight first, the candidate_list is used to find the position having the highest weight.

- ###### **Chessboard:**

  Implemented by **an numpy array** with size 8 × 8, 0 represents empty position, 1 for white pieces and -1 for black pieces.

- ###### **Direction:**

  Implemented by **a two-dimension list** with size 2 × 8, every column in the list represents a direction. For example, (-1, 1) is the direction top left.

- ###### Weight Table:

  Implemented by **a two-dimension list** with size 8 × 8, every value in the table represents the weight of corresponding position.

- ###### Minimax Search Tree:

  The Minimax algorithm relies on **a game search tree**, but the tree doesn't actually exist. The structure is implemented by recursive DFS.

### 2.3 Model Design

- ```python
  find_valid_position(chessboard, color)
  ```

This function is to find all valid move in this round and will return a list of tuples. First of all, there are only empty places to drop the pieces, so we get all none positions. For a none position, the position is legal iff one of the eight directions satisfies that there is a piece with the same color in this direction and all the pieces between are opposing pieces. So I traverse each none place,and checking their eight directions. In this regard, I use the following two methods **`search(x,y)`** and **`nextSearch(x,y,direction,chessboard,color)`** for recursive judgment 

