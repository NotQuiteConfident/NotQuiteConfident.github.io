# Towers of Hanoi
# Hayden Smedley

import os
import keyboard
import time
import random

# Empty spot on the board
blank = "         "
# Hidden value at end of each tower to simplify placing blocks
ender = "###########"
# Standardized divider
divider = "---------------------------------"
# Blocks used in game
blocks = ["    #    ", "   ###   ", "  #####  ", " ####### ", "#########"]

# Example of a completed tower for comparison
completed = ["    #    ", "   ###   ", "  #####  ", " ####### ", "#########", ender]

# Creates board
def createBoard(inBlocks, inBoard):

    for block in inBlocks:

        col = random.randint(0,2)
        row = random.randint(0,4)

        # Checks if random spot is already filled
        while inBoard[col][row] != blank:

            col = random.randint(0,2)
            row = random.randint(0,4)

        inBoard[col][row] = block

    # Sorts board
    inBoard[0].sort()
    inBoard[1].sort()
    inBoard[2].sort()

    # Checks if created board is in a win state
    if checkWin(inBoard[0], inBoard[1], inBoard[2]):
        inBoard = createBoard(inBlocks, inBoard)

    return(inBoard)

# Checks OS and clears terminal
def clear():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Display the current board
def display(in1, in2, in3, sel, selb, count):

    clear()

    print(divider)
    
    # Display number of moves if not on game opening
    if count == 0:
        print("Welcome to Towers of Hanoi")
    else:
        print("Moves: " + str(count))
    
    print(divider)

    # Display block selected
    print("Selected Block: " + selb)

    print(divider)

    # Display which tower is selected
    if sel == 1:
        print("    [A]    " + "     B     " + "     C     ")
    elif sel == 2:
        print("     A     " + "    [B]    " + "     C     ")
    elif sel == 3:
        print("     A     " + "     B     " + "    [C]    ")
    else:
        print("Selector out of bounds")
    
    # Display board
    print(" " + in1[0] + "  " + in2[0] + "  " + in3[0] + " ")
    print(" " + in1[1] + "  " + in2[1] + "  " + in3[1] + " ")
    print(" " + in1[2] + "  " + in2[2] + "  " + in3[2] + " ")
    print(" " + in1[3] + "  " + in2[3] + "  " + in3[3] + " ")
    print(" " + in1[4] + "  " + in2[4] + "  " + in3[4] + " ")

    print(divider)
    print("Control via arrow keys, left and \nright to select tower, up to \nselect block, down to deposit \nselected block, ESC to quit")
    print(divider)

# Check if move is valid
def validMove(inPiece, inTower):
    
    if inTower[0] != blank:
        return(False)
    elif inTower[1] < inPiece and inTower[1] != blank:
        return(False)
    elif inTower[2] < inPiece and inTower[2] != blank:
        return(False)
    elif inTower[3] < inPiece and inTower[3] != blank:
        return(False)
    elif inTower[4] < inPiece and inTower[4] != blank:
        return(False)
    else:
        return(True)

# Check if board is in a win state
def checkWin(in1, in2, in3):
    
    if in1 == completed:
        return(True)
    elif in2 == completed:
        return(True)
    elif in3 == completed:
        return(True)
    else:
        return(False)

def runGame():

    # Stores which tower is selected
    selector = 1
    # Stores a block when one is selected
    selected = blank
    # Current win state
    win = False
    # How many moves have been taken
    moves = 0
 
    # Towers
    tower1 = [blank, blank, blank, blank, blank, ender]
    tower2 = [blank, blank, blank, blank, blank, ender]
    tower3 = [blank, blank, blank, blank, blank, ender]

    # Array for generating a board
    board = [tower1, tower2, tower3]

    endGame = False

    # Create initial board
    board = createBoard(blocks, board)

    # Assign created towers
    tower1 = board[0]
    tower2 = board[1]
    tower3 = board[2]

    # Display opening board
    display(tower1, tower2, tower3, selector, selected, moves)

    # Run game
    while win is not True:
        
        # change selected tower to the left
        if keyboard.is_pressed("left"):
            
            time.sleep(0.1)

            selector = selector - 1

            # Check if looped around
            if selector < 1:

                selector = 3

            display(tower1, tower2, tower3, selector, selected, moves)

        # change selected tower to the right
        if keyboard.is_pressed("right"):

            time.sleep(0.1)
            
            selector = selector + 1

            # Check if looped around
            if selector > 3:

                selector = 1
                
            display(tower1, tower2, tower3, selector, selected, moves)

        # Selecting a block
        if keyboard.is_pressed("up"):

            time.sleep(0.1)

            # Check if something is already selected
            if selected == blank:

                board = [tower1, tower2, tower3]

                for i, block in enumerate(board[selector - 1]):

                    # Find first non blank spot that is not the hidden end piece
                    if block != blank and i != (len(board[selector - 1]) - 1):

                        selected = block
                        board[selector - 1][i] = blank

                        tower1 = board[0]
                        tower2 = board[1]
                        tower3 = board[2]

                        display(tower1, tower2, tower3, selector, selected, moves)
                            
                        break

        # Deposit block
        if keyboard.is_pressed("down"):

            time.sleep(0.1)

            # Check if something is actually selected
            if selected != blank:

                board = [tower1, tower2, tower3]

                # Deposit if move is valid
                if validMove(selected, board[selector - 1]):

                    for i, block in enumerate(board[selector - 1]):

                        # Find first non blank spot
                        if block != blank:
                            
                            board[selector - 1][i - 1] = selected
                            selected = blank
                            moves += 1

                            tower1 = board[0]
                            tower2 = board[1]
                            tower3 = board[2]

                            display(tower1, tower2, tower3, selector, selected, moves)
                            
                            break
        
        # End game early
        if keyboard.is_pressed("esc"):

            print("Game Ended")

            break
        
        # Check if the game has been won and end the game
        if checkWin(tower1, tower2, tower3):

            win = True
            print("YOU WIN")
            print(divider)

            break

    # Close program after ESC is hit or start a new one if Space is hit
    if win and endGame is not True:
        
        print("Press 'ESC' to end program or 'Space' to start a new one.")
        
        while endGame is not True:

            if keyboard.is_pressed("esc"):

                endGame = True

            if keyboard.is_pressed("space"):

                runGame()
                endGame = True

runGame()
