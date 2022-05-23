# Python program to create a simple GUI
# calculator using Tkinter
# import everything from tkinter module
import tkinter as tk
from tkinter import *
# create a GUI window
calc = tk.Tk()
# set the configuration of GUI window
calc.geometry("180x240")
# set the title of GUI window
calc.title("Calculator")
# set the background colour of GUI window
calc.configure(background="cyan")
calc.maxsize(180, 240)
calc.minsize(180, 240)
# Widgets are added here
inp = Entry(calc, width=16, borderwidth=2, relief=RIDGE)
inp.grid(pady=15, row=0, sticky="w", padx=15)


#  All the button operations Starts here.


def nine():
    inp.insert("end", "9")


def eight():
    inp.insert("end", "8")


def seven():
    inp.insert("end", "7")


def six():
    inp.insert("end", "6")


def five():
    inp.insert("end", "5")


def four():
    inp.insert("end", "4")


def three():
    inp.insert("end", "3")


def two():
    inp.insert("end", "2")


def one():
    inp.insert("end", "1")


def zero():
    inp.insert("end", "0")


def double_zero():
    inp.insert("end", "00")


def dot():
    inp.insert("end", ".")


def plus():
    inp.insert("end", "+")


def minus():
    inp.insert("end", "-")


def mul():
    inp.insert("end", "*")


def divide():
    inp.insert("end", "/")


def modulus():
    inp.insert("end", "%")


def result():
    if inp.get() == "":
        inp.insert("end", "Insert a Number")
    elif inp.get()[0] == "0":
        inp.delete(0, "end")
        inp.insert("end", "Insert a Number")

    else:
        res = inp.get()
        res = eval(res)
        inp.insert("end", " = ")
        inp.insert("end", res)


def clear():
    inp.delete(0, "end")


# This is where the Button Design Code is.
clear = Button(calc, text="C", width=3, command=clear, bg="lime", fg="white", relief=RIDGE, )
clear.grid(row=0, sticky="w", padx=125, pady=5)
seven = Button(text="7", width=3, command=seven, borderwidth=2, relief=RIDGE)
seven.grid(row=1, sticky="w", padx=15, pady=5)
eight = Button(text="8", width=3, command=eight, borderwidth=2, relief=RIDGE)
eight.grid(row=1, sticky="w", padx=50, pady=5)
nine = Button(calc, text="9", width=3, command=nine, borderwidth=2, relief=RIDGE)
nine.grid(row=1, sticky="w", padx=85, pady=5)
plus = Button(calc, text="+", width=3, command=plus, borderwidth=2, relief=RIDGE)
plus.grid(row=1, sticky="e", padx=125, pady=5)
four = Button(text="4", width=3, command=four, borderwidth=2, relief=RIDGE)
four.grid(row=2, sticky="w", padx=15, pady=5)
five = Button(text="5", width=3, command=five, borderwidth=2, relief=RIDGE)
five.grid(row=2, sticky="w", padx=50, pady=5)
six = Button(calc, text="6", width=3, command=six, borderwidth=2, relief=RIDGE)
six.grid(row=2, sticky="w", padx=85, pady=5)
minus = Button(calc, text="-", width=3, command=minus, borderwidth=2, relief=RIDGE)
minus.grid(row=2, sticky="e", padx=125, pady=5)
one = Button(text="1", width=3, command=one, borderwidth=2, relief=RIDGE)
one.grid(row=3, sticky="w", padx=15, pady=5)
two = Button(text="2", width=3, command=two, borderwidth=2, relief=RIDGE)
two.grid(row=3, sticky="w", padx=50, pady=5)
three = Button(calc, text="3", width=3, command=three, borderwidth=2, relief=RIDGE)
three.grid(row=3, sticky="w", padx=85, pady=5)
multiply = Button(calc, text="*", width=3, command=mul, borderwidth=2, relief=RIDGE)
multiply.grid(row=3, sticky="e", padx=125, pady=5)
zero = Button(text="0", width=3, command=zero, borderwidth=2, relief=RIDGE)
zero.grid(row=4, sticky="w", padx=15, pady=5)
double_zero = Button(text="00", width=3, command=double_zero, borderwidth=2, relief=RIDGE)
double_zero.grid(row=4, sticky="w", padx=50, pady=5)
dot = Button(calc, text=".", width=3, command=dot, borderwidth=2, relief=RIDGE)
dot.grid(row=4, sticky="w", padx=85, pady=5)
divide = Button(calc, text="/", width=3, command=divide, borderwidth=2, relief=RIDGE)
divide.grid(row=4, sticky="e", padx=125, pady=5)
result = Button(calc, text="=", width=13, command=result, bg="lime", fg="white", borderwidth=2, relief=RIDGE)
result.grid(row=5, sticky="w", padx=15, pady=5)
modulus = Button(calc, text="%", width=3, command=modulus, borderwidth=2, relief=RIDGE)
modulus.grid(row=5, sticky="e", padx=125, pady=5)
# start the GUI
calc.mainloop()
