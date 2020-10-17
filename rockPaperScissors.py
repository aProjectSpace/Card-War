import tkinter as tk
import random as r
player = False
madman = False
winner = False
withWho = False

def pWin():
    global player
    global madman
    global winner
    if (winner == "player"):
        if (withWho):
            print(".:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-:.\n(☞ﾟヮﾟ)☞ First player won! ☜(ﾟヮﾟ☜)")
        else:
            print(".:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-:.\n(҂‾ ▵‾)︻デ═一 💰 ┌┐∵]┘ The madman got distracted, you've been able to escape!(You've won)")

    elif (winner == "second"):
        if (withWho):
            print(".:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-:.\n(☞ﾟヮﾟ)☞ Second player won! ☜(ﾟヮﾟ☜)")
        else:
            print(".:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-:.\n(҂‾ ▵‾)︻デ═一 (˚▽˚’!)/ The madman killed you.(You've lost)")

    else:
        if (withWho):
            print(".:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-:.\n┬┴┬┴┤≖_≖) ├┬┴┬┴ It's a draw! ー═┻┳︻▄(≖_≖ )")
        else:
            print(".:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-:.\n(╰,╯) The madman looks angry, no one been able to make the same decision he made.(Draw)")

    player = False
    madman = False
    winner = False
    print("\nGo for an another round!\n")

def aCommand():
    global player
    global madman
    if (not player):
        player = "Rock"
        if (not withWho):
            beginTheWar()

    else:
        madman = "Rock"
        beginTheWar()
		
def aCommand2():
    global player
    global madman
    if (not player):
        player = "Paper"
        if (not withWho):
            beginTheWar()

    else:
        madman = "Paper"
        beginTheWar()

def aCommand3():
    global player
    global madman
    if (not player):
        player = "Scissor"
        if (not withWho):
            beginTheWar()

    else:
        madman = "Scissor"
        beginTheWar()

def aCommand4():
    global withWho
    if (withWho):
        withWho = False
        button.configure(text="Two players")
    else:
        withWho = True
        button.configure(text="Play with madman!")

def beginTheWar():
    global winner
    if (not withWho):
        global madman
        n = r.randint(1, 12)
        if ( (n == 3) or (n == 6) or (n == 8) or (n == 11) ):
            madman = "Rock"
        elif ( (n == 1) or (n == 3) or (n == 9) or (n == 12) ):
            madman = "Paper"
        elif ( (n == 2) or (n == 4) or (n == 7) or (n == 10) ):
            madman = "Scissor"
        else:
            madman = "Rock"

    if (player == "Scissor" and madman == "Paper"):
        winner = "player"
        pWin()
    elif(player == "Paper" and madman == "Rock"):
        winner = "player"
        pWin()
    elif(player == "Rock" and madman == "Scissor"):
        winner = "player"
        pWin()
    elif(player == "Scissor" and madman == "Rock"):
        winner = "second"
        pWin()
    elif (player == "Paper" and madman == "Scissor" ):
        winner = "second"
        pWin()
    elif(player == "Rock" and madman == "Paper"):
        winner = "second"
        pWin()
    elif (player == madman):
        winner = False
        pWin()

button = tk.Button(height=4, text="Two players", width=20, command=aCommand4)
button2 = tk.Button(height=4, text="Rock", width=20, command=aCommand)
button3 = tk.Button(height=4, text="Paper", width=20, command=aCommand2)
button4 = tk.Button(height=4, text="Scissor", width=20, command=aCommand3)

button.pack()
button2.pack()
button3.pack()
button4.pack()
