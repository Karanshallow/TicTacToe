from TicTacTree import TicTacTree
import random
import pickle


def boardMaker(boardState):
    print(" | |")
    print(boardState[1] + "|" + boardState[2] + "|" + boardState[3])
    print(" | |")
    print("---------")
    print(" | |")
    print(boardState[4] + "|" + boardState[5] + "|" + boardState[6])
    print(" | |")
    print("---------")
    print(" | |")
    print(boardState[7] + "|" + boardState[8] + "|" + boardState[9])
    print(" | |")

def goesFirst():
    choice = ""
    while((choice!="X") and (choice!="O")):
        print("Choose X or O (X goes first)")
        choice = input().upper()
    if choice =='X':
        return ['X','O']
    else:
        return ['O','X']
def playIt(board,turn,choice):
    board[turn] = choice
def checkWinner(board,turn):
    return (board[1] == turn and board[2] == turn and board[3] == turn) or (board[4] == turn and board[5] == turn and board[6] == turn) or (board[7] == turn and board[8] == turn and board[9] == turn) or (board[1] == turn and board[5] == turn and board[9] == turn) or (board[3] == turn and board[5] == turn and board[7] == turn) or (board[1] == turn and board[4] == turn and board[7] == turn) or (board[2] == turn and board[5] == turn and board[8] == turn) or (board[3] == turn and board[6] == turn and board[9] == turn)
def copyBoard(board):
    copy = []
    for i in board:
        copy.append(i)
    return copy
def isSpaceFree(board,choice):
    return board[choice] == " "
def playerMove(board,movesMade,pastGames):
    turner = ''
    turn = 0
    copyPast = pastGames
    while turner not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(turn)):
        print("Choose the space where your next move is going to be (1-9)")
        turner = input()
        turn = int(turner)
    for i in movesMade:
        if i == 9:
            copyPast = copyPast.is9
        elif i==8:
            copyPast = copyPast.is8
        elif i==7:
            copyPast = copyPast.is7
        elif i==6:
            copyPast = copyPast.is6
        elif i==5:
            copyPast = copyPast.is5
        elif i==4:
            copyPast = copyPast.is4
        elif i==3:
            copyPast = copyPast.is3
        elif i==2:
             copyPast = copyPast.is2
        elif i==1:
            print("Gotcha")
            copyPast = copyPast.is1

    if turn == 9 and copyPast.is9 == None:
        copyPast.is9 = TicTacTree()
    elif turn == 8 and copyPast.is8 == None:
        copyPast.is8 = TicTacTree()
    elif turn ==7 and copyPast.is7 == None:
        copyPast.is7 = TicTacTree()
    elif turn ==6 and copyPast.is6 == None:
        copyPast.is6 = TicTacTree()
    elif turn ==5 and copyPast.is5 == None:
        copyPast.is5 = TicTacTree()
    elif turn == 4 and copyPast.is4 == None:
        copyPast.is4 = TicTacTree()
    elif turn == 3 and copyPast.is3 == None:
        copyPast.is3 = TicTacTree()
    elif turn == 2 and copyPast.is2 == None:
        copyPast.is2 = TicTacTree()
    elif turn ==1 and copyPast.is1 == None:
        copyPast.is1 = TicTacTree()
    return turn
def gameAI(board, choice, movesMade, pastGames):
    if choice == 'X':
        return gameGoesFirst(board, movesMade, pastGames)
    else:
        return gameGoesSec(board,movesMade,pastGames)
#returns the move position for the highest possible numeric value 
def gameGoesFirst(board,movesMade,pastGames):
#tries to open up dataset on old moves otherwise creates a new dataset
    copyPast = pastGames
#goes into the old moves
    for i in movesMade:
        if i == 9:
            copyPast = copyPast.is9
        elif i==8:
            copyPast = copyPast.is8
        elif i==7:
            copyPast = copyPast.is7
        elif i==6:
            copyPast = copyPast.is6
        elif i==5:
            copyPast = copyPast.is5
        elif i==4:
            copyPast = copyPast.is4
        elif i==3:
            copyPast = copyPast.is3
        elif i==2:
            copyPast = copyPast.is2
        elif i==1:
            copyPast = copyPast.is1
    possMoves = []
    for i in range(1,10):
        if isSpaceFree(board,i):
            possMoves.append(i)
    temp = -10000000
    maxJ = 0
    temp3 = []
    oppBlock = -1
    myWin = -1
    for j in possMoves:
        if copyPast.next(j) !=None:
            if copyPast.next(j)>temp:
                temp = copyPast.next(j)
                maxJ = j

        else:
            temp3.append(j)
        dupeBoard = copyBoard(board)
        playIt(dupeBoard,j,'O')
        if checkWinner(dupeBoard,'O'):
            oppBlock = j
        dupeBoard = copyBoard(board)
        playIt(dupeBoard,j,'X')
        if checkWinner(dupeBoard,'X'):
            myWin = j
    if myWin != -1 and temp <=0:
        return myWin
    if oppBlock != -1 and oppBlock <=0:
        return oppBlock
    if temp>0 or len(temp3) == 0:
        movesMade.append(maxJ)
        return maxJ
    else:
        if temp3[0] == 9:
            copyPast.is9 = TicTacTree()
        elif temp3[0] == 8:
            copyPast.is8 = TicTacTree()
        elif temp3[0] ==7:
            copyPast.is7 = TicTacTree()
        elif temp3[0] ==6:
            copyPast.is6 = TicTacTree()
        elif temp3[0] ==5:
            copyPast.is5 = TicTacTree()
        elif temp3[0] == 4:
            copyPast.is4 = TicTacTree()
        elif temp3[0] == 3:
            copyPast.is3 = TicTacTree()
        elif temp3[0] == 2:
            copyPast.is2 = TicTacTree()
        elif temp3[0] ==1:
            copyPast.is1 = TicTacTree()
        movesMade.append(temp3[0])
        return temp3[0]
def gameGoesSec(board,movesMade,pastGames):
    copyPast = pastGames
    for i in movesMade:
        if i == 9:
            copyPast = copyPast.is9
        elif i==8:
            copyPast = copyPast.is8
        elif i==7:
            copyPast = copyPast.is7
        elif i==6:
            copyPast = copyPast.is6
        elif i==5:
            copyPast = copyPast.is5
        elif i==4:
            copyPast = copyPast.is4
        elif i==3:
            copyPast = copyPast.is3
        elif i==2:
            copyPast = copyPast.is2
        elif i==1:
            copyPast = copyPast.is1
    possMoves = []
    for i in range(1,10):
        if isSpaceFree(board,i):
            possMoves.append(i)
    temp = 10000000
    maxJ = possMoves[0]
    temp3 = []
    oppBlock = -1
    myWin = -1
    for j in possMoves:
            if copyPast.next(j) !=None:
                if copyPast.next(j)<temp:
                    temp = copyPast.next(j)
                    maxJ = j
            else:
                temp3.append(j)
            dupeBoard = copyBoard(board)
            playIt(dupeBoard,j,'X')
            if checkWinner(dupeBoard,'X'):
                oppBlock = j
            dupeBoard = copyBoard(board)
            playIt(dupeBoard,j,'O')
            if checkWinner(dupeBoard,'O'):
                myWin = j
    if myWin != -1 and temp <=0:
        return myWinn
    if oppBlock != -1 and oppBlock <=0:
        return oppBlock
    if temp<0 or len(temp3) == 0:
        movesMade.append(maxJ)
        return maxJ
    else:
        if temp3[0] == 9:
            copyPast.is9 = TicTacTree()
        elif temp3[0] == 8:
            copyPast.is8 = TicTacTree()
        elif temp3[0] ==7:
            copyPast.is7 = TicTacTree()
        elif temp3[0] ==6:
            copyPast.is6 = TicTacTree()
        elif temp3[0] ==5:
            copyPast.is5 = TicTacTree()
        elif temp3[0] == 4:
            copyPast.is4 = TicTacTree()
        elif temp3[0] == 3:
            copyPast.is3 = TicTacTree()
        elif temp3[0] == 2:
            copyPast.is2 = TicTacTree()
        elif temp3[0] ==1:
            copyPast.is1 = TicTacTree()
        movesMade.append(temp3[0])
        return temp3[0]
def TieGame(board):
    for i in board:
        if i == " ":
            return False
    return True
def playAgain():
    resp = ''
    while resp != 'Y' and resp != 'N':
        print("Would you like to play me again?(Y or N)")
        resp = input().upper()
    if resp == 'Y':
        return True
    else:
        return False
def XWins(movesMade,pastGames):
    copyPast = pastGames
    for i in movesMade:
        if i == 9:
            copyPast = copyPast.is9
        elif i==8:
            copyPast = copyPast.is8
        elif i==7:
            copyPast = copyPast.is7
        elif i==6:
            copyPast = copyPast.is6
        elif i==5:
            copyPast = copyPast.is5
        elif i==4:
            copyPast = copyPast.is4
        elif i==3:
            copyPast = copyPast.is3
        elif i==2:
            copyPast = copyPast.is2
        elif i==1:
            copyPast = copyPast.is1
    if copyPast.data == 0:
        secondCopy = pastGames
        for i in movesMade:
            if i == 9:
                secondCopy = secondCopy.is9
                secondCopy.data +=1
            elif i==8:
                secondCopy = secondCopy.is8
                secondCopy.data +=1
            elif i==7:
                secondCopy = secondCopy.is7
                secondCopy.data +=1
            elif i==6:
                secondCopy = secondCopy.is6
                secondCopy.data +=1
            elif i==5:
                secondCopy = secondCopy.is5
                secondCopy.data +=1
            elif i==4:
                secondCopy = secondCopy.is4
                secondCopy.data +=1
            elif i==3:
                secondCopy = secondCopy.is3
                secondCopy.data +=1
            elif i==2:
                secondCopy = secondCopy.is2
                secondCopy.data +=1
            elif i==1:
                secondCopy = secondCopy.is1
                secondCopy.data +=1
def XLoses(movesMade,pastGames):
    copyPast = pastGames
    for i in movesMade:
        if i == 9:
            copyPast = copyPast.is9
        elif i==8:
            copyPast = copyPast.is8
        elif i==7:
            copyPast = copyPast.is7
        elif i==6:
            copyPast = copyPast.is6
        elif i==5:
            copyPast = copyPast.is5
        elif i==4:
            copyPast = copyPast.is4
        elif i==3:
            copyPast = copyPast.is3
        elif i==2:
            copyPast = copyPast.is2
        elif i==1:
            copyPast = copyPast.is1
    if copyPast.data == 0:
        secondCopy = pastGames
        for i in movesMade:
            if i == 9:
                secondCopy = secondCopy.is9
                secondCopy.data -=1
            elif i==8:
                secondCopy = secondCopy.is8
                secondCopy.data -=1
            elif i==7:
                secondCopy = secondCopy.is7
                secondCopy.data -=1
            elif i==6:
                secondCopy = secondCopy.is6
                secondCopy.data -=1
            elif i==5:
                secondCopy = secondCopy.is5
                secondCopy.data -=1
            elif i==4:
                secondCopy = secondCopy.is4
                secondCopy.data -=1
            elif i==3:
                secondCopy = secondCopy.is3
                secondCopy.data -=1
            elif i==2:
                secondCopy = secondCopy.is2
                secondCopy.data -=1
            elif i==1:
                secondCopy = secondCopy.is1
                secondCopy.data -=1
def main():
    try:
        pickle_in = open("tictacdata.pickle","rb")
        pastGames = pickle.load(pickle_in)
    except:
        pastGames = TicTacTree()
        print("Pickle Failed")
    print("Tic Tac Toe! Beat me once, shame on you. Beat me twice, shame on Karandeep")
    while True:
        board = [""," "," "," "," "," "," "," "," "," "]
        playerTurn, compTurn = goesFirst()
        if compTurn == 'X':
            print("I go first")
        else:
            print("You go first")
        gameState = True
        boardMaker(board)
        pastMoves= []
        while gameState:
            if playerTurn == 'X':
                move = playerMove(board,pastMoves,pastGames)
                playIt(board,move,playerTurn)
                pastMoves.append(move)
                boardMaker(board)
                if checkWinner(board, playerTurn):
                    print("You win this time! I'll learn from this mistake")
                    XWins(pastMoves,pastGames)
                    gameState = False
                else:
                    if TieGame(board):
                        print("The game is a tie. Good game")
                        gameState = False
                    else:
                        print("Good move. My turn.")
                        print(" ")
                        move = gameAI(board,compTurn,pastMoves,pastGames)
                        playIt(board,move,compTurn)
                        boardMaker(board)
                        if checkWinner(board, compTurn):
                            print("I win this time! I'm becoming too smart for ya!")
                            XLoses(pastMoves,pastGames)
                            gameState = False
                        else:
                            if TieGame(board):
                                print("The game is a tie. Good game")
                                gameState = False
            else:
                print("My turn")
                print(" ")
                move = gameAI(board,compTurn,pastMoves,pastGames)
                playIt(board,move,compTurn)
                boardMaker(board)
                if checkWinner(board, compTurn):
                    print("I win this time! I'm becoming too smart for ya!")
                    XWins(pastMoves,pastGames)
                    gameState = False
                else:
                    if TieGame(board):
                        print("The game is a tie. Good game")
                        gameState = False
                
                    else:
                        move = playerMove(board,pastMoves,pastGames)
                        playIt(board,move,playerTurn)
                        pastMoves.append(move)
                        boardMaker(board)
                        if checkWinner(board, playerTurn):
                            print("You win this time! I'll learn from this mistake")
                            XLoses(pastMoves,pastGames)
                            gameState = False
                        else:
                            if TieGame(board):
                                print("The game is a tie. Good game")
                                gameState = False
        if not playAgain():
            break
    pickle_out = open("tictacdata.pickle","wb")
    pickle.dump(pastGames,pickle_out)
main()
                        

                    
                
        
        







