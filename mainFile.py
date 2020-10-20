from PIL import ImageTk #To load images into the window
import os #to check using os.getcwd() where the folder path
from functools import partial #To add arguments 
import introduction as intro #To launch first msg and audio after pressing startGame
import tkinter as tk
import random as r


createGameWindowRoot = False #To destroy game window on game finishs
firstTimeFirstPlayerWins = True #Added it so Player wins Bot at first time for a special event
points = [0, 0] #Scors of Player and Bot..
#To check if a player has these cards. He can't pick a card which he doesn't have.
cardAvailable = [[False, False, False, False, False, False, False, False, False, False, False, False, False, False], [True, False, False, False, False, False, False, False, False, False, False, False, False, False]]
#To check which card he picked before starting a round
cardPicked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
#No duplicate cards are allowed, so this table is to check which card he has already received
removeCards = [[], [0]]

#To get a random number between 0 and 13
def getRandomNumber():
    return r.randint(0,13)

#To start game window from introduction.py
def startGame():
    createGameWin()

#get a random number for either the player or bot
def getNumber(plr):
    ran = getRandomNumber()
    for i in removeCards[plr]:
        if (i == ran):
            return getNumber(plr)
    removeCards[plr].append(ran)
    return ran

#A small joke, game are all about fun.
def pickBetweenThreeNumberJoke():
    cP = input("You've WON the first round! Exclusively you can pick 1 of three cards! Pick between: 13, 7 and 10\n")
    print("I don't care what you picked! Did you actually believe we'll let you win by picking a free number??")

#Add cards into a player deck.
def addCards(firstTimeGettingCards):#First argument is so players receive 2 cards.
    txt = "You've had the cards: "#main text
    if (firstTimeGettingCards):#A small error appeared used this to avoid it
        a = getNumber(0)
        b = getNumber(0)
        addCard(0, [a, b])
        addCard(1, [getNumber(1), getNumber(1)])
        print("You've received the cards: "+str(a)+" and "+str(b)+"!\n")
        return
    global firstTimeFirstPlayerWins#For the joke.
    if (firstTimeFirstPlayerWins):#For the joke PLUS they will receive 3 cards.
        a = 0
        b = 0
        c = 0
        num = -1#In python tables index starts with 0 because 0 is a card number in this game
        for index in cardAvailable[0]:#To check which cards I already have to add them with the print.
            num = num + 1#Didn't know how to check colums so I used this method.
            if (index):#If index == true
                txt = txt+str(num)+" "#Add card number in print.
        pickBetweenThreeNumberJoke()#The joke.
        a, b, c =  getNumber(0), getNumber(0), getNumber(0)#Get 3 random numbers
        addCard(0, [a, b, c])#add the 3 card into available table for Player
        addCard(1, [getNumber(1), getNumber(1), getNumber(1)])#add 3 card into available table for Player
        firstTimeFirstPlayerWins = False#Disable the joke.
        print(txt+"; And you received: "+str(a)+", "+str(b)+", "+str(c)+"!\n")
    else:#If the joke has already been seen, means they'll receive only 1 card each.
        num = -1#Same method as above
        for i in cardAvailable[0]:
            num = num + 1
            if (i):
                txt = txt+str(num)+" "
        a = getNumber(0)
        addCard(0, [a])
        addCard(1, [getNumber(1)])
        print(txt+"; And you received: "+str(a)+"!\n")
#______________________________________________________________________________________________________________________________________
def createLaunchWin():#Create the first window
    master = tk.Tk() #The window
    master.geometry("226x60")#Geometry which is the window size.
    master.title("Card Battle!")#Window title
    startGameBut = tk.Button(master, text="Start Game", fg="blue", command=partial(startInto, master))#Start Game Button
    startGameBut.pack(side="top")#Set position at top
    quitGameBut = tk.Button(master, text="Quit", fg="red", command=master.destroy)#Quit game button
    quitGameBut.pack(side="bottom")#Set position at bottom

def startInto(master):#To Start Audio/Message of introduction.py and destroy the launch window
    intro.launchTimer(0)
    master.destroy()

def pickCard(but, cardNumber):#On pressing pick card button to add it in cardPicked and add some print texts
    global cardAvailable
    if (cardAvailable[0][cardNumber] == False): #If player doesn't have the card
        print("Hey don't touch me! You don't have me.\n")
        return
    if (but["text"] == "Remove"):
        but["text"] = "Pick Me"
        print("You dare question my number?!\n")
        b = -1
        for i in cardAvailable[0]:
            b = b + 1
            if (b == cardNumber):
                cardPicked[b] = False
    else:
        but["text"] = "Remove"
        print("I'll be as fast as my number!\n")
        b = -1
        for i in cardAvailable[0]:
            b = b + 1
            if (b == cardNumber):
                cardPicked[b] = True

def addPointToScore(who):
    global points #score table
    global createGameWindowRoot #If a winner has been decided to close window
    points[who] = points[who]+1 #add 1 score to the winner's total
    print("The scores are "+str(points[0])+" for Player and "+str(points[1])+" for Bot. Hail User! Hail Processeur.\n")#Score message
    if (points[0] == 3): #if Player has 3 points he wins and close the window
        print("Player WINS!")
        createGameWindowRoot.destroy()
        return
    elif(points[1] == 3): #if bot has 3 points he wins and close the window
        print("Bot WINS!")
        createGameWindowRoot.destroy()
        return
    addCards(False) #To add cards of game didn't end

def startRound(): #Start the round, check if he picked a card, Check who wins.
    global cardPicked #table for which cards the Player has picked
    plrColumn = -1 #Check available cards column
    botColumn = -1 #Check available cards column
    checkIfHeUsedACard = False #To check if he picked a card or no.
    player = 0 #player total card sum, card 5 + card 4 = speed 9!
    botTable = [] #to check what cards does a bot have.
    bot = 0 #bot total card sum.
    for i in cardPicked: #check what cards a player has used and set their column in -> To second line.
        plrColumn = plrColumn + 1 # -> card available table to False: can't use can't twice.
        if (i): #if one of the index(i) is equal to true means he picked a card.
            cardAvailable[0][plrColumn] = False
            checkIfHeUsedACard = True
            player = player + plrColumn
    if (checkIfHeUsedACard == False): #After we've checked if he selected a card, if he didn't send message and return def.
        print("Pick at least 1 card! We need card fuel!")
        return
    for i in cardAvailable[1]: #Check available cards for bot
        botColumn = botColumn + 1
        if (i):
            botTable.append(botColumn)
    for i in botTable:
        bot = bot + i
        cardAvailable[1][i] = False
        if (firstTimeFirstPlayerWins): #To make sure the joke will be seen
            if (bot < player): #If bot total cards number lower than player's the FOR breaks and continues.
                break
        else: #if the joke has passed, we'll make sure that the user will have a hard time.
            if (bot > player):
                break

    if (player>bot or player==bot): #Draw are not accepted. Player wins by default.
        addPointToScore(0) #Add point to Player
    else:
        if (firstTimeFirstPlayerWins): #If a bug made a bot won, will make sure the joke will be seen...
            addPointToScore(0)
        else:
            addPointToScore(1) #If the joke has already been seen, the bot will win.
    #After using the cards, making sure he can't use them again.
    cardPicked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]

def addCard(who, cTbl):#Add card to availabe table so player or bot can use the card.
    global cardAvailable
    for i in cTbl:
        cardAvailable[who][i] = True

def createGameWin(): #Create game window
    global createGameWindowRoot #So we can destroy the window once game finish

    master = tk.Tk() #The window
    createGameWindowRoot = master #So we can destroy the window once game finish
    master.geometry("800x600")#Geometry, window size.
    master.title("Card Battle!")#Window title
    master.resizable(False, False)#Window is not resizable by width or height.
    c0 = ImageTk.PhotoImage(file = os.getcwd()+"/images/0.png") #The card photos
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

    can = tk.Canvas(master, bg="black", height=600, width=800)#The game window canvas.
    img = ImageTk.PhotoImage(file = os.getcwd()+"/images/bckRnd.png")#The background horse race field.
    can.create_image(400, 350, image=img) #Setting the image and it's size.
    can.pack(side="bottom")#Setting position at bottom
#Card's canvases and their image.
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
#Start round button
    goBut = tk.Button(master, text="Go!", bg="black", fg="red", width=8, height=2, command=startRound).place(x=4, y=3)
    quitBut = tk.Button(master, text="Quit", bg="black", fg="red", width=8, height=2, command=master.destroy).place(x=4, y=57)
#Select a card buttons.
    cBut0 = tk.Button(master, text="Pick Me", bg="black", fg="red", width=6, height = 1)
    cBut0["command"] = partial(pickCard, cBut0, 0)#Used partial so we can send arguments with def
    cBut0.place(x=71, y=68)#Set button's width and height position

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
    addCards(True) #Can't start the game if players didn't have card.
    master.mainloop() #render the images.

createLaunchWin()
