import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Contact Agenda")
root.geometry("700x500")
root.resizable(False, False)

# Filled 
fill_of_nothing = tk.Label(root, text="")
fill_of_nothing.grid(row=0, column=0, padx=15)

# Main title
main_title = tk.Label(root, text="Contactos")
main_title.grid(row=0, column=1, pady=5, padx=10)

# The listbox for the contacts
listbox = tk.Listbox(root, width=25, height=8,)
listbox.grid(row=4, column=1,)

root.mainloop()