import time
import os
import winsound as ws
from threading import Timer
import mainFile

msg = ["Weird person: You! You don't look like a peasant. Take a seat and have some ale, might consider sharing your story with me? And please, ignore my accent.\n",
"Me: Very well. I was a guard in the palace, they conspired against me once I didn't accept their deal to smuggle goods.\n",
"Weird person: What did the queen do?\n",
"Me: She didn't even do an investigation. Seems fate wants me to roam the outside world.\n",
"Weird person: Or not. Join the event. Win and the queen will grant you any wish aslong it doesn't touch her position.\n",
"Me: What is that event like?\n",
"Weird person: Card battle, although it's a bit weird. The cards can... move.\n",
"Me: Cards? Move? You are drunk.\n",
"Weird person: Huh, just listen! The number of the cards are their speed. First round each one will receive two cards. There're no identical. You can pick a card or two, of course if you pick two cards on the same race their speed will be equal to their sum, max cards you can use in a race is three. Who wins may pick a one of three cards. Then the winner will receive the card he picked plus two random cards and the loser shall receive three random cards. What comes after is that you've to win most races as each one gives a point to the winner. The winner is who has the most points.\n",
"Me: Game of luck?\n",
"Weird person: Luck? Let's see what fate has for you. Go! The event is today. It's free to participate and who loses doesn't pay a thing.\n",
"Me: What do I have to lose? Guess lollygagging is allowed now.\n",
"Weird person: May he who is known as *I am* lighten your path.\n"]

def startGame():
    mainFile.startGame()

def launchTimer(num):
    global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13
    if (num == 0):
        t0.start()
    elif (num == 1):
        t1.start()
    elif (num == 2):
        t2.start()
    elif (num == 3):
        t3.start()
    elif (num == 4):
        t4.start()
    elif (num == 5):
        t5.start()
    elif (num == 6):
        t6.start()
    elif (num == 7): 
        t7.start()
    elif (num == 8): 
        t8.start()
    elif (num == 9):
        t9.start()
    elif (num == 10):
        t10.start()
    elif (num == 11):
        t11.start()
    elif (num == 12): 
        t12.start()
        lwT.start()

def messages(num, sound):
    print(msg[num])
    if (num != 12):
        launchTimer(num+1)
    if (sound):
        ws.PlaySound(os.getcwd()+"/"+sound, ws.SND_NODEFAULT)

t0 = Timer(1.0, messages, (0, "ikSnd/innkeeper1.wav"))
t1 = Timer(12.5, messages, (1, "meSnd/me1.wav"))
t2 = Timer(8.8, messages, (2, "ikSnd/innkeeper2.wav"))
t3 = Timer(2.5, messages, (3, "meSnd/me2.wav"))
t4 = Timer(7.5, messages, (4, "ikSnd/innkeeper3.wav"))
t5 = Timer(8.5, messages, (5, "meSnd/me3.wav"))
t6 = Timer(2.5, messages, (6, "ikSnd/innkeeper4.wav"))
t7 = Timer(7.5, messages, (7, "meSnd/me4.wav"))
t8 = Timer(4.5, messages, (8, "ikSnd/innkeeper5.wav"))
t9 = Timer(47.5, messages, (9, "meSnd/me5.wav"))
t10 = Timer(1.8, messages, (10, "ikSnd/innkeeper6.wav"))
t11 = Timer(9.5, messages, (11, "meSnd/me6.wav"))
t12 = Timer(5.8, messages, (12, "ikSnd/innkeeper7.wav"))
lwT = Timer(12.5, startGame)
