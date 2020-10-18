import time
import os
import winsound as ws
from threading import Timer

timer = time.time()

msg = ["Innkeeper: Huh..? You don't look like a peasant. Take a seat and have some ale, if you don't mind I would like to listen to your story.\n",
"Me: Very well. I was a guard in the palace, they conspired against me once I didn't accept their deal to smuggle goods.\n",
"Innkeeper: What did the queen do?\n",
"Me: She didn't even do an investigation! Seems fate wants me to roam the outside world.\n",
"Innkeeper: Or not. Join the event. Win and the queen will grant you any wish aslong it doesn't touch her position.\n",
"Me: What's the game like?\n",
"Innkeeper: Card battle, although it's a bit weird. The cards can... move.\n",
"Me: Cards? Move? You are drunk.\n",
"Innkeeper: Huh, just listen! The number of the cards are their speed. First round each one will receive two cards. You can pick a card or two, of course if you pick two cards on the same race their speed will be equal to their sum, max cards you can use in a race is three. Who wins may pick a one of three cards. Then the winner will receive the card he picked plus two random cards and the loser shall receive three random cards. What comes after is that you've to win most races as each one gives a point to the winner. The winner is who has the most points.\n",
"Me: Game of luck, ey?\n",
"Innkeeper: Luck? Let's see what fate has for you. Go! The event is today. It's free to participate and who loses doesn't pay a thing.\n",
"Me: What do I have to lose? Guess lollygagging is allowed now.\n",
"Innkeeper: May he who is known as *I am* lighten your path.\n"]

def messages(num, sound):
    print(msg[num])
    ws.PlaySound(os.getcwd()+"/"+sound, ws.SND_NODEFAULT)
    if (num != 13):
        t[num+1].start()

t = [ Timer(2.0, messages, (0, "innkeeper1.wav)),
Timer(12.0, messages, (1, "me1.wav")),
Timer(5.0, messages, (2), "innkeeper2.wav"),
Timer(8.0, messages, (3, "me2.wav")),
Timer(9.0, messages, (4, "innkeeper3.wav")),
Timer(4.0, messages, (5, "me3.wav")),
Timer(7.0, messages, (6, "innkeeper4.wav")),
Timer(5.0, messages, (7, "me4.wav")),
Timer(40.0, messages, (8, "innkeeper5.wav")),
Timer(4.0, messages, (9, "me5.wav")),
Timer(11.0, messages, (10, "innkeeper6.wav")),
Timer(6.0, messages, (11, "me6.wav")),
Timer(7.0, messages, (12, "innkeeper7.wav"))]

t[0].start()
