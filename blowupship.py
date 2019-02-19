# battleship.py
import random
#To do:
#Turn off testing flag
#Instruction function
#Random computer ship placement
#Better user input checking throughout
#Consider using lists to show which ships on each side have already been sunk
#Keep computer and player from shooting at same square
#Input checking for shooting
#Let player know when they've sunk an entire ship

# Constants
BLANK = "_"
CARRIER = "A"
BATTLESHIP = "B"
CRUISER = "C"
SUB = "S"
DESTROYER = "D"
CARRIERLENGTH = 5
BATTLESHIPLENGTH = 4
CRUISERLENGTH = 3
SUBLENGTH = 3
DESTROYERLENGTH = 2

DEBUGGING = False

# *** Functions ***

def playershoots(computerships, hitsmissesoncomputer):
    goodshot = False
    while goodshot == False:
        print("Where would you like to shoot?  Please enter coordinates.")
        playercoo = input()
        x,y = getplayercoord(playercoo)
        if hitsmissesoncomputer[x,y][-1] == "S":
            print("You already shot there!  Choose again.")
        else:
            goodshot = True
    if computerships[x,y] == "_":
        print("You missed!")
        hitsmissesoncomputer[x,y] = "_S"
    else:
        print("You hit a ship!")
        hitsmissesoncomputer[x,y] = computerships[x,y] + "S"
        computerships[x,y] = computerships[x,y] + "S"
    return computerships, hitsmissesoncomputer

def computershoots(playerships, hitsmissesonplayer):
    goodshot = False
    while goodshot == False:
        x = random.randint(1,10)
        y = random.randint(1,10)
        if hitsmissesonplayer[x,y][-1] != "S":
            goodshot = True
    if playerships[x,y] == "_":
        hitsmissesonplayer[x,y] = "_S"
        print("The computer shot and missed at:")
        print(x,y)
    else:
        hitsmissesonplayer[x,y] = playerships[x,y] + "S"
        playerships[x,y] = playerships[x,y] + "S"
        print(x,y)
        if playerships[x,y] == CARRIER + "S":
            print("The computer shot and hit your aircraft carrier.")
        elif playerships[x,y] == BATTLESHIP + "S":
            print("The computer shot and hit your battleship.")
        elif playerships[x,y] == CRUISER + "S":
            print("The computer shot and hit your cruiser.")
        elif playerships[x,y] == SUB + "S":
            print("The computer shot and hit your submarine.")
        else:
            print("The computer shot and hit your destroyer.")
    return playerships, hitsmissesonplayer

def instructions():
    print("Welcome to Battleship, written by Melody Gill. ")
    print("You'll be playing against a ")
    print("computer opponent.  This program uses the usual rules of Battleship.")
    print("If you are unfamiliar with these rules, please enter i now.  ")
    print("Otherwise, press enter to continue.")
    iorc = input()
    if iorc == "i" or iorc == "I":
        print("Instructions coming soon to a program near you!\n")

def checkforwinner(playerships, computerships):
    count = 0
    for y in range (1,11):
        for x in range (1,11):
            if hitsmissesoncomputer[x,y] == "AS" or hitsmissesoncomputer[x,y] == "BS" or hitsmissesoncomputer[x,y] == "CS" or hitsmissesoncomputer[x,y] == "DS" or hitsmissesoncomputer[x,y] == "SS":
                count = count + 1
    if count == CARRIERLENGTH + BATTLESHIPLENGTH + CRUISERLENGTH + SUBLENGTH + DESTROYERLENGTH:
        return "human"
    else:
        return "None"
    count = 0
    for y in range (1,11):
        for x in range (1,11):
            if hitsmissesonplayer[x,y] == "AS" or hitsmissesonplayer[x,y] == "BS" or hitsmissesonplayer[x,y] == "CS" or hitsmissesonplayer[x,y] == "DS" or hitsmissesonplayer[x,y] == "SS":
                count = count + 1
    if count == CARRIERLENGTH + BATTLESHIPLENGTH + CRUISERLENGTH + SUBLENGTH + DESTROYERLENGTH:
        return "computer"
    #Return "computer" if computer has won.  Return "human" if player has won.
    #Return "None" if no one has won yet.
    return "None"

def blankboard(board):
    x = 0
    y = 0
    for x in range (1, 11):
        for y in range (1, 11):
            board[x,y] = BLANK
    return board

def drawboard(board):
    print("  1 2 3 4 5 6 7 8 9 10")
    for y in range (1,11):
        print(chr(64+y), end= " ")
        for x in range(1,11):
            print(board[x,y], end=" ")
        print("")

def doubledrawboard(board1, board2):
    print("  1 2 3 4 5 6 7 8 9 10\t\t\t\t  1 2 3 4 5 6 7 8 9 10")
    for y in range (1, 11):
        print(chr(64+y), end= " ")
        for x in range(1,11):
            if board1[x,y] == "AS":
                print("@", end=" ")
            elif board1[x,y] == "BS":
                print("&", end=" ")
            elif board1[x,y] == "CS":
                print("<", end=" ")
            elif board1[x,y] == "SS":
                print("$", end=" ")
            elif board1[x,y] == "DS":
                print("!", end=" ")
            else:
                print(board1[x,y], end=" ")
        print("\t\t\t\t", end="")
        print(chr(64+y), end= " ")
        for x in range(1,11):
            if board2[x,y] == BLANK:
                print(BLANK, end=" ")
            elif board2[x,y] == "_S":
                print("M", end=" ")
            else:
                print("H", end=" ")
        print("")

def computersetupships(board):
    for q in range(4,9):
        board[q,9] = "A"
    for i in range(3,7):
        board[2,i] = "B"
    for c in range(6,9):
        board[c,4] = "C"
    for s in range(5,8):
        board[4,s] = "S"
    for d in range(5,7):
        board[d,1] = "D"
    return board

def playersetupships(board):
    drawboard(board)
    goodcoo = False
    while goodcoo == False:
        print("Enter coordinates for the beginning of the aircraft carrier.  It will be " + str(CARRIERLENGTH) + " squares long.")
        coo = input()
        startx, starty = getplayercoord(coo)
        print("Do you want your carrier placed (v)ertically or (h)orizontally?")
        vorh = input()
        if vorh == "v" or vorh == "V":
            endx = startx
            endy = starty + CARRIERLENGTH - 1
        elif vorh == "h" or vorh == "H":
            endx = startx + CARRIERLENGTH - 1
            endy = starty
        board, isitok = checkshipplacement(board, CARRIER, startx, starty, endx, endy)
        if isitok == "OUT":
            print("These coordinates result in the carrier being off the board!")
        if isitok == "OVERLAP":
            print("These coordinates result in the carrier overlapping another ship!")
        if isitok == "OK":
            goodcoo = True
    drawboard(board)
    goodcoo = False
    while goodcoo == False:
        print("Enter coordinates for the beginning of the battleship.  It will be " + str(BATTLESHIPLENGTH) + " squares long.")
        coo = input()
        startx, starty = getplayercoord(coo)
        print("Do you want your battleship placed (v)ertically or (h)orizontally?")
        vorh = input()
        if vorh == "v" or vorh == "V":
            endx = startx
            endy = starty + BATTLESHIPLENGTH - 1
        elif vorh == "h" or vorh == "H":
            endx = startx + BATTLESHIPLENGTH - 1
            endy = starty
        board, isitok = checkshipplacement(board, BATTLESHIP, startx, starty, endx, endy)
        if isitok == "OUT":
            print("These coordinates result in the battleship being off the board!")
        if isitok == "OVERLAP":
            print("These coordinates result in the battleship overlapping another ship!")
        if isitok == "OK":
            goodcoo = True
    drawboard(board)
    goodcoo = False
    while goodcoo == False:
        print("Enter coordinates for the beginning of the cruiser.  It will be " + str(CRUISERLENGTH) + " squares long.")
        coo = input()
        startx, starty = getplayercoord(coo)
        print("Do you want your cruiser placed (v)ertically or (h)orizontally?")
        vorh = input()
        if vorh == "v" or vorh == "V":
            endx = startx
            endy = starty + CRUISERLENGTH - 1
        elif vorh == "h" or vorh == "H":
            endx = startx + CRUISERLENGTH - 1
            endy = starty
        board, isitok = checkshipplacement(board, CRUISER, startx, starty, endx, endy)
        if isitok == "OUT":
            print("These coordinates result in the cruiser being off the board!")
        if isitok == "OVERLAP":
            print("These coordinates result in the cruiser overlapping another ship!")
        if isitok == "OK":
            goodcoo = True
    drawboard(board)
    goodcoo = False
    while goodcoo == False:
        print("Enter coordinates for the beginning of the submarine.  It will be " + str(SUBLENGTH) + " squares long.")
        coo = input()
        startx, starty = getplayercoord(coo)
        print("Do you want your submarine placed (v)ertically or (h)orizontally?")
        vorh = input()
        if vorh == "v" or vorh == "V":
            endx = startx
            endy = starty + SUBLENGTH - 1
        elif vorh == "h" or vorh == "H":
            endx = startx + SUBLENGTH - 1
            endy = starty
        board, isitok = checkshipplacement(board, SUB, startx, starty, endx, endy)
        if isitok == "OUT":
            print("These coordinates result in the submarine being off the board!")
        if isitok == "OVERLAP":
            print("These coordinates result in the submarine overlapping another ship!")
        if isitok == "OK":
            goodcoo = True
    drawboard(board)
    goodcoo = False
    while goodcoo == False:
        print("Enter coordinates for the beginning of the destroyer.  It will be " + str(DESTROYERLENGTH) + " squares long.")
        coo = input()
        startx, starty = getplayercoord(coo)
        print("Do you want your destroyer placed (v)ertically or (h)orizontally?")
        vorh = input()
        if vorh == "v" or vorh == "V":
            endx = startx
            endy = starty + DESTROYERLENGTH - 1
        elif vorh == "h" or vorh == "H":
            endx = startx + DESTROYERLENGTH - 1
            endy = starty
        board, isitok = checkshipplacement(board, DESTROYER, startx, starty, endx, endy)
        if isitok == "OUT":
            print("These coordinates result in the destroyer being off the board!")
        if isitok == "OVERLAP":
            print("These coordinates result in the destroyer overlapping another ship!")
        if isitok == "OK":
            goodcoo = True
    drawboard(board)
    return board

def checkshipplacement(board, ID, startx, starty, endx, endy):
    # If ship placement is out of the board, return "OUT"
    # If ship placement overlaps with another ship, return "OVERLAP"
    # If ship placement is OK, place ship on board and return "OK"

    # Check to see if ship fits on the board
    if startx >= 1 and startx <= 10 and starty >= 1 and starty <= 10 and \
       endx >= 1 and endx <= 10 and endy >= 1 and endy <= 10:
            pass
    else:
        return board, "OUT"
       
    # Now check to see if the ship overlaps with a previously placed ship.
    # Note that if startx = endx, the ship must be vertically placed and if
    # starty = endy, the ship must be horitzontally placed.  If neither of these
    # is true, we have been given bad input and must complain!
    if startx == endx:
        coordsok = True
        for index in range(starty, endy+1): #Have to compensate for range stopping one early
            if board[startx, index] != BLANK: #Since startx=endx; I can use either one for the xcoord
                coordsok = False
        if coordsok == False:
            return board, "OVERLAP"
    if starty == endy:
        coordsok = True
        for index in range(startx, endx+1):
            if board[index, starty] != BLANK:
                coordsok = False
        if coordsok == False:
            return board, "OVERLAP"
    if startx != endx and starty != endy:
        print("Error in checkshipplacement - bad input received!")
        return board, "OVERLAP" #Not actually an overlap but that's OK

    # It's a legal ship placement so place the ship and return "OK".  Again,
    # if startx = endx, ship is being placed vertically.  If starty = endy,
    # ship is being placed horizontally.  No need to check for the case that
    # neither of these is true because we already handled that above.
    if startx == endx:
        for index in range(starty, endy+1):
            board[startx, index] = ID
    if starty == endy:
        for index in range(startx, endx+1):
            board[index, starty] = ID
    return board, "OK" 
   
def getplayercoord(string):
    y = string[0].lower()
    x = int(string[1:])
    y = ord(y)
    y = y-96
    return x, y
      
# *** Main Function ***
# *** Main Function ***
# *** Main Function ***

# Introduce the game
instructions()

# Create the four arrays to be used to track what's going on in the game
computerships = {} #Shows computer's ships and any hits on them
playerships = {} #Shows player's ships and any hits on them
hitsmissesoncomputer = {} #Shows shots fired by player on computer and any hits/misses
hitsmissesonplayer = {} #Shows shots fired by computer on player and any hits/misses

# Fill all four arrays with blanks
computerships = blankboard(computerships)
playerships = blankboard(playerships)
hitsmissesoncomputer = blankboard(hitsmissesoncomputer)
hitsmissesonplayer = blankboard(hitsmissesonplayer)

# Have both players set up their ships prior to starting the game
computerships = computersetupships(computerships)

if DEBUGGING == True:
    playerships = computersetupships(playerships)
elif DEBUGGING == False:
    playerships = playersetupships(playerships)
else:
    print("Help!  Bad value in DEBUGGING!")

# Now each player takes turns shooting at the other.  After each shot, check
# to see if the game is over or not.
while True:
    print("Here's how things look right now...")
    print("  YOUR SHIPS\t\t\t\t\t  ENEMY SHIPS")
    doubledrawboard(playerships, hitsmissesoncomputer)
    playershoots(computerships, hitsmissesoncomputer)
    winner = checkforwinner(playerships, computerships)
    if winner != "None":
        break
    playerships, hitsmissesonplayer = computershoots(playerships, hitsmissesonplayer)
    winner = checkforwinner(playerships, computerships)
    if winner != "None":
        break

# Show the winner and end program
print("The " + winner + " won the game!  Thanks for playing; hope to see you again soon!")
