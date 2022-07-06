from asyncore import write
from operator import le
from random import randint, random, shuffle
from textwrap import fill
from tkinter import font, scrolledtext
import random
from unicodedata import name
from attr import has
from tkinter import *
from tkinter import messagebox

from numpy import size

window=Tk()
i = 270
j = 200

def change_pose():
    j = randint(randint(170,190), randint(210,230))
    i = randint(randint(230,260),randint(290,350))
    no_btn.place(x=i, y=j)

def said_yes():
    messagebox.showinfo('hands up!','    i knew it!  :p    ')


label=Label(window, text='are you a bot?', fg='black', font=("Helvetica", 24))
label.place(x=95, y=50)

no_btn = Button(window, text= "NO", command=change_pose)
no_btn.place(x=i, y=j)

yes_btn = Button(window, text= "YES", command=said_yes)
yes_btn.place(x=90, y=200)






window.title('human verification')
window.geometry("400x300+10+10")
window.mainloop()