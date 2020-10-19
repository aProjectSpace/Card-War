import tkinter as tk
import random as r

playerName, playerName2 = False, False
bot = False
rmdCards, checkCards = [[], []], [["", "", ""], ["", "", ""]]

def setBotOrPlayer(v):
    global botOrPlayer
    botOrPlayer = v

def gR():
    return r.randint(0,12)

def getNumber(plr):
    ran = gR()
    for i in rmdCards[plr]:
        if (i == ran):
            return getNumber(plr)
    rmdCards[plr].append(ran)
    return ran

def pickBetweenThreeNumber(plr):
    r0, r1, r2 = checkCards[plr][0], checkCards[plr][1], checkCards[plr][2]
    if (type(r0) != int):
        r0 = False
    if (type(r1) != int):
        r1 = False
    if (type(r2) != int):
        r2 = False
        
    if (r0 == False):
        r0 = gR()
        for i in rmdCards[plr]:
            if (i == r0):
                return pickBetweenThreeNumber(plr)
    if (r1 == False):
        r1 = gR()
        for i in rmdCards[plr]:
            if (i == r1):
                return pickBetweenThreeNumber(plr)
    if (r2 == False):
        r2 = gR()
        for i in rmdCards[plr]:
            if (i == r2):
                return pickBetweenThreeNumber(plr)
    return r0 or -1, r1 or -1, r2 or -1

def executeIt():
    r0, r1, rS0, rS1 = getNumber(0), getNumber(0), getNumber(1), getNumber(1)
    print(str(r0) + "    " + str(r1) + "    " + str(rS0) + "    " + str(rS1))
    a, b, c = pickBetweenThreeNumber(0)
    print(str(a) + "    " + str(b) + "    " + str(c))

#def whoWon(fPlrCards, secPlrCards):
