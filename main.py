import tkinter as tk

root = tk.Tk()

root.title("Contact Agenda")
root.geometry("700x500")
root.resizable(False, False)

# Name 
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10) 

name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)


# Phone
phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=10)

phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=10)


# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10)

email_entry = tk.Entry(root, width=30).grid(row=2, column=1, padx=10, pady=10)


# Save button
save_button = tk.Button(root, text="Add Contact")
save_button.grid(row=3, column=0, pady=15)


#why i use grid? = because it works for me given that its propierties are good for my from
#row is the fila and column is the columna hahah, i mean is where are in the position.
#padx = padding for x and pady for y

root.mainloop()