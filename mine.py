from tkinter import *
from tkinter import ttk
from random import randint
from tkinter import messagebox
import time


table=[]
botton=[]
found_mines=0

def tablee(x,y,m):
    for i in range(y):
        table2=[]
        for j in range(x):
            table2[j:j]=[0]
        table[i:i]=t=[table2]
    c=0
    while(c<m):
        a=randint(0,y-1)
        b=randint(0,x-1)
        if(table[a][b]==0):
            c=c+1
            del table[a][b]
            table[a][b:b]=[9]
    for i in range(y):
        for j in range(x):
            if(table[i][j]!=9):
                count = 0
                p = -1
                while (p < 2):
                    q = -1
                    while (q < 2):
                        e = i + p
                        f = j + q
                        if (e < y and e > -1 and f < x and f > -1 and (p != 0 or q != 0)):
                            if(table[e][f]==9):
                                count=count+1
                        q=q+1
                    p=p+1
                del table[i][j]
                table[i][j:j] = [count]


def lose(x,y):
    for i in range(y):
        for j in range(x):
            botton[i][j].state(['disabled'])
            if(table[i][j]==9):
                botton[i][j]["text"] = '*'
    messagebox.showinfo("Game Over","You Lost!!!")


def check(x,y,app):
    win=1
    for i in range(y):
        for j in range(x):
            if(table[i][j]!=9 and botton[i][j].instate(['!disabled'])):
                win=0
    if(win==1):
        for i in range(y):
            for j in range(x):
                if (table[i][j] == 9):
                    botton[i][j]["text"] = '^'
                botton[i][j].state(['disabled'])
        app.state=False
        messagebox.showinfo("Game Over", "You Won!!!")


def open(x,y,i,j):
    p = -1
    while (p < 2):
        q = -1
        while (q < 2):
            e = i + p
            f = j + q
            if (e < y and e > -1 and f < x and f > -1):
                botton[e][f].state(['disabled'])
                if (table[e][f] > 0 and table[e][f]<10):
                    botton[e][f]["text"] = str(table[e][f])
                if(p==0 and q==0):
                    del table[e][f]
                    table[e][f:f]=[10]
            q=q+1
        p=p+1


def click(x,y,i,j,app):
    if(table[i][j]==0):
        open(x,y,i,j)
        while(True):
            count=0
            for ii in range(y):
                for jj in range(x):
                    if(table[ii][jj]==0 and botton[ii][jj].instate(['disabled'])):
                        count=1
                        open(x,y,ii,jj)
            if(count==0):
                break
    if(table[i][j]>0 and table[i][j]<9):
        botton[i][j]["text"] = str(table[i][j])
        botton[i][j].state(['disabled'])
    check(x,y,app)
    if(table[i][j]==9):
        app.state = False
        lose(x,y)


def rightclick(i,j,label,m):
    global found_mines
    if(botton[i][j]["text"] == '^'):
        botton[i][j]["text"] = ''
        botton[i][j].state(['!disabled'])
        found_mines -= 1
    elif (botton[i][j].instate(['!disabled'])):
        botton[i][j]["text"] = '^'
        botton[i][j].state(['disabled'])
        found_mines += 1
    label.config(text='mines: '+str(m-found_mines))


def restart(x,y,m,rot):
    rot.destroy()
    tablee(x,y,m)
    map(x,y,m)


class App():
    def __init__(self,rot,x):
         self.timer = [0, 0, 0]
         self.state=True
         self.root=rot
         self.label = ttk.Label(text="")
         self.label.place(x=100,y=(x+1)*24)
         self.update_clock()
         self.button=ttk.Button(text='pause',command=self.pause )
         self.button.place(x=0,y=(x+1)*24)

    def update_clock(self):
        if (self.state):
            self.timer[2] += 1
            if (self.timer[2] >= 100):
                self.timer[2] = 0
                self.timer[1] += 1
            if (self.timer[1] >= 60):
                self.timer[0] += 1
                self.timer[1] = 0
        a=str(self.timer[0])
        if(len(a)<2):
            a= '0' + a
        b = str(self.timer[1])
        if (len(b) < 2):
            b = '0' + b
        c = str(self.timer[2])
        if (len(c) < 2):
            c = '0' + c
        timeString = a+':'+b+':'+c
        self.label.configure(text=timeString)
        self.root.after(10, self.update_clock)

    def pause(self):
        if (self.state==True):
            self.state = False
            self.button.config(text='play')
        elif (self.state==False):
            self.state = True
            self.button.config(text='pause')


def map(x,y,m):
    rot = Tk()
    rot.title("Minesweeper")
    label = ttk.Label(rot,text= 'mines: '+str(m))
    label.place(x=100, y=x*24)
    for i in range(y):
        bottonn=[]
        for j in range(x):
            bottonnn=ttk.Button(rot, text='',width=2 ,command=lambda x=x, y=y, i=i, j=j: click(x,y,i,j,app))
            bottonnn.bind("<Button-3>", lambda e, i=i, j=j, label=label,m=m, : rightclick(i,j,label,m))
            bottonnn.place(x=i*21, y=j*24)
            bottonn[j:j]=[bottonnn]
        botton[i:i]=[bottonn]
    reset=ttk.Button(rot, text='restart',command=lambda x=x , y=y , m=m, rot=rot: restart(x,y,m,rot))
    reset.place(x=0, y=x*24)
    app = App(rot,x)
    rot.mainloop()


def callback1():
    root.destroy()
    tablee(8, 8, 10)
    map(8, 8, 10)

def callback2():
    root.destroy()
    tablee(16, 16, 40)
    map(16, 16, 40)

def callback3():
    root.destroy()
    tablee(16, 30, 99)
    map(16, 30, 99)

def callback4():
    window=Tk()
    label1 = ttk.Label(window, text='width: ')
    label1.grid(row=0, column=0)
    width = StringVar()
    spinbox1 = Spinbox(window, from_=5, to=50, textvariable=width)
    spinbox1.grid(row=0, column=1)
    spinbox1.config(state='readonly')
    label2 = ttk.Label(window, text='height: ')
    label2.grid(row=1, column=0)
    height = StringVar()
    spinbox2 = Spinbox(window, from_=5, to=50, textvariable=height)
    spinbox2.grid(row=1, column=1)
    spinbox2.config(state='readonly')
    label3 = ttk.Label(window, text='percent mines: ')
    label3.grid(row=2, column=0)
    spinbox3 = Spinbox(window, from_=5, to=400)
    spinbox3.grid(row=2, column=1)
    spinbox3.config(state='readonly')
    botton5 = ttk.Button(window, text='play game')
    botton5.grid(row=3, column=0)
    botton5.config(command=lambda window=window: callback5(window,spinbox1,spinbox2,spinbox3))
    botton6 = ttk.Button(window, text='cancel')
    botton6.grid(row=3, column=1)
    botton6.config(command=lambda window=window:callback6(window))

def callback5(window,spinbox1,spinbox2,spinbox3):
    x=int(spinbox1.get())
    y=int(spinbox2.get())
    m=int(spinbox3.get())
    if(m>x*y-10):
        m=x*y-10
    root.destroy()
    window.destroy()
    tablee(x, y, m)
    map(x,y,m)

def callback6(window):
    window.destroy()

root =Tk()
root.title("Mines")
botton1 = ttk.Button(root, text='8*8\n10 mines')
botton1.grid(row=0, column = 0)
botton1.config(command =callback1)
botton2 = ttk.Button(root, text='16*16\n40 mines')
botton2.grid(row=0, column = 1)
botton2.config(command = callback2)
botton3 = ttk.Button(root, text='30*16\n99 mines')
botton3.grid(row=1, column = 0)
botton3.config(command = callback3)
botton4 = ttk.Button(root, text='?\nCustom')
botton4.grid(row=1, column = 1)
botton4.config(command = callback4)
root.mainloop()
