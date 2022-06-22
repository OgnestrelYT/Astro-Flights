import csv
import os
import sys
from tkinter import *

global list
w = Tk()
w.title("Minecraft")
mf = Frame(w)
mf.grid(column=0, row=0, sticky=(N, W, E, S))
w.columnconfigure(0, weight=1)
w.rowconfigure(0, weight=1)


def back(*args):
    quit()


rec = str

with open("leaderboard.csv", "r") as f:
    reader = csv.DictReader(f)
    fin = ""

    res = {}

    for i in reader:
        score = i["score"]
        username = i["name"]
        if username not in res:
            res[username] = score
        if username in res and int(score) > int(res[username]):
            res[username] = score


    res = sorted(res.items(), key=lambda item: int(item[1]), reverse=True)

    for el in res:
        fin += str(el) + "\n"

Label(mf, text=fin).grid(column=1, row=1, sticky=W)

ex = Button(mf, text="Назад", command=back)
ex.grid(column=1, row=2, sticky=(E, W))

w.mainloop()
