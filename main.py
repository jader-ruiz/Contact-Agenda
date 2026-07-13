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

email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=10)

# List pf contacts
contacts = []

# Fuctions
def add_contact():
    contact = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get()
    }

    contacts.append(contact)

    listbox.insert(tk.END, contact["name"])


def show_contact(event):
    index = listbox.curselection()[0]
    contact = contacts[index]

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])
    

# Save button
save_button = tk.Button(root, text="Add Contact",command=add_contact)
save_button.grid(row=3, column=1, pady=15)

#why i use grid? = because it works for me given that its propierties are good for my from
#row is the fila and column is the columna hahah, i mean is where are in the position.
#padx = padding for x and pady for y

# The listbox for the contacts

listbox = tk.Listbox(root, width=25, height=8)
listbox.grid(row=4, column=1,)

# Connect to fuction
listbox.bind("<<ListboxSelect>>", show_contact)

root.mainloop()