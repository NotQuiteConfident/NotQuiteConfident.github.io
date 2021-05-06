# Towers of Hanoi

tower1 = [" ### ", "#####", "     "]
tower2 = ["     ", "     ", "  #  "]
tower3 = ["     ", "     ", "     "]

selector = 1
selected = "     "
blank = "     "

def display(in1, in2, in3, sel):

    print("--------------------------")
    print("Welcome to Towers of Hanoi")
    print("--------------------------")

    print(selected)

    print("--------------------------")

    in1 = sortTowers(in1)
    in2 = sortTowers(in2)
    in3 = sortTowers(in3)

    if sel == 1:
        print("  [A]  " + "   B   " + "   C   ")
    elif sel == 2:
        print("   A   " + "  [B]  " + "   C   ")
    elif sel == 3:
        print("   A   " + "   B   " + "  [C]  ")
    else:
        print("Selector out of bounds")
    
    print(" " + in1[0] + "  " + in2[0] + "  " + in3[0] + " ")
    print(" " + in1[1] + "  " + in2[1] + "  " + in3[1] + " ")
    print(" " + in1[2] + "  " + in2[2] + "  " + in3[2] + " ")

    print("--------------------------")

def sortTowers(inTower):

    if inTower[0] > inTower[2]:
        
        temp = inTower[2]
        inTower[2] = inTower[0]
        inTower[0] = temp

    elif inTower[0] > inTower[1]:
        
        temp = inTower[1]
        inTower[1] = inTower[0]
        inTower[0] = temp

    if inTower[1] > inTower[2]:

        temp = inTower[2]
        inTower[2] = inTower[1]
        inTower[1] = temp

    return(inTower)

def validMove(inPiece, inTower):
    
    if inTower[0] != blank:
        return(False)
    elif inTower[1] < inPiece:
        return(False)
    elif inTower[2] < inPiece:
        return(False)
    else:
        return(True)

display(tower1, tower2, tower3, selector)

print(validMove("#####",tower2))
