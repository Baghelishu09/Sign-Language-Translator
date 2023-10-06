from tkinter import *

win=Tk()
win.geometry("1366x768+0+0")
win.resizable(False,False)
win.title("Sign Language Translator")

frame1=Frame(win)
frame1.place(x=0,y=0,height=70,width=1366)

title=Label(frame1,text="SIGN LANGUAGE TRANSLATOR",font=("times new roman",40,"bold"),bg="white",
            fg="red",relief=SUNKEN,bd=2)
title.pack(side=TOP,fill=X)

frame2=Frame(win,bg="powder blue",relief=RIDGE)
frame2.place(x=0,y=70,width=800,height=640)

lbl_frame2=Label(frame2,text="Camera Frame",font=("times new roman",30,"italic bold"),
                 fg="green",bg="powder blue")
lbl_frame2.place(x=100,y=100)

frame2=Frame(win,bg="light grey",relief=RIDGE)
frame2.place(x=800,y=70,width=550,height=640)

lbl_frame2=Label(frame2,text="Translator Frame",font=("times new roman",30,"italic bold"),
                 fg="black",bg="light grey")
lbl_frame2.place(x=100,y=100)


win.mainloop()