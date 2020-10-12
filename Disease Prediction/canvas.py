#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:57:05 2020

@author: nishant
"""


from tkinter import *
import random
import time

index=1
def c():
    s="#"
    for i in range(6):
        a=random.randrange(0,16)
        s+=l[a]
    cv.config(bg=s)
    lb.config(text=s,bg=s,font=("Elephant", 30))
    print(s)
        
    
l=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
Frame = Tk()
Frame.title("Colors")
Frame.geometry('1200x800')
color='#ffffff'
cv = Label(Frame,width=1200,height=800,bg=color)
cv.place(x=2,y=2)

lb = Label(Frame,text="#ffffff")
lb.place(x=2,y=2)


color = list(color)
#time.sleep(2)
#time.sleep(3)

#cv.config(bg="#ff0000")
btn2 = Button(Frame, text="c",command=c,bg="#aaff00")
btn2.place(x=650, y = 300)
Frame.mainloop()