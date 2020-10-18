import time
import os
import winsound as ws

num = 0
timer = time.time()

msg = [ ["Innkeeper: Huh..? You don't look like a peasant. Take a seat and have some ale, if you don't mind I would like to listen to your story.", 12, "innkeeper1.wav"],
["Me: Very well. I was a guard in the palace, they conspired against me once I didn't accept their deal to smuggle goods.", 10, "me1.wav"],
["Innkeeper: What did the queen do?", 5, "innkeeper2.wav"],
["Me: She didn't even do an investigation! Seems fate wants me to roam the outside world.", 8, "me2.wav"],
["Innkeeper: Or not. Join the event. Win and the queen will grant you any wish aslong it doesn't touch her position.", 9, "innkeeper3.wav"],
["Me: What's the game like?", 4, "me3.wav"],
["Innkeeper: Card battle, although it's a bit weird. The cards can... move.", 7, "innkeeper4.wav"],
["Me: Cards? Move? You are drunk.", 5, "me4.wav"],
["Innkeeper: Huh, just listen! The number of the cards are their speed. First round each one will receive two cards. You can pick a card or two, of course if you pick two cards on the same race their speed will be equal to their sum, max cards you can use in a race is three. Who wins may pick a one of three cards. Then the winner will receive the card he picked plus two random cards and the loser shall receive three random cards. What comes after is that you've to win most races as each one gives a point to the winner. The winner is who has the most points.", 40, "innkeeper5.wav"],
["Me: Game of luck, ey?", 4, "me5.wav"],
["Innkeeper: Luck? Let's see what fate has for you. Go! The event is today. It's free to participate and who loses doesn't pay a thing.", 11, "innkeeper6.wav"],
["Me: What do I have to lose? Guess lollygagging is allowed now.", 6, "me6.wav"],
["Innkeeper: May he who is known as *I am* lighten your path.", 7, "innkeeper7.wav"] ]

def sendMsg():
    global num
    global timer
    if (num == 0):
        print (msg[num+1])
    #else:
        #while(num < 13):
