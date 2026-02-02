# 4InALine AI bot

Connect Four AI Trainer

This is a Python-based Connect Four implementation with a simple reinforcement learning AI. The program allows two AI agents to train against each other and learn optimal moves over time, and also lets a human play against the AI.

Features

Board Representation:
The game board is represented as a list of 7 columns, each holding the pieces stacked as strings. Each column can hold up to 6 pieces.

AI Training:
Two bots (Bot and Bot2) play against each other to improve their strategy using a Q-learning approach.

qTable stores the AI's learned values for player 1.

qTable0 stores the AI's learned values for player 0.

The AI chooses moves based on exploration vs. exploitation (e value).

Win Checking:
The game detects victories in four ways:

Vertical

Horizontal

Diagonal (up-right and down-right)

Draw Checking:
Detects when all columns are full, resulting in a draw.

Human vs AI:
After training, a human can play against the AI in the console.

State Encoding:
The board is encoded into a fixed-length string for use in the Q-learning tables. Empty spaces are represented by "9".

How to Run

Clone or download the repository.

Make sure you have Python 3 installed.

Run the script in your terminal:

python connect_four_ai.py


The AI will train against itself for a number of laps. After training, you can play against the AI by entering column numbers (0–6).

Functions Overview

BuildBoard() – Initializes an empty board and resets the current player.

PrintBoard(board) – Prints the current board state in a readable format.

DropPiece(col) – Drops the current player’s piece into the specified column.

CheckWinVertically(col), CheckWinHorizontally(row), CheckWinDiagonallyUp(col,row), CheckWinDiagonallyDown(col,row) – Check for winning conditions.

CheckWinsOverall(col,row) – Combines all win checks.

CheckDraw(grid) – Checks if the game ended in a draw.

encodeBoard(BoardState) – Encodes the board state as a string for Q-learning.

AddGameMovesToQTable / AddGameMovesToQTable0 – Updates the Q-tables based on game results.

Bot(e, state) / Bot2(e, state) – AI decision-making functions using Q-table and exploration.

Training AI

The AI trains by playing thousands of games against itself.

The e variable controls the exploration rate, increasing over time to favor learning.

The Q-tables are updated with rewards (1 for a win, -1 for a loss).

Playing Against AI

Once training is complete, the human can play as player 0.

Input your move by typing the column number (0–6) when prompted.

The AI will respond with its move.

The game prints the board after each move and announces the winner or a draw.

Notes

Each column has a maximum height of 6.

AI moves are random at first and improve as training progresses.

The game is console-based and does not include a GUI.

The code can be extended to save Q-tables to files for future training sessions.

Example Board

| | | | | | | |

| | | | | | | |

| | | | | | | |

| | | | | | | |

| | |1| | | | |

|0|1|0| | | | |

--------------

 0|1|2|3|4|5|6


This setup creates a self-learning Connect Four AI with the ability to challenge humans after thousands of simulated games.
