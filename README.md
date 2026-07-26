Connect Four Q-Learning Bot

A Connect Four implementation in Python featuring a reinforcement learning agent trained via self-play using a Q-table approach.

Overview

This project trains two bots to play Connect Four against each other over thousands of games, learning which moves lead to wins. After training, you can play against the trained bot yourself.

How It Works
The Board

The board is represented as a list of 7 strings (one per column). Each character in a string is a piece ("1" or "0"), stacked bottom-to-top. Pieces are dropped into columns and settle at the lowest empty slot, just like real Connect Four. The grid is 7 columns wide and 6 rows tall.

Win Detection

After each move, the code checks for four-in-a-row in every direction:

Vertical — scans the current column for "1111" or "0000"
Horizontal — builds the row across all columns and scans it
Diagonal (up and down) — walks the two diagonals through the placed piece and scans them

A draw is declared when every column is full.

Learning Approach

The bots use a simple Q-table (a dictionary mapping board states to action values):

State encoding — each board is encoded into a fixed-length string via encodeBoard, padding unfilled cells with "9" so every state has a consistent key.
Two Q-tables — qTable for player 1 and qTable0 for player 0, so each side learns independently.
Rewards — after a game ends, every move the winner made gets +1 added to its state-action value, and every move the loser made gets -1.
Epsilon-greedy policy — the Bot functions mix exploration and exploitation. Early on, moves are mostly random; as training progresses (e increases each lap), the bots increasingly pick the highest-valued legal move from their Q-table.
Training Loop

The script runs 100 laps. Each lap plays 1,000 self-play games, gradually raising the exploitation rate e. This builds up the Q-tables through roughly 100,000 games of experience.

Play Phase

After training, the script starts a human-vs-bot loop. The trained bot plays as player 1, and you enter your column (0–6) each turn. The board prints after every move.

Running It
bash
python connect_four.py

Training runs first and prints progress (Lap Done 0, Lap Done 1, ...). This takes a while. Once complete, you'll be prompted to Enter move: — type a column number 0–6.

Requirements

Python 3. Only the standard library (random) is used
