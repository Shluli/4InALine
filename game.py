import random

board = []
player = 1
def BuildBoard():
    global board, player
    board = ["", "", "", "", "", "", ""]
    player = 1

def PrintBoard(board):
    for r in range(6):
        line = ""
        for c in range(7):
            line += ("|")
            if len(board[c]) > 5-r:
                line += (board[c][5-r])
            else:
                line += (" ")
        line += ("|")
        print(line)
    print("--" * 7)
    print(" 0|1|2|3|4|5|6")

def DropPiece(col):
    global board, player
    if type(col) == int and col>=0 and col<=6 and len(board[col]) < 6:
        board[col] += str(player)
        player = 1-player
        return True
    else:
        return False
    
def checkWinVerticly(col):
    return "1111" in col or "0000" in col

def checkWinHorizontally(row):
    line = ""
    for i in range(7):
        if len(board[i]) > row:
            line += board[i][row]
        else:
            line += " "
    return "1111" in line or "0000" in line

def CheckWinDiagonallyUp(col, row):
    line = "" 
    for i in range(7):
        if col-4+i >= 0 and row-4+i >= 0 and col-4+i <= 6 and row-4+i <= 6 and len(board[col-4+i]) > row-4+i:
            line += board[col-4+i][row-4+i]
    return "1111" in line or "0000" in line

def CheckWinDiagonallyDown(col, row):
    line = "" 
    for i in range(9):
        if col-4+i >= 0 and row+4-i >= 0 and col-4+i <= 6 and row+4-i <= 6 and len(board[col-4+i]) > row+4-i:
            line += board[col-4+i][row+4-i]
    return "1111" in line or "0000" in line

def CheckWinsOverall(col, row):
    return checkWinHorizontally(row) or checkWinVerticly(board[col]) or CheckWinDiagonallyUp(col, row) or CheckWinDiagonallyDown(col, row)

def CheckDraw(grid):
    return all(len(col) == 6 for col in grid)

def encodeBoard(BoardState):
    encoded = ""
    for i in range(7):
        encoded += (BoardState[i] + ((6-len(BoardState[i]))*"9"))
    return encoded

def AddGameMovesToQTable(States, Actions, win):
    global qTable
    for i in range(len(States)):
        if qTable.get(States[i]) is None:
            new = [0,0,0,0,0,0,0]
            new[Actions[i]] = win
            qTable.update({States[i] : new})
        else:
            new = qTable.get(States[i])
            new[Actions[i]] += win
            qTable.update({States[i] : new})

def AddGameMovesToQTable0(States, Actions, win):
    global qTable0
    for i in range(len(States)):
        if qTable0.get(States[i]) is None:
            new = [0,0,0,0,0,0,0]
            new[Actions[i]] = win
            qTable0.update({States[i] : new})
        else:
            new = qTable0.get(States[i])
            new[Actions[i]] += win
            qTable0.update({States[i] : new})
        

def Bot(e, state):
    chance = random.randint(1,100)
    move = random.randint(0, 6)
    Qmoves = qTable.get(state)
    while len(board[move]) == 6:
        move = random.randint(0, 6)
    if chance < e and Qmoves != None:
        for i in range(7):
            if Qmoves[i] > Qmoves[move] and len(board[i]) < 6:
                move = i
    return move


def Bot2(e, state):
    chance = random.randint(1,150)
    move = random.randint(0, 6)
    Qmoves = qTable0.get(state)
    while len(board[move]) == 6:
        move = random.randint(0, 6)
    if chance < e and Qmoves != None:
        for i in range(7):
            if Qmoves[i] > Qmoves[move] and len(board[i]) < 6:
                move = i
    return move

qTable = {}
qTable0 = {}
e = 0
for i in range(100):
        e = e+1
        print("Lap Done" + str(i))
        for i in range(1000):
            BuildBoard()
            end = False
            gamemoves = []
            Actions = []
            gamemoves0 = []
            Actions0 = []
            while end == False:
                if player == 1:
                    ColInput = Bot(e, encodeBoard(board))
                    gamemoves.append(encodeBoard(board))
                    Actions.append(ColInput)
                else:
                    ColInput = Bot2(e, encodeBoard(board))
                    gamemoves0.append(encodeBoard(board))
                    Actions0.append(ColInput)
                DropPiece(ColInput)
                if CheckDraw(board):
                    end = True
                if CheckWinsOverall(ColInput, len(board[ColInput]) - 1):
                    end = True
                    if player == 0:
                        AddGameMovesToQTable(gamemoves, Actions, 1)
                        AddGameMovesToQTable0(gamemoves0, Actions0, -1)
                    else:
                        AddGameMovesToQTable(gamemoves, Actions, -1)
                        AddGameMovesToQTable0(gamemoves0, Actions0, 1)
        
            
for i in range(50000):
            BuildBoard()
            PrintBoard(board)
            end = False
            gamemoves = []
            Actions = []
            while end == False:
                if player == 1:
                    ColInput = Bot(e, encodeBoard(board))
                    gamemoves.append(encodeBoard(board))
                    Actions.append(ColInput)
                else:
                    ColInput = int(input("Enter move:"))
                DropPiece(ColInput)
                if CheckDraw(board):
                    end = True
                if CheckWinsOverall(ColInput, len(board[ColInput]) - 1):
                    end = True
                    if player == 0:
                        print("player 1 wins!")
                    else:
                        print("player 0 wins!")
                PrintBoard(board)

        
