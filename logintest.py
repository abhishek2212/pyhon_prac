import sys
import random
from tkinter import *
import tkinter
import tkinter as tkMessageBox
import sqlite3
global a
global b
global c
global d
global e
global f
global g
global h
global i
global j
top=Tk()
conn=sqlite3.connect('example.db')
t=conn.cursor()
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
j=StringVar()
def data(e,f,g,h):
    list1=[e,f,g,h]
    t.execute('INSERT INTO student10 VALUES(?,?,?,?)',list1)
    for row in t.execute('SELECT * FROM student10'):
        print (row)
    conn.commit()
    conn.close()
    tkMessageBox.showinfo("ucab","you registered succesfully")
def log():
    top2=Tk()
    def booking():
        top3=Tk()
        def fare3():
            var12=IntVar
            var12=fare1()
            l36=Label(frame3,text=var12,bg="blue",fg="white").grid(row=7,column=4)
        def fare1():
            v1=IntVar()
            v2=IntVar()
            v1=var.get()
            v2=var1.get()
            if v1=="bh-1" and v2=="unimall":
                fare2=30
                return fare2
            elif v1=="bh-1" and v2=="administrative":
                fare2=20
                return fare2
            elif v1=="bh-1" and v2=="bh-3":
                fare2=15
                return fare2
            elif v1=="bh-1" and v2=="maingate":
                fare2=80
                return fare2
            elif v1=="bh-1" and v2=="gh-6":
                fare2=40
                return fare2
            elif v1=="bh-6" and v2=="unimall":
                fare2=45
                return fare2
            elif v1=="bh-6" and v2=="administrative":
                fare2=30
                return fare2
            elif v1=="bh-6" and v2=="bh-3":
                fare2=15
                return fare2
            elif v1=="bh-6" and v2=="maingate":
                fare2=100
                return fare2
            elif v1=="bh-6" and v2=="gh-6":
                fare2=25
                return fare2
            elif v1=="bh-2" and v2=="unimall":
                fare2=20
                return fare2
            elif v1=="bh-2" and v2=="administrative":
                fare2=15
                return fare2
            elif v1=="bh-2" and v2=="bh-3":
                fare2=10
                return fare2
            elif v1=="bh-2" and v2=="maingate":
                fare2=90
                return fare2
            elif v1=="bh-2" and v2=="gh-6":
                fare2=45
                return fare2
            elif v1=="unimall" and v2=="administrative":
                fare2=10
                return fare2
            elif v1=="unimall" and v2=="bh-3":
                fare2=25
                return fare2
            elif v1=="unimall" and v2=="maingate":
                fare2=55
                return fare2
            elif v1=="unimall" and v2=="gh-6":
                fare2=20
                return fare2
            elif v1=="maingate" and v2=="unimall":
                fare2=36
                return fare2
            elif v1=="maingate" and v2=="administrative":
                fare2=65
                return fare2
            elif v1=="maingate" and v2=="bh-3":
                fare2=86
                return fare2
            elif v1=="maingate" and v2=="gh-6":
                fare2=64
                return fare2
            elif v1==v2:
                tkMessageBox.showwarning("ucab","please enter different origin and destination places")
        def final():
            tkMessageBox.showinfo("ucab","you have succesfully registered the cab")
        frame3=Frame(top3,width=800,height=800,bg="blue")
        labelfont=('times',15,'italic')
        l30=Label(frame3,text="UCAB online booking",bg="blue",fg="brown")
        l30.config(font=labelfont)
        l30.config(height=4,width=25)
        l30.grid(row=0,column=0,columnspan=5)
        l31=Label(frame3,text="mobile:",bg="blue",fg="white").grid(row=1,column=0)
        e1=Entry(frame3,bd=5).grid(row=1,column=4)
        l32=Label(frame3,text="from:",bg="blue",fg="white").grid(row=3,column=0)
        global var
        var=StringVar(top3)
        var.set(" ")
        om=OptionMenu(frame3,var,"bh-1","bh-6","bh-2","unimall","maingate").grid(row=3,column=4)
        l33=Label(frame3,text="to",bg="blue",fg="white").grid(row=5,column=0)
        global var1
        var1=StringVar(top3)
        var1.set(" ")
        om1=OptionMenu(frame3,var1,"unimall","administrative","bh-3","maingate","gh-6").grid(row=5,column=4)
        l34=Label(frame3,text="day",bg="blue",fg="white").grid(row=11,column=0)
        e2=Entry(frame3,bd=5).grid(row=11,column=4)
        l35=Label(frame3,text="time",bg="blue",fg="white").grid(row=9,column=0)
        e3=Entry(frame3,bd=5).grid(row=9,column=4)
        b7=Button(frame3,text="fare",bg="blue",fg="white",command=fare3).grid(row=7,column=0)
        b6=Button(frame3,text="Book",bg="red",fg="black",command=final).grid(row=13,column=2,columnspan=2)
        frame3.pack()
    frame2=Frame(top2,width=800,height=800,bg="yellow")
    labelfont=('times',20,'bold')
    l09=Label(frame2,text="WELCOME",bg="yellow",fg="red")
    l09.config(font=labelfont)
    l09.config(height=3,width=22)
    l09.grid(row=0,columnspan=3)
    l10=Label(frame2,text="Available routes",bg="yellow",fg="red")
    l10.config(font=labelfont)
    l10.config(height=3,width=22)
    l10.grid(row=1,column=0,columnspan=5)
    l11=Label(frame2,text="from",bg="red",fg="black").grid(row=2,column=0)
    l12=Label(frame2,text="To",bg="red",fg="black").grid(row=2,column=4)
    l13=Label(frame2,text="bh-1",bg="yellow").grid(row=4,column=0)
    l14=Label(frame2,text="-->",bg="yellow").grid(row=4,column=2)
    l15=Label(frame2,text="unimall",bg="yellow").grid(row=4,column=4)
    l16=Label(frame2,text="bh-6",bg="yellow").grid(row=6,column=0)
    l17=Label(frame2,text="-->",bg="yellow").grid(row=6,column=2)
    l18=Label(frame2,text="administrative",bg="yellow").grid(row=6,column=4)
    l19=Label(frame2,text="bh-2",bg="yellow").grid(row=8,column=0)
    l20=Label(frame2,text="-->",bg="yellow").grid(row=8,column=2)
    l21=Label(frame2,text="bh-3",bg="yellow").grid(row=8,column=4)
    l22=Label(frame2,text="unimall",bg="yellow").grid(row=10,column=0)
    l23=Label(frame2,text="-->",bg="yellow").grid(row=10,column=2)
    l24=Label(frame2,text="maingate",bg="yellow").grid(row=10,column=4)
    l25=Label(frame2,text="maingate",bg="yellow").grid(row=12,column=0)
    l26=Label(frame2,text="-->",bg="yellow").grid(row=12,column=2)
    l27=Label(frame2,text="gh-6",bg="yellow").grid(row=12,column=4)
    b5=Button(frame2,text="Book your cab",bg="pink",fg="white",command=booking).grid(row=1,rowspan=12,padx=5,column=5,columnspan=20)
    frame2.pack()
    top2.mainloop()
def newuser():
    #top.destroy()
    top1=Tk()
    def registered():
        tkMessageBox.showinfo("ucab","you have succesfully logged in")
    var=IntVar()
    frame1=Frame(top1,width=100,height=100,bg="orange")
    #logo2=PhotoImage(file="cab1.gif")
    #label6=Label(frame1,image=logo2,bg="orange").grid(row=0,column=0,columnspan=12,rowspan=9)
    label1=Label(frame1,text="name :",fg="blue",bg="orange").grid(row=0)
    entry1=Entry(frame1,bd=5)
    label2=Label(frame1,text="sex :",fg="blue",bg="orange").grid(row=2)
    rb1=Radiobutton(frame1,text="male",bg="orange",variable=var,value=1).grid(row=2,column=2,columnspan=2)
    rb2=Radiobutton(frame1,text="female",bg="orange",variable=var,value=2).grid(row=3,column=2,columnspan=2)
    label3=Label(frame1,text="Emailid :",fg="blue",bg="orange").grid(row=4)
    entry2=Entry(frame1,bd=5)
    label4=Label(frame1,text="mobile :",fg="blue",bg="orange").grid(row=5)
    entry3=Entry(frame1,text="#8096238512",bd=5)
    label5=Label(frame1,text="password:",fg="blue",bg="orange").grid(row=6)
    entry4=Entry(frame1,bd=5,show="*")
    entry1.grid(row=0,column=2,padx=5)
    entry2.grid(row=4,column=2,padx=5)
    entry3.grid(row=5,column=2)
    entry4.grid(row=6,column=2)
    b3=Button(frame1,text="submit",bg="blue",fg="orange",command=lambda:data(entry1.get(),entry2.get(),entry3.get(),entry4.get()))
    b3.grid(row=8,column=1,columnspan=2,pady=3)
    frame1.pack()
    top1.mainloop()
def log1(i,j):
    print (i,j)
    t.execute('INSERT INTO student9 VALUES(?)',[i])
    conn.commit()
    s1=StringVar()
    j1=StringVar()
    s2=StringVar()
    for s1 in t.execute('SELECT password FROM student10 WHERE emailid IS (SELECT emailid FROM student9)'):
        j1="(u"+"'"+j+"'"+",)"
        s2=str(s1)
        print (s2,j1)
        if s2==j1:
            log()
        else :
            tkMessageBox.showerror("ucab","please enter valid email and password");
t.execute("drop table student9")
t.execute('CREATE TABLE student9(emailid text)')
##t.execute('CREATE TABLE student10(name text,emailid text,mobile text,password text)')
f2=Frame(top,width=400,height=800,bg="blue")
logo1=PhotoImage(file="cab.gif")
l=Label(f2,image=logo1,bg="blue").grid(row=0,column=2,rowspan=3,columnspan=3)
l1=Label(f2,text="emailid:",bg="blue").grid(row=0,padx=5,pady=1)
e1=Entry(f2,bd=5)
l2=Label(f2,text="password:",bg="blue").grid(row=1,padx=5,pady=1)
e2=Entry(f2,bd=5,show="*")
e1.grid(row=0,column=1,padx=5,pady=1)
e2.grid(row=1,column=1,padx=5,pady=1)
b1=Button(f2,text="login",command=lambda:log1(e1.get(),e2.get()))
b1.grid(row=2,column=0,columnspan=2)
l3=Label(f2,text="",bg="blue").grid(row=3,rowspan=3)
labelfont=('times',20,'bold')
l3=Label(f2,text="For a new user, register here",bg="blue",fg="red")
l3.config(font=labelfont)
l3.config(height=3,width=22)
l3.grid(row=6,column=1,columnspan=3)
f2.pack()
b2=Button(f2,text="Newuser",bg="orange",fg="black",command=newuser)
b2.grid(row=6,column=4)
top.mainloop()
