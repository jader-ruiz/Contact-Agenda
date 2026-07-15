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
listbox.grid(row=2, column=1,)
contacts = []

# Open other window of add contact
def open_add():
    add = tk.Toplevel(root)
    add.title("Add New Contact")
    add.geometry("300x200")
    root.resizable(False, False)

    # Name 
    name_label = tk.Label(add, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10) 
    name_entry = tk.Entry(add, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Phone
    phone_label = tk.Label(add, text="Phone:")
    phone_label.grid(row=1, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(add, width=30)
    phone_entry.grid(row=1, column=1, padx=10, pady=10)

    # Email
    email_label = tk.Label(add, text="Email:")
    email_label.grid(row=2, column=0, padx=10, pady=10)
    email_entry = tk.Entry(add, width=30)
    email_entry.grid(row=2, column=1, padx=10, pady=10)

    # Add contact fuction
    def add_contact():
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()

        if name == "" or phone == "" or email == "":
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            add.destroy()
            return
    
        contact = {
        "name": name,
        "phone": phone,
        "email": email
        }
    
        contacts.append(contact)
        listbox.insert(tk.END, name)

    # Save button of add contact
    save_button = tk.Button(
    add,
    text="Save",
    command=add_contact
    )
    save_button.grid(row=3, column=1, pady=10)

    # Close button
    close_button = tk.Button(add, text="Close", command=add.destroy)
    close_button.grid(row=4, column=1)

# Add contact button
add_button = tk.Button(root, text="Add Contact",command=open_add)
add_button.grid(row=3, column=1, pady=10)


# Open other window of edit contact
def open_edit():
    if not listbox.curselection():
        messagebox.showwarning(
            "No Selection",
            "Please select a contact."
        )
        return
    edit = tk.Toplevel(root)
    edit.title("Edit Contact")
    edit.geometry("300x200")
    edit.resizable(False, False)

    # Name 
    name_label = tk.Label(edit, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10) 
    name_entry = tk.Entry(edit, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Phone
    phone_label = tk.Label(edit, text="Phone:")
    phone_label.grid(row=1, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(edit, width=30)
    phone_entry.grid(row=1, column=1, padx=10, pady=10)

    # Email
    email_label = tk.Label(edit, text="Email:")
    email_label.grid(row=2, column=0, padx=10, pady=10)
    email_entry = tk.Entry(edit, width=30)
    email_entry.grid(row=2, column=1, padx=10, pady=10)

    index = listbox.curselection()[0]
    contact = contacts[index]

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])


    # Close button
    close_button = tk.Button(edit, text="Close", command=edit.destroy)
    close_button.grid(row=4, column=1)
    
    def save_edit():
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()

        if name == "" or phone == "" or email == "":
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            edit.destroy()
            return
        
        contact["name"] = name
        contact["phone"] = phone
        contact["email"] = email

        listbox.delete(index)
        listbox.insert(index, contact["name"])
        
        edit.destroy()
    
    # Save button
    save_button = tk.Button(edit, text="Save",command=save_edit)
    save_button.grid(row=5, column=1, pady=2)
    

# Edit contact button
edit_button = tk.Button(root, text="Edit Contact",command=open_edit)
edit_button.grid(row=4, column=1, pady=5)

root.mainloop()

root.mainloop()