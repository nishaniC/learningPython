from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(len(board)):
        print(board[i])

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeSq = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if ((board[i][j] != 'O') and (board[i][j] != 'X')):
                freeTuple = (i+1,j+1)
                freeSq.append(freeTuple)
    return freeSq
    
def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game
    match = [[board[0][0],board[0][1],board[0][2]],\
    [board[1][0],board[1][1],board[1][2]],\
    [board[2][0],board[2][1],board[2][2]],\
    [board[0][0],board[1][0],board[2][0]],\
    [board[0][1],board[1][1],board[2][1]],\
    [board[0][2],board[1][2],board[2][2]],\
    [board[0][0],board[1][1],board[2][2]],\
    [board[0][2],board[1][1],board[2][0]]]
    a,b,c=0
    for i in range(len(match)):
        a,b,c=match[i]
        if ((a==b) and (b==c) and (c==sign)):
            return True
    return False
            
               
                    

def draw_move(board):
#     # The function draws the computer's move and updates the board.
    free=[]
    free=make_list_of_free_fields(board)
    valueAssigned = False
    if (len(free)!=0):
        cValue=randrange(8)+1
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == cValue):
                    board[i][j] = 'X'
                    valueAssigned = True
                    display_board(board)
                    break
            if(valueAssigned):
                break
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valueAssigned = False
    if (len(make_list_of_free_fields(board))!=0):
        try:
            value=int(input("Please enter your move: "))
            if (value in[1,2,3,4,5,6,7,8,9]):
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if (board[i][j] == value):
                            board[i][j] = 'O'
                            valueAssigned = True
                            display_board(board)
                            break
                    if(valueAssigned):
                        break
            else:
                print("incorrect move please try again")
                enter_move(board)
            if ((len(make_list_of_free_fields(board))!=0)):
                draw_move(board)
                enter_move(board)
        except:
            print("incorrect move please try again")
            enter_move(board)
    else:
        print("array is full")
        if (victory_for(board, 'X')):
            print("The computer has won")
        elif (victory_for(board, 'O')):
            print("You have won")
        else:
            print("It's a draw")
        display_board(board)
        
board = [[1,2,3],[4,'X',6],[7,8,9]]
# board=[['O','X','O'],['X','X','X'],['O','X','O']]
display_board(board)
print(make_list_of_free_fields(board))
print(len(make_list_of_free_fields(board)))
enter_move(board)


                
        







