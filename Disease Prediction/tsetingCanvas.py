#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:59:10 2020

@author: nishant
"""
from tkinter import *

f = Tk()
fname = "bg1.png"
bg_image = PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
f.geometry("%dx%d+50+30" % (w, h))
# size the window so the image will fill it 
#root.geometry("%dx%d+50+30" % (w, h))
root = Canvas(f,width=w, height=h)
root.place(x=2,y=2)
root.create_image(2, 2, image=bg_image, anchor='nw')
# Heading
w2 = Label(f, justify=LEFT, text="Disease Prediction using Machine Learning", fg="white", bg="sky blue")
w2.config(font=("Elephant", 30))
w2.place(x= 350,y=10)
    
fname = "RedCross.png"
logo_image = PhotoImage(file=fname)
# get the width and height of the image
w = logo_image.width()
h = logo_image.height()
#f.geometry("%dx%d+50+30" % (w, h))
# size the window so the image will fill it 
#root.geometry("%dx%d+50+30" % (w, h))
l = Canvas(root,width=w, height=h)
l.place(x=400,y=100)
l.create_image(2, 2, image=logo_image, anchor='nw')

f.mainloop()