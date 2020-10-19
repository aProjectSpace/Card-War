import tkinter as tk
import random as r

rmdCards, checkCards = [], [False, False, False]]

def gR():
    return r.randint(0,12)

def getNumber():
    ran = gR()
    for i in rmdCards:
        if (i == ran):
            return getNumber()
    rmdCards.append(ran)
    return ran

def pickBetweenThreeNumber():
    r0, r1, r2 = checkCards[0], checkCards[1], checkCards[2]
    if (r0 == False):
        r0 = gR()
        for i in rmdCards:
            if (i == r0):
                return pickBetweenThreeNumber()
    if (r1 == False):
        r1 = gR()
        for i in rmdCards:
            if (i == r1):
                return pickBetweenThreeNumber()
    if (r2 == False):
        r2 = gR()
        for i in rmdCards:
            if (i == r2):
                return pickBetweenThreeNumber()
    return r0 or -1, r1 or -1, r2 or -1

def startGame():
    r0, r1, rS0, rS1 = getNumber(), getNumber()
    a, b, c = pickBetweenThreeNumber()

#def whoWon(fPlrCards, secPlrCards):
