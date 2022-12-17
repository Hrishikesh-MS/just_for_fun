from tkinter import *
import random

root = Tk()
root.title("Question?")
root.geometry('360x300')


def move(e):
    n_bt.place(relx=random.choice(x_coordinate), rely=random.choice(y_coordinate), relwidth=0.25, relheight=0.1)


def yes():
    for widget in root.winfo_children():
        widget.destroy()

    end = Label(root, text="I Knew It!", font=("", 18))
    end.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)


qn = Label(root, text="Are you stupid?", font=("", 15), padx=5, pady=5)
qn.place(relx=0.3, rely=0.1, relwidth=0.4)

y_bt = Button(root, text="Yes", background='silver', command=yes)
n_bt = Button(root, text="No", background='silver', command= lambda: move(0))

n_bt.bind("<Enter>", move)

y_bt.place(relx=0.2, rely=0.6, relwidth=0.25, relheight=0.1)
n_bt.place(relx=0.550, rely=0.6, relwidth=0.25, relheight=0.1)

x_coordinate = []
y_coordinate = []

x = 0.550
y = 0.45
while x <= 0.850:
    x_coordinate.append(x)
    x += 0.100

while y <= 0.9:
    y_coordinate.append(y)
    y += 0.100

root.mainloop()
