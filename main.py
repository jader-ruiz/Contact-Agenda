import tkinter as tk
from tkinter import messagebox
import json

root = tk.Tk()

root.title("Contact Agenda")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#787c82")

header_frame = tk.Frame(root)
header_frame.pack(fill="x")

content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(content_frame)
left_frame.pack(side="left", padx=20)

right_frame = tk.Frame(content_frame)
right_frame.pack(side="right", padx=20)

button_frame = tk.Frame(root)
button_frame.pack(fill="x")

# Filled 
fill_of_nothing = tk.Label(root, text="",bg="#787c82")
fill_of_nothing.grid(row=0, column=0, padx=15)

# Main title
main_title = tk.Label(root, text="Contacts",font=("Arial", 12, "bold",),bg="#787c82")
main_title.grid(row=0, column=1, pady=5, padx=10)

# The listbox for the contacts
listbox = tk.Listbox(root, width=25, height=8,font=("Arial", 11),
    bg="white",
    fg="#333333",
    selectbackground="#4CAF50",
    selectforeground="white",
    relief="flat")


listbox.grid(row=2, column=1,pady=5)

# .json
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def load_contacts():
    with open("contacts.json") as file:
        contacts = json.load(file)
    for contact in contacts:
        name = contact["name"]
        listbox.insert(tk.END, name)
    return contacts

try:
    contacts = load_contacts()
except FileNotFoundError:
    contacts = []
    print("contacts.json was not found. Starting with an empty contact list.")


# Open other window of add contact
def open_add():
    add = tk.Toplevel(root)
    add.title("Add New Contact")
    add.geometry("300x200")
    add.resizable(False, False)
    add.configure(bg="#787c82")

    # Name 
    name_label = tk.Label(add, text="Name:",font=("Arial", 12,"bold"),bg="#787c82")
    name_label.grid(row=0, column=0, padx=5, pady=5) 
    name_entry = tk.Entry(add, width=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Phone
    phone_label = tk.Label(add, text="Phone:",font=("Arial", 12,"bold"),bg="#787c82")
    phone_label.grid(row=1, column=0, padx=5, pady=5)
    phone_entry = tk.Entry(add, width=30)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    # Email
    email_label = tk.Label(add, text="Email:",font=("Arial", 12,"bold"),bg="#787c82")
    email_label.grid(row=2, column=0, padx=5, pady=5)
    email_entry = tk.Entry(add, width=30)
    email_entry.grid(row=2, column=1, padx=5, pady=5)

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
        
        if not phone.isdigit():
            messagebox.showwarning(
            "Invalid Phone",
            "The phone number must contain only numbers."
            )
            add.destroy()
            return
        
        if "@" not in email or "." not in email:
            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email address."
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

        save_contacts()

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)   

    # Save button of add contact
    save_button = tk.Button(
    add,
    text="✅ Save",
    command=add_contact,bg="#4CAF50",fg="white",width=15)
    save_button.grid(row=3, column=1, pady=10)

    # Close button
    close_button = tk.Button(add, text="❌ Close", command=add.destroy,bg="#FF1500",fg="white",width=15)
    close_button.grid(row=4, column=1)

# Add contact button
add_button = tk.Button(root, text="➕ Add Contact",command=open_add,bg="#4CAF50",fg="white",width=15)
add_button.grid(row=3, column=1, pady=5)


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
    edit.configure(bg="#787c82")

    # Name 
    name_label = tk.Label(edit, text="Name:",font=("Arial", 12,"bold"),bg="#787c82")
    name_label.grid(row=0, column=0, padx=5, pady=5) 
    name_entry = tk.Entry(edit, width=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Phone
    phone_label = tk.Label(edit, text="Phone:",font=("Arial", 12,"bold"),bg="#787c82")
    phone_label.grid(row=1, column=0, padx=5, pady=5)
    phone_entry = tk.Entry(edit, width=30)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    # Email
    email_label = tk.Label(edit, text="Email:",font=("Arial", 12,"bold"),bg="#787c82")
    email_label.grid(row=2, column=0, padx=5, pady=5)
    email_entry = tk.Entry(edit, width=30)
    email_entry.grid(row=2, column=1, padx=5, pady=5)

    index = listbox.curselection()[0]
    contact = contacts[index]

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])


    # Close button
    close_button = tk.Button(edit,text="❌ Close", command=edit.destroy,bg="#FF1500",fg="white",width=15)
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
        if not phone.isdigit():
            messagebox.showwarning(
            "Invalid Phone",
            "The phone number must contain only numbers."
            )
            edit.destroy()
            return
        
        if "@" not in email or "." not in email:
            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email address."
            )
            edit.destroy()
            return
        
        contact["name"] = name
        contact["phone"] = phone
        contact["email"] = email

        save_contacts()

        listbox.delete(index)
        listbox.insert(index, contact["name"])
        
        edit.destroy()
    
    # Save button
    save_button = tk.Button(edit, text="✅ Save",
    command=save_edit,bg="#4CAF50",fg="white",width=15)
    save_button.grid(row=3, column=1, pady=2)
    

# Edit contact button
edit_button = tk.Button(root, text="✏️ Edit Contact",command=open_edit,bg="#2196F3",fg="white",width=15)
edit_button.grid(row=4, column=1, pady=5)


# Fuction of delete contact
def delete():
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]

    contacts.pop(index)

    save_contacts()

    listbox.delete(index)

# Delete contact button
delete_button = tk.Button(root, text="✂️ Delete Contact",command=delete,bg="#F44336",fg="white",width=15)
delete_button.grid(row=5, column=1, pady=5)



root.mainloop()