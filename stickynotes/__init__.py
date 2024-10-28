import tkinter as tk
from tkinter import simpledialog
import time

def StickyNotes():
    current_time = time.strftime("%H:%M")

    root = tk.Tk()
    root.title("Sticky Notes")
    root.geometry("300x300")

    note_input = simpledialog.askstring("Input", "Type Your notes here:", parent=root)
    
    if note_input is not None:
        tk.Label(root, text="Time: " + current_time, font=("Arial", 12)).pack(pady=10)

        tk.Label(root, text="Note:", font=("Arial", 10, "bold")).pack()
        tk.Label(root, text=note_input, font=("Arial", 10)).pack(pady=5)

    root.mainloop()

StickyNotes()
