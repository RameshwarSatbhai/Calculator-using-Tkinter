from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root = Tk()
root.geometry("454x720")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill="x",padx=10,pady=10)

# frame of 9 8 7
f = Frame(root,bg="grey")
for i in range(9,6,-1):
    b = Button(f, text=f"{i}", font="lucida 20 bold",padx=5,pady=5)
    b.pack(side="left",padx=10,pady=10)
    b.bind("<Button-1>",click)
f.pack()

# frame of 6 5 4
f = Frame(root,bg="grey")
for i in range(6,3,-1):
    b = Button(f, text=f"{i}", font="lucida 20 bold",padx=5,pady=5)
    b.pack(side="left",padx=10,pady=10)
    b.bind("<Button-1>",click)
f.pack()

# frame of 3 2 1
f = Frame(root,bg="grey")
for i in range(3,0,-1):
    b = Button(f, text=f"{i}", font="lucida 20 bold",padx=5,pady=5)
    b.pack(side="left",padx=10,pady=10)
    b.bind("<Button-1>",click)
f.pack()

# frame of 0 - +
f = Frame(root,bg="grey")
b = Button(f, text="0", font="lucida 20 bold",padx=6,pady=6)
b.pack(side="left",padx=12,pady=10)
b.bind("<Button-1>",click)


b = Button(f, text="-", font="lucida 20 bold",padx=6,pady=6)
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="*", font="lucida 20 bold",padx=6,pady=6)
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

# frame of + / C
f = Frame(root,bg="grey")
b = Button(f, text="+", font="lucida 20 bold",padx=6,pady=6)
b.pack(side="left",padx=12,pady=10)
b.bind("<Button-1>",click)


b = Button(f, text="/", font="lucida 20 bold",padx=6,pady=6)
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="C", font="lucida 20 bold",padx=6,pady=6)
b.pack(side="left",padx=5,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="=", font="lucida 20 bold",padx=6,pady=6,width=10)
b.pack(side="left",padx=8,pady=10,anchor="sw",)
b.bind("<Button-1>",click)
f.pack(padx=100)

designer = Label(root,text="Rameshwar Vitthal Satbhai")
designer.pack()

root.mainloop()