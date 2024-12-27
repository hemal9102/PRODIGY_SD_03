import tkinter as tk
from tkinter import messagebox
import csv
import os

CONTACTS_FILE = "contacts.csv"

# Load contacts from file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            contacts = [row for row in reader]
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Add a new contact
def add_contact(name, phone, email):
    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    contacts.append([name, phone, email])
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_fields()

# View all contacts
def view_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

# Edit a selected contact
def edit_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to edit!")
        return

    index = selected[0]
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    name_entry.insert(0, contacts[index][0])
    phone_entry.insert(0, contacts[index][1])
    email_entry.insert(0, contacts[index][2])

    def save_edit():
        contacts[index] = [name_entry.get(), phone_entry.get(), email_entry.get()]
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_fields()
        view_contacts()
        save_button.destroy()

    save_button = tk.Button(root, text="Save", command=save_edit)
    save_button.grid(row=6, column=1, pady=5)

# Delete a selected contact
def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to delete!")
        return

    index = selected[0]
    del contacts[index]
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact deleted successfully!")
    view_contacts()

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Load initial contacts
contacts = load_contacts()

# GUI setup
root = tk.Tk()
root.title("Contact Management System")

# Input fields
name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email")
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=lambda: add_contact(name_entry.get(), phone_entry.get(), email_entry.get()))
add_button.grid(row=3, column=1, pady=5)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=4, column=1, pady=5)

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.grid(row=5, column=0, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=5, column=1, pady=5)

# Contact list display
listbox = tk.Listbox(root, width=50)
listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Start the application
root.mainloop()
