import os

# Clear console
def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
def CreateBoard():
    """ Get a number of cells as input and return matrix as a base for a board"""
    try:
        num = int(input('Please choose the size of the row : '))
        count = 1
        matrix = [[j + i * num + 1 for j in range(num)] for i in range(num)]
        return matrix
    except:
        print('Something went wrong, please try again ')
        CreateBoard()
def DrawBoard(_matrix):
    """ Print the board """
    length = len(_matrix[0])
    max_cell_length = len(str(len(_matrix) ** 2))
    cell_width = max_cell_length + 2
    for i in range(len(_matrix)):
        row = '  |  '.join(('\033[94mX\033[0m' if num == -1 else '\033[95mO\033[0m' if num == 0 else str(num)).center(max_cell_length) for num in _matrix[i])
        print('|', row.center(cell_width * len(_matrix[i]) + len(_matrix[i]) - 1), '|')
        if i < len(_matrix) - 1:
            print(" " * (cell_width))

def DoneGame(_matrix):
    """ Get matrix as an input. if there is a free cell return False, else return True """
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] != -1 and _matrix[i][j] != 0:
                print(_matrix[i][j], 'not done')
                return False
    return True
def ChooseCell(_num , _type , _matrix):
    """ Get as input :
     _num - cell number
     _type - -1 or 0
     _matrix - the matrix
    put the _type in it's place in the matrix
     """
    size = len(_matrix[0])
    _matrix[(_num-1) // size][(_num % size)-1] = _type
def CheckList(_list):
    """ Get input of list. and check if there is a winner in the list
     if the computer won  return 0
     if the player won  return -1
     if no one won return -2
     """
    size = len(_list)
    countX = 0
    countO = 0
    for item in _list:
        if item == -1:
            countX += 1
        if item == 0:
            countO += 1
    if countX == size:
        return -1
    elif countO == size:
        return 0
    else:
        return -2
def CheckWin(_matrix):
    """ Get input of matrix and check if there is a winner in all the possible lists """
    size = len(_matrix[0])
    j = 0
    tempList = []
    # checks rows
    for list in _matrix:
        winner = CheckList(list)
        if winner != -2:
            return winner
    # check columns
    for i in range(size):
        tempList.clear()
        for j in range(size):
            tempList.append(_matrix[j][i])
        winner = CheckList(tempList)
        if winner != -2:
            return winner
    # check diagonal 1
    tempList.clear()
    for i in range(size):
        tempList.append(_matrix[i][i])
    winner = CheckList(tempList)
    if winner != -2:
        return winner
    # check diagonal 2
    tempList.clear()
    for i in range(size):
        tempList.append(_matrix[i][size - 1 - i])
    winner = CheckList(tempList)
    if winner != -2:
        return winner
    return -2

def CheckListForWinMove(_list):
    """ Get input of list. and check if there is a move which the computer can win
     if the computer have one move to win - return 0 and the cell number to choose
     if the player have one move to win - return -1 and the cell number to choose
     if there is no way to win return -2 and the cell number
     """
    size = len(_list)
    countX = 0
    countO = 0
    cellNum = -2
    for i in range(size):
        if _list[i] == -1:
            countX += 1
        elif _list[i] == 0:
            countO += 1
        else:
            cellNum = _list[i]
    if countX == size - 1 and cellNum != -2:
        return -1, cellNum
    elif countO == size - 1 and cellNum != -2:
        return 0, cellNum
    else:
        return -2, cellNum
def CheckMoveForWin(_matrix):
    """ Get input of matrix and check if there is a move to winn in all the possible lists.
     if there is - return the cell number
     else return -2
     """
    size = len(_matrix[0])
    j = 0
    tempList = []
    # checks rows
    for list in _matrix:
        winMove, cell = CheckListForWinMove(list)
        if winMove == 0:
            return cell
    # check columns
    for i in range(size):
        tempList.clear()
        for j in range(size):
            tempList.append(_matrix[j][i])
        winMove , cell = CheckListForWinMove(tempList)
        if winMove == 0:
            return cell
    # check diagonal 1
    tempList.clear()
    for i in range(size):
        tempList.append(_matrix[i][i])
    winMove, cell = CheckListForWinMove(tempList)
    if winMove == 0:
        return cell
    # check diagonal 2
    tempList.clear()
    for i in range(size):
        tempList.append(_matrix[i][size - 1 - i])
    winMove, cell = CheckListForWinMove(tempList)
    if winMove == 0:
        return cell
    return -2
def CheckMoveForUmanNotWin(_matrix):
    """ Get input of matrix and check if the player is one move from winn in all the possible lists and block him.
     if there is - return the cell number
     else return -2
     """
    size = len(_matrix[0])
    j = 0
    tempList = []
    # checks rows
    for list in _matrix:
        winMove, cell = CheckListForWinMove(list)
        if winMove == -1:
            return cell
    # check columns
    for i in range(size):
        tempList.clear()
        for j in range(size):
            tempList.append(_matrix[j][i])
        winMove , cell = CheckListForWinMove(tempList)
        if winMove == -1:
            return cell
    # check diagonal 1
    tempList.clear()
    for i in range(size):
        tempList.append(_matrix[i][i])
    winMove, cell = CheckListForWinMove(tempList)
    if winMove == -1:
        return cell
    # check diagonal 2
    tempList.clear()
    for i in range(size):
        tempList.append(_matrix[i][size - 1 - i])
    winMove, cell = CheckListForWinMove(tempList)
    if winMove == -1:
        print('winMove', winMove)
        print('cell', cell)
        return cell
    return -2
def CheckCornersRound1(_matrix):
    """ Get input of matrix and check for the first turn of the computer, if all the corners are available,
    if they are, return a number of a cell in the corner
     else return -2
     """
    length = len(_matrix[0])
    upLeft = _matrix[0][0]
    upRight = _matrix[0][length-1]
    downLeft = _matrix[length-1][0]
    downRight = _matrix[length-1][length-1]
    if upLeft != 0 and upRight != 0 and downRight != 0 and downLeft != 0 and upLeft != -1 and upRight != -1 and downRight != -1 and downLeft != -1:
            return downRight
    else:
        return -2
def CheckMiddleRound1(_matrix):
    """ Get input of matrix and check for the first turn of the computer, if one of the corners not available,
     return a number of a cell in the middle
     else return -2
     """
    length = len(_matrix[0])
    upLeft = _matrix[0][0]
    upRight = _matrix[0][length-1]
    downLeft = _matrix[length-1][0]
    downRight = _matrix[length-1][length-1]
    if upLeft == -1 or upRight == -1 or downLeft == -1 or downRight == -1:
        print(' matrics', _matrix[(length - 1)//2][(length - 1)//2])
        return _matrix[(length - 1)//2][(length - 1)//2]
    else:
        return -2
def CheckCornersRound2(_matrix):
    """ Get input of matrix and check for the second turn of the computer, if one of the corners are mark with the computer sign,
    check if the opposite corner is free, if it is , return the cell number of that corner
     else return -2
     """
    length = len(_matrix[0])
    upLeft = _matrix[0][0]
    upRight = _matrix[0][length-1]
    downLeft = _matrix[length-1][0]
    downRight = _matrix[length-1][length-1]
    if upLeft == 0 and downRight != -1:
        return downRight
    elif upRight == 0 and downLeft != -1:
        return downLeft
    elif downLeft == 0 and upRight != -1:
        return upRight
    elif downRight == 0 and upLeft != -1:
        return upLeft
    else:
        return -2
def CheckMiddleRound2(_matrix):
    """ Get input of matrix and check for the second turn of the computer, if one of the middle are mark with the computer sign,
    return one of the cells in the row or the column, but not in the diiagonal
     else return -2
     """
    length = len(_matrix[0])
    middle = _matrix[(length - 1)//2][(length - 1)//2]
    up = _matrix[0][(length - 1)//2]
    down = _matrix[length - 1][(length - 1)//2]
    left = _matrix[(length - 1)//2][0]
    right = _matrix[(length - 1)//2][length-1]
    if middle == 0:
        if up != 0 and up != -1 and down != 0 and down != -1:
            return up
        if left != 0 and left != -1 and right != 0 and right != -1:
            return left
    else:
        return -2
def CoputerLogic(_matrix, _roundNumber):
    """ Get input of matrix and the round number, choose the logic of the computer move, and return the cell number"""
    cellNum = CheckMoveForWin(_matrix)
    if cellNum != -2:
        print('cellNum', cellNum)
        return cellNum
    cellNum = CheckMoveForUmanNotWin(_matrix)
    if cellNum != -2:
        print('cellNum', cellNum)
        return cellNum
    if _roundNumber == 2:
        cellNum = CheckCornersRound1(_matrix)
        if cellNum != -2:
            return cellNum
        cellNum = CheckMiddleRound1(_matrix)
        if cellNum != -2:
            return cellNum
    if _roundNumber == 4:
        cellNum = CheckCornersRound2(_matrix)
        if cellNum != -2:
            return cellNum
        cellNum = CheckMiddleRound2(_matrix)
        if cellNum != -2:
            return cellNum
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] != -1 and _matrix[i][j] != 0:
                return _matrix[i][j]

def CheckUserInput(_num, _matrix):
    """ Get input of matrix and the number that the user choose.
    return True if it is a valid number
    else, return False
     """
    length = len(_matrix[0])
    if _num < 1 or _num > length * length:
        return False
    occupied = _matrix[(_num - 1) // length][(_num % length) - 1]
    if occupied == -1 or occupied == 0:
        return False
    return True
def rounds(_matrix):
    """ Get input of matrix and play all the rounds until end of game """
    win = False
    length = len(_matrix[0])
    roundNumber = 1
    maxRoundNumber = length * length
    print('maxRoundNumber', maxRoundNumber )
    while not win and roundNumber < maxRoundNumber +1 :
        print('roundNumber', roundNumber)
        cellNum = int(input('Please choose cell number : '))
        if not(CheckUserInput(cellNum, _matrix)):
            print('Invalid input')
            continue
        roundNumber += 1
        print('roundNumber', roundNumber)
        ChooseCell(cellNum, -1, _matrix)
        DrawBoard(_matrix)
        winner = CheckWin(_matrix)
        if winner != -2:
            break
        if roundNumber == maxRoundNumber +1:
            break
        computer = CoputerLogic(_matrix, roundNumber)
        roundNumber += 1
        print('roundNumber', roundNumber)
        ChooseCell(computer, 0, _matrix)
        ClearConsole()
        print('\n')
        DrawBoard(_matrix)
        print('\n')
        winner = CheckWin(_matrix)
        if winner != -2:
            win = True
    winner = CheckWin(_matrix)
    if winner == -2:
        print('It is a tie ')
    elif winner == -1:
        print('You are the winner')
    else:
        print('The computer is the winner')



#size = int(input('Please choose the size of the row : '))
my_matrix = CreateBoard()

print('\n')
DrawBoard(my_matrix)
print('\n')
rounds(my_matrix)
