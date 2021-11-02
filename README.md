# Reversed-Reversi

**Project 3 Report of**

**CS303 Artificial intelligence**

**Department of Computer Science and Engineering**

Southern University of Science and Technology

Peiqi YUAN

11912526

## **1. Preliminaries**

### 1.1 Background

Artificial intelligence is one of the most active research fields in recent years. Chess is an important branch of artificial intelligence research and with the development of game algorithms, more and more AI "chess players" have been created, such as AlphaGo. Reversi is a widespread and popular foreign board game. The game, which has simple and changeable rules, is full of interesting and recreational. Reversi is played by flipping each other's pieces between the piece you just played and any of your old pieces, and after the board is full filled, the player with more pieces left wins the game. Reversed-Reversi, the game in our project, has the same rules as Reversi except for the way to determine the winner, which is that fewer pieces in the end means victory. Although the game rules are simple, the amount of data in the search tree is extremely huge. The purpose of this project is to build a Reversed-Reversi artificial intelligence based on game algorithms, and make some adjustments and optimizations in order to be able to play against human players automatically and achieve a relatively high level of intelligence.

### 1.2 Technology

The programming language used in this project is *Python* *(Version 3.8)* with *Anaconda3 (Version 5.3.1)* and the editor is *PyCharm Professional (Version 2020.3.2)*.

All coding and local experiments were conducted (with single thread) on a machine with an *Intel® Core™ i5-9300H CPU @ x64 2.40GHz*, and *8.00GB of RAM*. The operating system of the machine is *Windows 10 Home (Version 20H2)*.

Official online battle platform is deployed (with single thread) on a server with *Intel® Xeon Gold 6240 CPU @ x64  2.60GHz*.

### 1.3 Algorithm

The core algorithm of this project consists of two parts, greedy algorithm and minimax algorithm. Based on these two main algorithms, I constructed a series of dynamic evaluation methods of chess games situation, including the evaluation of action power (number of valid positions), dynamic evaluation of position value as well as evaluation of the early, middle and late stages of a chess game. In addition, in order to improve the computation efficiency, the project invokes alpha-beta pruning to speed up minimax algorithm

Can computer chess, so that it can play against opponents. Visual C+ is used here

\+ 6.0 game design black and white procedures, the application of Alpha - Beta pruning and

Maxima minima principle to search the best position.
