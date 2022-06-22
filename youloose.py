import os
from tkinter import *

w = Tk()
w.title("Minecraft")
mf = Frame(w)
mf.grid(column=0, row=0, sticky=(N, W, E, S))
w.columnconfigure(0, weight=1)
w.rowconfigure(0, weight=1)


def restart(*args):
    os.system('python main.py')


def exit(*args):
    quit()


res = Button(mf, text="Перезайти", command=restart)
res.grid(column=1, row=1, sticky=(E, W))

ex = Button(mf, text="Выйти", command=exit)
ex.grid(column=1, row=2, sticky=(E, W))


w.mainloop()