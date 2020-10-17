import random as r

x = False
who = False
board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""]

def print_board():
    print("\n "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("---|---|---")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("---|---|---")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")

def mtr(msg):
    global x
    global who
    print_board()
    print(msg)
    x = False
    for i in range(0, 10):
        board[i]=str(i)
    who = False

def genNum():
    if(board[1]=="1"and board[2]=="x"and board[3]=="x"):
        return 1
    elif(board[1]=="x"and board[2]=="2"and board[3]=="x"):
        return 2
    elif(board[1]=="x"and board[2]=="x"and board[3]=="3"):
        return 3
    elif(board[4]=="4"and board[5]=="x"and board[6]=="x"):
        return 4
    elif(board[4]=="x"and board[5]=="5"and board[6]=="x"):
        return 5
    elif(board[4]=="x"and board[6]=="x"and board[6]=="6"):
        return 6
    elif(board[7]=="7"and board[8]=="x"and board[9]=="x"):
        return 7
    elif(board[7]=="x"and board[8]=="8"and board[9]=="x"):
        return 8
    elif(board[7]=="x"and board[8]=="x"and board[9]=="9"):
        return 9
    elif(board[1]=="1"and board[4]=="x"and board[7]=="x"):
        return 1
    elif(board[1]=="x"and board[4]=="4"and board[7]=="x"):
        return 4
    elif(board[1]=="x"and board[4]=="x"and board[7]=="7"):
        return 7
    elif(board[2]=="2"and board[5]=="x"and board[8]=="x"):
        return 2
    elif(board[2]=="x"and board[5]=="5"and board[8]=="x"):
        return 5
    elif(board[2]=="x"and board[5]=="x"and board[8]=="8"):
        return 8
    elif(board[3]=="3"and board[6]=="x"and board[9]=="x"):
        return 3
    elif(board[3]=="x"and board[6]=="6"and board[9]=="x"):
        return 6
    elif(board[3]=="x"and board[6]=="x"and board[9]=="9"):
        return 9
    elif(board[1]=="1"and board[5]=="x"and board[9]=="x"):
        return 1
    elif(board[1]=="x"and board[5]=="5"and board[9]=="x"):
        return 5
    elif(board[1]=="x"and board[5]=="x"and board[9]=="9"):
        return 9
    elif(board[3]=="3"and board[5]=="x"and board[7]=="x"):
        return 3
    elif(board[3]=="x"and board[5]=="5"and board[7]=="x"):
        return 5
    elif(board[3]=="x"and board[5]=="x"and board[7]=="7"):
        return 7
    else:
        num = r.randint(1,9)
        if(board[num]!="x" and board[num]!="o"):
            return num
        else:
            return genNum()

def checkWin():
    a = "\n"+x+" has won the round.\nGo for an another round!"
    if((board[1]=="x" and board[2]=="x" and board[3]=="x")or(board[4]=="x" and board[5]=="x" and board[6]=="x")or(board[7]=="x" and board[8]=="x" and board[9]=="x")or(board[1]=="x" and board[4]=="x" and board[7]=="x")or(board[2]=="x" and board[5]=="x" and board[8]=="x")or(board[3]=="x" and board[6]=="x" and board[9]=="x")or(board[1]=="x" and board[5]=="x" and board[9]=="x")or(board[3]=="x" and board[5]=="x" and board[7]=="x")):
        mtr(a)
    elif((board[1]=="o" and board[2]=="o" and board[3]=="o")or(board[4]=="o" and board[5]=="o" and board[6]=="o")or(board[7]=="o" and board[8]=="o" and board[9]=="o")or(board[1]=="o" and board[4]=="o" and board[7]=="o")or(board[2]=="o" and board[5]=="o" and board[8]=="o")or(board[3]=="o" and board[6]=="o" and board[9]=="o")or(board[1]=="o" and board[5]=="o" and board[9]=="o")or(board[3]=="o" and board[5]=="o" and board[7]=="o")):
        mtr(a)
    else:
        if(board[1]!="1"and board[2]!="2"and board[3]!="3"and board[4]!="4"and board[5]!="5"and board[6]!="6"and board[7]!="7"and board[8]!="8"and board[9]!="9"):
            mtr("It's a TIE")

def management():
    global x
    global who
    if (not who):
        who = str(input("\nPick 'AI' to play with a bot or 'players' to play with someone else.\n"))
        while (who!="AI" and who!="players"):
            who = input("\nI told you to pick or 'AI' or 'players', can't you just type it?\n")
            if (who=="players" or who=="AI"):
                break
    if (not x):
        x="x"
    choice = int(input("\nPlease, pick a nombre between 1 and 9 as "+x+" gets remplaced by the nombre.\n"))
    if(board[choice]!="x" and board[choice]!="o"):
        board[choice]=x
        checkWin()
        if (who == "AI"):
            board[genNum()]="o"
        else:
            if(x=="x"):
                x="o"
            else:
                x="x"
    else:
        print("Sorry, this place is occupied")

while True:
    print_board()
    management()
