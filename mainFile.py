from PIL import ImageTk
import os
from functools import partial
import introduction as intro
from threading import Timer
import tkinter as tk
import random as r


createLaunchWindowRoot = False
createGameWindowRoot = False
firstTimeFirstPlayerWins = True
points = [0, 0]
cardAvailable = [[False, False, False, False, False, False, False, False, False, False, False, False, False, False], [True, False, False, False, False, False, False, False, False, False, False, False, False, False]]
cardPicked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
removeCards = [[], [0]]

def getRandomNumber():
    return r.randint(0,13)

def startGame():
    createGameWin()

def getNumber(plr):
    ran = getRandomNumber()
    for i in removeCards[plr]:
        if (i == ran):
            return getNumber(plr)
    removeCards[plr].append(ran)
    return ran

def pickBetweenThreeNumber():
    cP = input("You've WON the first round! Exclusively you can pick 1 of three cards! Pick between: 13, 7 and 10\n")
    print("I don't care what you picked! Did you actually believe we'll let you win by picking a free number??")

def addCards(firstTimeGettingCards):
    txt = "You've had the cards: "
    if (firstTimeGettingCards):
        a = getNumber(0)
        b = getNumber(0)
        addCard(0, [a, b])
        addCard(1, [getNumber(1), getNumber(1)])
        print("You've received the cards: "+str(a)+" and "+str(b)+"!\n")
        return
    global firstTimeFirstPlayerWins
    if (firstTimeFirstPlayerWins):
        a = 0
        b = 0
        c = 0
        num = -1
        for i in cardAvailable[0]:
            num = num + 1
            if (i and (num != a or num != b or num != c)):
                txt = txt+str(num)+" "
        pickBetweenThreeNumber()
        a, b, c =  getNumber(0), getNumber(0), getNumber(0)
        addCard(0, [a, b, c])
        addCard(1, [getNumber(1), getNumber(1), getNumber(1)])
        firstTimeFirstPlayerWins = False
        print(txt+"; And you received: "+str(a)+", "+str(b)+", "+str(c)+"!\n")
    else:
        num = -1
        for i in cardAvailable[0]:
            num = num + 1
            if (i):
                txt = txt+str(num)+" "
        a = getNumber(0)
        addCard(0, [a])
        addCard(1, [getNumber(1)])
        print(txt+"; And you received: "+str(a)+"!\n")
#______________________________________________________________________________________________________________________________________
def createLaunchWin():
    global createLaunchWindowRoot
    master = tk.Tk()
    createLaunchWindowRoot = master
    master.geometry("226x60")
    master.title("Card Battle!")
    startGameBut = tk.Button(master, text="Start Game", fg="blue", command=startInto)
    startGameBut.pack(side="top")
    quitGameBut = tk.Button(master, text="Quit", fg="red", command=master.destroy)
    quitGameBut.pack(side="bottom")

def startInto():
    global createLaunchWindowRoot
    intro.launchTimer(0)
    createLaunchWindowRoot.destroy()

def pickCard(but, num):
    global cardAvailable
    if (cardAvailable[0][num] == False):
        print("Hey don't touch me! You don't have me.\n")
        return
    a = False
    if (but["text"] == "Remove"):
        but["text"] = "Pick Me"
        print("You dare question my number?!\n")
        a = True
    else:
        but["text"] = "Remove"
        print("I'll be as fast as my number!\n")
    if (a):
        b = -1
        for i in cardAvailable[0]:
            b = b + 1
            if (b == num):
                cardPicked[b] = False
    else:
        b = -1
        for i in cardAvailable[0]:
            b = b + 1
            if (b == num):
                cardPicked[b] = True

def addPointToScore(who):
    global points
    global createGameWindowRoot
    points[who] = points[who]+1
    print("The scores are "+str(points[0])+" for Player and "+str(points[1])+" for Bot. Hail User! Hail Processeur.\n")
    if (points[0] == 3):
        print("Player WINS!")
        createGameWindowRoot.destroy()
        return
    elif(points[1] == 3):
        print("Bot WINS!")
        createGameWindowRoot.destroy()
        return
    addCards(False)

def startRound():
    global cardPicked
    plrColumn = -1
    botColumn = -1
    checkIfHeUsedACard = False
    player = 0
    botTable = []
    bot = 0
    for i in cardPicked:
        plrColumn = plrColumn + 1
        if (i):
            cardAvailable[0][plrColumn] = False
            checkIfHeUsedACard = True
            player = player + plrColumn
    if (checkIfHeUsedACard == False):
        print("Pick at least 1 card! We need card fuel!")
        return
    for i in cardAvailable[1]:
        botColumn = botColumn + 1
        if (i):
            botTable.append(botColumn)
    for i in botTable:
        bot = bot + i
        cardAvailable[1][i] = False
        if (firstTimeFirstPlayerWins):
            if (bot < player):
                break
        else:
            if (bot > player):
                break

    if (player>bot or player==bot):
        addPointToScore(0)
    else:
        if (firstTimeFirstPlayerWins):
            addPointToScore(0)
        else:
            addPointToScore(1)
    cardPicked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]

def addCard(who, cTbl):
    global cardAvailable
    for i in cTbl:
        cardAvailable[who][i] = True

def createGameWin():
    global createGameWindowRoot

    master = tk.Tk()
    createGameWindowRoot = master
    master.geometry("800x600")
    master.title("Card Battle!")
    master.resizable(False, False)
    c0 = ImageTk.PhotoImage(file = os.getcwd()+"/images/0.png")
    c1 = ImageTk.PhotoImage(file = os.getcwd()+"/images/1.png")
    c2 = ImageTk.PhotoImage(file = os.getcwd()+"/images/2.png")
    c3 = ImageTk.PhotoImage(file = os.getcwd()+"/images/3.png")
    c4 = ImageTk.PhotoImage(file = os.getcwd()+"/images/4.png")
    c5 = ImageTk.PhotoImage(file = os.getcwd()+"/images/5.png")
    c6 = ImageTk.PhotoImage(file = os.getcwd()+"/images/6.png")
    c7 = ImageTk.PhotoImage(file = os.getcwd()+"/images/7.png")
    c8 = ImageTk.PhotoImage(file = os.getcwd()+"/images/8.png")
    c9 = ImageTk.PhotoImage(file = os.getcwd()+"/images/9.png")
    c10 = ImageTk.PhotoImage(file = os.getcwd()+"/images/10.png")
    c11 = ImageTk.PhotoImage(file = os.getcwd()+"/images/11.png")
    c12 = ImageTk.PhotoImage(file = os.getcwd()+"/images/12.png")
    c13 = ImageTk.PhotoImage(file = os.getcwd()+"/images/13.png")

    can = tk.Canvas(master, bg="black", height=600, width=800)
    img = ImageTk.PhotoImage(file = os.getcwd()+"/images/bckRnd.png")
    can.create_image(400, 350, image=img)
    can.pack(side="bottom")

    can0 = tk.Canvas(master, bg="black", height=90, width=48)
    can0.create_image(25, 33, image=c0)
    can0.place(x=71, y=3)

    can1 = tk.Canvas(master, bg="black", height=90, width=48)
    can1.create_image(25, 33, image=c1)
    can1.place(x=123, y=3)

    can2 = tk.Canvas(master, bg="black", height=90, width=48)
    can2.create_image(25, 33, image=c2)
    can2.place(x=175, y=3)

    can3 = tk.Canvas(master, bg="black", height=90, width=48)
    can3.create_image(25, 33, image=c3)
    can3.place(x=227, y=3)

    can4 = tk.Canvas(master, bg="black", height=90, width=48)
    can4.create_image(25, 33, image=c4)
    can4.place(x=279, y=3)

    can5 = tk.Canvas(master, bg="black", height=90, width=48)
    can5.create_image(25, 33, image=c5)
    can5.place(x=331, y=3)

    can6 = tk.Canvas(master, bg="black", height=90, width=48)
    can6.create_image(25, 33, image=c6)
    can6.place(x=383, y=3)

    can7 = tk.Canvas(master, bg="black", height=90, width=48)
    can7.create_image(25, 33, image=c7)
    can7.place(x=435, y=3)

    can8 = tk.Canvas(master, bg="black", height=90, width=48)
    can8.create_image(25, 33, image=c8)
    can8.place(x=487, y=3)

    can9 = tk.Canvas(master, bg="black", height=90, width=48)
    can9.create_image(25, 33, image=c9)
    can9.place(x=539, y=3)

    can10 = tk.Canvas(master, bg="black", height=90, width=48)
    can10.create_image(25, 33, image=c10)
    can10.place(x=591, y=3)

    can11 = tk.Canvas(master, bg="black", height=90, width=48)
    can11.create_image(25, 33, image=c11)
    can11.place(x=642, y=3)

    can12 = tk.Canvas(master, bg="black", height=90, width=48)
    can12.create_image(25, 33, image=c12)
    can12.place(x=694, y=3)

    can13 = tk.Canvas(master, bg="black", height=90, width=48)
    can13.create_image(25, 33, image=c13)
    can13.place(x=745, y=3)

    goBut = tk.Button(master, text="Go!", bg="black", fg="red", width=8, height=2, command=startRound).place(x=4, y=3)
    quitBut = tk.Button(master, text="Quit", bg="black", fg="red", width=8, height=2, command=createGameWindowRoot.destroy).place(x=4, y=57)
    
    cBut0 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut0["command"] = partial(pickCard, cBut0, 0)
    cBut0.place(x=71, y=68)

    cBut1 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut1["command"] = partial(pickCard, cBut1, 1)
    cBut1.place(x=123, y=68)

    cBut2 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut2["command"] = partial(pickCard, cBut2, 2)
    cBut2.place(x=175, y=68)

    cBut3 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut3["command"] = partial(pickCard, cBut3, 3)
    cBut3.place(x=227, y=68)

    cBut4 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut4["command"] = partial(pickCard, cBut4, 4)
    cBut4.place(x=279, y=68)

    cBut5 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut5["command"] = partial(pickCard, cBut5, 5)
    cBut5.place(x=331, y=68)

    cBut6 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut6["command"] = partial(pickCard, cBut6, 6)
    cBut6.place(x=383, y=68)

    cBut7 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut7["command"] = partial(pickCard, cBut7, 7)
    cBut7.place(x=435, y=68)

    cBut8 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut8["command"] = partial(pickCard, cBut8, 8)
    cBut8.place(x=487, y=68)

    cBut9 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut9["command"] = partial(pickCard, cBut9, 9)
    cBut9.place(x=539, y=68)

    cBut10 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut10["command"] = partial(pickCard, cBut10, 10)
    cBut10.place(x=591, y=68)

    cBut11 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut11["command"] = partial(pickCard, cBut11, 11)
    cBut11.place(x=642, y=68)

    cBut12 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut12["command"] = partial(pickCard, cBut12, 12)
    cBut12.place(x=694, y=68)

    cBut13 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut13["command"] = partial(pickCard, cBut13, 13)
    cBut13.place(x=745, y=68)
    addCards(True)
    master.mainloop()

createLaunchWin()
