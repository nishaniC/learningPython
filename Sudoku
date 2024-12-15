# Sudoku 
# reads 9 rows, each row of the board must contain all digits from 0 to 9 
# reads 9colums, each column of the board must contain all digits from 0 to 9
# each of the nine 3x3 "tiles" of the table must contain all digits from 0 to 9
# userInput = input("please enter the Sudoku to verify: ")
# userInput="295743861431865927876192543387459216612387495549216738763524189928671354154938672"
userInput="195743862431865927876192543387459216612387495549216738763524189928671354254938671"
Sudoku = list(userInput)
print("Sudoku :", Sudoku)
rawS=False
ColumnS=False
tileS=False
SudokuR=[]
SudokuC=[]
SudokuT1=[]
SudokuT2=[]
SudokuT3=[]
SudokuT4=[]
SudokuT5=[]
SudokuT6=[]
SudokuT7=[]
SudokuT8=[]
SudokuT9=[]
equals=0
SetIndex=-1
set=['1','2','3','4','5','6','7','8','9']
print("set :", set)
# breaking down into lists of:
# raws

def brakeIntoTiles(start,end):
    SudokuTM1=[]
    for i in range(start,end+1):
        # print("i: ", i)
        if ((i>=start)and(i<=start+2)):
            SudokuTM1.append(Sudoku[i])
        if((i>=start+9)and(i<=start+11)):
            SudokuTM1.append(Sudoku[i])
        if((i>=start+18)and(i<=start+20)):
            SudokuTM1.append(Sudoku[i])
    # print("SudokuTM1 : ", SudokuTM1)
    return SudokuTM1
    
def checkTiels(tiel):
    global equals
    set=['1','2','3','4','5','6','7','8','9']
    for j in range(0,9):
        if (tiel[j]in set):
            SetIndex = int(tiel[j])-1
            set[SetIndex]+="Y"
            
            equals+=1
        else:
            break

for i in range(0,81,9):
    print("i: ", i)
    SudokuR=Sudoku[i:i+9]
    print("SudokuR : ", SudokuR)
    for j in range(0,9):
        if (SudokuR[j]in set):
            SetIndex = int(SudokuR[j])-1
            set[SetIndex]+="Y"
            equals+=1
        else:
            break
    print("set :", set)
    print("equals :", equals)
    set=['1','2','3','4','5','6','7','8','9']
    print("set :", set)
    if((equals%9)!=0):
        break
    if(equals==81):
        rawS=True
if(rawS):
    print("raws are ok so continuing to check the columns")
    set=['1','2','3','4','5','6','7','8','9']
    for i in range(0,9):
        print("i: ", i)
        SudokuC=Sudoku[i::9]
        print("SudokuC : ", SudokuC)
        for j in range(0,9):
            if (SudokuC[j]in set):
                SetIndex = int(SudokuC[j])-1
                set[SetIndex]+="Y"
                equals+=1
            else:
                break
        print("set :", set)
        print("equals :", equals)
        set=['1','2','3','4','5','6','7','8','9']
        print("set :", set)
        if((equals%9)!=0):
            break
        if(equals==162):
            ColumnS=True
    if (ColumnS):
        print("columns are ok continuing to check the tiles")
        set=['1','2','3','4','5','6','7','8','9']
        SudokuT1=brakeIntoTiles(0,20)
        SudokuT2=brakeIntoTiles(3,23)
        SudokuT3=brakeIntoTiles(6,26)
        SudokuT4=brakeIntoTiles(27,47)
        SudokuT5=brakeIntoTiles(30,50)
        SudokuT6=brakeIntoTiles(33,53)
        SudokuT7=brakeIntoTiles(54,74)
        SudokuT8=brakeIntoTiles(57,77)
        SudokuT9=brakeIntoTiles(60,80)

        print("SudokuT1 : ", SudokuT1)
        print("SudokuT2 : ", SudokuT2)
        print("SudokuT3 : ", SudokuT3)
        print("SudokuT4 : ", SudokuT4)
        print("SudokuT5 : ", SudokuT5)
        print("SudokuT6 : ", SudokuT6)
        print("SudokuT7 : ", SudokuT7)
        print("SudokuT8 : ", SudokuT8)
        print("SudokuT9 : ", SudokuT9)
       
        checkTiels(SudokuT1)
        if((equals%9)!=0):
            print("Tile1 is not a Sudoku so it is not a Sudoku")
        else:
            print("Tile1 is a Sudoku so continuing to check Tile2")
            checkTiels(SudokuT2)
            if((equals%9)!=0):
                print("Tile2 is not a Sudoku so it is is not a Sudoku")
            else:
                print("Tile2 is a Sudoku so continuing to check Tile3")
                checkTiels(SudokuT3)
                if((equals%9)!=0):
                    print("Tile3 is not a Sudoku so it is not a Sudoku")
                else:
                    print("Tile3 is a Sudoku so continuing to check Tile4")
                    checkTiels(SudokuT4)
                    if((equals%9)!=0):
                        print("Tile4 is not a Sudoku so it is not a Sudoku")
                    else:
                        print("Tile4 is a Sudoku so continuing to check Tile5")
                        checkTiels(SudokuT5)
                        if((equals%9)!=0):
                            print("Tile5 is not a Sudoku so it is not a Sudoku")
                        else:
                            print("Tile5 is a Sudoku so continuing to check Tile6")
                            checkTiels(SudokuT6)
                            if((equals%9)!=0):
                                print("Tile6 is not a Sudoku so it is not a Sudoku")
                            else:
                                print("Tile6 is a Sudoku so continuing to check Tile7")
                                checkTiels(SudokuT7)
                                if((equals%9)!=0):
                                    print("Tile7 is not a Sudoku so it is not a Sudoku")
                                else:
                                    print("Tile7 is a Sudoku so continuing to check Tile8")
                                    checkTiels(SudokuT8)
                                    if((equals%9)!=0):
                                        print("Tile8 is not a Sudoku so it is not a Sudoku")
                                    else:
                                        print("Tile8 is a Sudoku so continuing to check Tile9")
                                        checkTiels(SudokuT9)
                                        if((equals%9)!=0):
                                            print("Tile9 is not a Sudoku so it is not a Sudoku")
                                        else:
                                            print("Tile9 is a Sudoku so it is a Sudoku")
    else:
        print("columns are not a Sudoku no need to continue")
        
        
    
else:
    print("raws are not a Sudoku no need to continue")
        
