import tkinter as tk
import exports as ex
import introduction as intro

class launchWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start = tk.Button(self, text="Start Game", fg="blue", command=self.startGame)
        self.start.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def startGame(self):
        intro.launchTimer(0)
        self.master.destroy()

class gameWindow(tk.Frame):
    def __init__(self, masterRoot=None):
        super().__init__(masterRoot)
        self.masterRoot = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

    def updates(self):

root = tk.Tk()
lW = launchWindow(master=root)
lW.mainloop()

root2 = tk.Tk()
gW = gameWindow(masterRoot=root2)
gW.mainloop()
