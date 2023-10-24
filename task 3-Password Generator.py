import random
import string
from tkinter import *

def pswd_generator():
    """Generate a random character (lowercase, uppercase, digit, or punctuation)."""
    global sc
    n = int(e2.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    res = ""
    for i in range(n):
        res += random.choice(characters)
    sc.set(res)

tk = Tk()
tk.geometry("600x600")
tk.title("Password Generator")

f = Frame(tk)

f4 = Frame(f)
Label(f4, text="Password Generator", font="comicsans 18").pack(side=LEFT)
f4.pack(pady=20)

f1 = Frame(f)
Label(f1, text="Username:", font="comicsans 14").pack(side=LEFT)
e1 = Entry(f1, font="comicsans 14", relief=RAISED)
e1.pack(side=LEFT, padx=30)
f1.pack()

f2 = Frame(f)
Label(f2, text="Enter password Length:", font="comicsans 14").pack(padx=20, side=LEFT)
e2 = Entry(f2, font="comicsans 14", relief=RAISED)
e2.pack(side=LEFT)
f2.pack(pady=20)

f3 = Frame(f)
sc = StringVar()
Label(f3, text="Generated Password:", font="comicsans 14").pack(side=LEFT)
e3 = Entry(f3, font="comicsans 14", relief=RAISED, textvariable=sc)
e3.pack(side=LEFT, padx=20)
f3.pack()

f.pack(pady=20)

b = Button(text="GENERATE PASSWORD", font="comicsans 14 bold", bg="dark blue", fg="white", borderwidth=3, command=pswd_generator)
b.pack()

b2 = Button(text="ACCEPT", font="comicsans 14", bg="white", fg="dark blue", borderwidth=3)
b2.pack(pady=20)

b3 = Button(text="REJECT", font="comicsans 14", bg="white", fg="dark blue", borderwidth=3)
b3.pack()

tk.mainloop()