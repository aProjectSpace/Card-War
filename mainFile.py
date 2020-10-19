import tkinter as tk
import exports as ex
import introduction as intro

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.startGame = tk.Button(self, text="Start Game", fg="blue", command=self.launchGame)
        self.startGame.pack(side="top")

        self.option = tk.Button(self, text="AI", fg="grey", command=self.changeText)
        self.option.pack()
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def launchGame(self):
        intro.launchTimer(0)
        if (self.option["text"] == "AI"):
            ex.setBotOrPlayer(True)
        self.master.destroy()

    def changeText(self):
        if (self.option["text"] == "AI"):
            self.option["text"] = "2 Player"
        else:
            self.option["text"] = "AI"

root = tk.Tk()
app = Application(master=root)
app.mainloop()