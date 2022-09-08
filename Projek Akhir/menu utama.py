from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Welcome").grid(column=0, row=0)
ttk.Button(frm, text="Coming Soon", command=root.destroy).grid(column=0, row=1)

root.mainloop()