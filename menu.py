import csv
import os
import sys
from tkinter import *
from idk import *


w = Tk()
w.title("Minecraft")
mf = Frame(w)
mf.grid(column=0, row=0, sticky=(N, W, E, S))
w.columnconfigure(0, weight=1)
w.rowconfigure(0, weight=1)


def start(*args):
    global username, usernamestr
    usernamestr = username.get()
    with open("username.txt", "w") as f:
        f.write(usernamestr)
    # with open("leaderboard.csv", "a", newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=fields)
    #     writer.writerow({'name': usernamestr})

    os.system('python main.py')


def exit(*args):
    quit(10)


def records(*args):
    os.system('python records.py')



st = Button(mf, text="Старт", command=start)
st.grid(column=1, row=1, sticky=(E, W))

ex = Button(mf, text="Выйти", command=exit)
ex.grid(column=1, row=2, sticky=(E, W))

username = StringVar()
username_e = Entry(mf, width=40, textvariable=username)
username_e.grid(column=2, row=1, sticky=(W, E))

ex = Button(mf, text="Рейтинг", command=records)
ex.grid(column=2, row=2, sticky=(E, W))

# sys.stdout.write(str(username))

w.mainloop()