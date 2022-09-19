import tkinter as tk
import main

window = tk.Toplevel()
window.geometry("500x500")

button = tk.Button(window, text="mulai", command=main.mulai)
button.pack()

window.mainloop()