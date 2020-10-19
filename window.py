import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.option = tk.Button(self, text="AI", fg="green", command=self.changeText)
        self.option.pack()
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def changeText(self):
        print(self.option.config('text')[4])
        if (self.option.configure('text') == "AI"):
            self.option.configure(text="2 Player")
        else:
            self.option.configure(text="AI")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
