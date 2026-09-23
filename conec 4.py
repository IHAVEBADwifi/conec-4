class Board:
    def __init__(self):
        self.boardarray = [[" " for i in range(7)] for j in range(6)]
        self.player = ["X","O"]

    def printboard(self):
        for i in self.boardarray:
            print(i)
            
    def addcounter(self,row,turn):
        for i in range(5,-1,-1):
            if self.boardarray[i][row] == " ":
                self.boardarray[i][row] = self.player[turn]
                return i
    
    def fullcheck(self):
        for i in range(6):
            for j in range(7):
                if self.boardarray[i][j] == " ":
                    return False
        return True
    
    def vertcheck(self,row,turn):
        consec = 0
        for i in range(6):
            if self.boardarray[i][row] == self.player[turn]:
                consec +=1
                if consec >=4:
                    return True
            else:
                consec = 0
        return False
    
    def horizcheck(self,yaxis,turn):
        consec = 0
        for i in range(7):
            if self.boardarray[yaxis][i] == self.player[turn]:
                consec +=1
                if consec >= 4:
                    return True
            else:
                consec = 0
        return False

    def diagcheck(self,row,yaxis,turn):
        yfrombottom = abs(5-yaxis)
        something = row -yfrombottom
        consec = 0
        for i in range(something,7):
            if self.boardarray[i-1][5-(i-something-1)] == self.player[turn]:
                consec += 1
                if consec >= 4:
                    return True
                else:
                   consec = 0
        
        consec = 0
        topx = max(row-yaxis,0)
        topy = max(yaxis-row,0)
        yfrombottom = abs(5-yaxis)
        bottomx = min(row+yfrombottom,6)
        for i in range(topx,bottomx+1):
            if self.boardarray[topy + (i-topx)][i] == self.player[turn]:
                consec+= 1
                if consec >= 4:
                    return True
            else:
                consec = 0



        return False

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 0
        self.active = True

    def changeturn(self):
        if self.turn == 0:
            self.turn = 1
            print("Player 2's Turn")
        else:
            self.turn = 0
            print("Player 1's Turn")
    
    def get_move(self):
        valid = False
        while valid == False:
            row = input("Which row would you like to drop a tile in")
            if row.isnumeric():
                row = int(row)
                if row <= 7 and row >= 1:
                    if self.board.boardarray[0][row-1] == " ":
                        valid = True
                        return row -1
                    else:   
                        print("Invalid input, the row is full, please enter another number")
                else:
                    print("Invalid input, please enter a number from 1 to 7")
            else:
                print("Invalid input, please enter a number")
            
    
    def wincheck(self,horizcon,vertcon,diagcon):
        if horizcon == True or vertcon == True or diagcon == True:
            if self.turn == 1:
                print("Player 2 Wins")
            else:
                print("Player 1 wins")
            self.active = False

    def drawcheck(self,isfull,horizcon,vertcon,diagcon):
        if isfull == True and horizcon == False and vertcon == False and diagcon == False:
            print("It is a Draw")
            self.active = False

activegame = Game()
while activegame.active == True:

    move = activegame.get_move()
    yaxis = activegame.board.addcounter(move,activegame.turn)
    vertcon = activegame.board.vertcheck(move,activegame.turn)
    horizcon = activegame.board.horizcheck(yaxis,activegame.turn)
    diagcon = activegame.board.diagcheck(move,yaxis,activegame.turn)
    activegame.wincheck(horizcon,vertcon,diagcon)
    isfull = activegame.board.fullcheck()
    activegame.drawcheck(isfull,horizcon,vertcon,diagcon)
    activegame.board.printboard()
    if activegame.active == True:
        activegame.changeturn()
