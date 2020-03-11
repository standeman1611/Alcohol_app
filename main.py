from tkinter import *
import tkinter as tk

window = tk.Tk()

tk.Label(window, text="Alcohol promillage calculator").grid()

tk.Label(window, text="Hoeveel glazen heb je gehad?").grid(row=1)

g = tk.Entry(window)grid(row=1, column=1)

tk.Label(window, text="Wat is je gewicht? (in kg)").grid(row=2)

m = tk.Entry(window).grid(row=2, column=1)

tk.Label(window, text="Hoelang geleden was je laatste glas alcohol? (in uren)").grid(row=3)

t = tk.Entry(window).grid(row=3, column=1)

tk.Label(window, text="Wat is je geslacht?").grid(row=4)

ge = tk.Entry(window).grid(row=4, column=1)

Glazen = g.get()
Massa = m.get()
Tijd = t.get()
Gender = ge.get()

def calc():
    if Gender.lower() == "man":
        Vocht = 0.72
    elif Gender.lower() == "vrouw":
        Vocht = 0.61
    promille = round(((Glazen * 10) / (Massa * Vocht)) - ((Tijd - 0.5) * (Massa * 0.002)), 1)
    tk.Label(window, text=promille).grid(row=5)

b = tk.Button(window, text="Calculate", command=calc)
b.grid(row=6)

window.mainloop()