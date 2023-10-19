import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        clear_fields()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['Phone']}")

def search_contact():
    query = search_entry.get()
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        if query in name or query in info['Phone']:
            contact_list.insert(tk.END, f"{name} - {info['Phone']}")

def display_contact(event):
    selected_contact = contact_list.get(contact_list.curselection())
    contact_name = selected_contact.split(" - ")[0]
    contact_details = contacts.get(contact_name)
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    name_entry.insert(tk.END, contact_name)
    phone_entry.insert(tk.END, contact_details['Phone'])
    email_entry.insert(tk.END, contact_details['Email'])
    address_entry.insert(tk.END, contact_details['Address'])

def update_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    contact_name = selected_contact.split(" - ")[0]
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[contact_name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        clear_fields()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    contact_name = selected_contact.split(" - ")[0]
    if messagebox.askyesno("Confirm Deletion", f"Delete {contact_name}?"):
        del contacts[contact_name]
        update_contact_list()
        clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Contact Management System")

name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(app, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(app, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(app, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(app)
address_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, padx=10, pady=5)

search_label = tk.Label(app, text="Search:")
search_label.grid(row=4, column=1, padx=10, pady=5)
search_entry = tk.Entry(app)
search_entry.grid(row=4, column=2, padx=10, pady=5)
search_button = tk.Button(app, text="Search", command=search_contact)
search_button.grid(row=4, column=3, padx=10, pady=5)

update_button = tk.Button(app, text="Update Contact", command=update_contact)
update_button.grid(row=5, column=0, padx=10, pady=5)
delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.grid(row=5, column=1, padx=10, pady=5)

contact_list = tk.Listbox(app, width=50)
contact_list.grid(row=6, column=0, columnspan=4, padx=10, pady=5)
contact_list.bind('<<ListboxSelect>>', display_contact)

update_contact_list()

app.mainloop()
