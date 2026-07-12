import tkinter as tk

root = tk.Tk()

firstLabel = tk.Label(root, text="Contact Agenda")
firstLabel.pack()
root.geometry("700x500")
root.resizable(False, False)

root.mainloop()