import tkinter as tk
from tkinter import ttk, messagebox

from phone_module import create_contact, duplicate_check, find_number_by_attribute


phone_list = []


def update_table(display_list):
    """Refresh the table with the given contact list."""
    for row in table.get_children():
        table.delete(row)

    for index, phone in enumerate(display_list, start=1):
        table.insert(
            "",
            "end",
            values=(
                index,
                phone["name"],
                phone["family"],
                phone["number"],
                phone["info"],
            ),
        )


def clear_fields():
    """Clear all input fields."""
    entry_name.delete(0, tk.END)
    entry_family.delete(0, tk.END)
    entry_number.delete(0, tk.END)
    entry_info.delete(0, tk.END)


def add_contact():
    """Add a new contact to the list."""
    name = entry_name.get()
    family = entry_family.get()
    number = entry_number.get()
    info = entry_info.get()

    if not name or not family or not number or not info:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    new_contact = create_contact(name, family, number, info)

    if duplicate_check(phone_list, new_contact):
        phone_list.append(new_contact)
        update_table(phone_list)
        clear_fields()
        messagebox.showinfo("Success", "Contact saved successfully.")
    else:
        messagebox.showerror("Error", "Duplicate contact or phone number found.")


def search_by_name():
    """Search contacts by name."""
    search_value = entry_name.get().strip()
    if not search_value:
        messagebox.showwarning("Input Error", "Please enter a name to search.")
        return

    result = find_number_by_attribute(phone_list, "name", search_value)
    update_table(result)


def search_by_family():
    """Search contacts by family name."""
    search_value = entry_family.get().strip()
    if not search_value:
        messagebox.showwarning("Input Error", "Please enter a family name to search.")
        return

    result = find_number_by_attribute(phone_list, "family", search_value)
    update_table(result)


def show_all():
    """Show all contacts."""
    update_table(phone_list)


root = tk.Tk()
root.title("Phone Book")
root.geometry("700x500")

frame_form = tk.LabelFrame(root, text="Contact Information", padx=10, pady=10)
frame_form.pack(padx=15, pady=10, fill="x")

tk.Label(frame_form, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(frame_form)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Family:").grid(row=0, column=2, sticky="w", pady=5)
entry_family = tk.Entry(frame_form)
entry_family.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_form, text="Phone Number:").grid(row=1, column=0, sticky="w", pady=5)
entry_number = tk.Entry(frame_form)
entry_number.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Info:").grid(row=1, column=2, sticky="w", pady=5)
entry_info = tk.Entry(frame_form)
entry_info.grid(row=1, column=3, padx=5, pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Contact", command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Search by Name", command=search_by_name).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Search by Family", command=search_by_family).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Show All", command=show_all).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Clear", command=clear_fields).grid(row=0, column=4, padx=5)

columns = ("row", "name", "family", "number", "info")
table = ttk.Treeview(root, columns=columns, show="headings", height=10)

table.heading("row", text="No.")
table.heading("name", text="Name")
table.heading("family", text="Family")
table.heading("number", text="Phone Number")
table.heading("info", text="Info")

table.column("row", width=50, anchor="center")
table.column("name", width=140, anchor="center")
table.column("family", width=140, anchor="center")
table.column("number", width=140, anchor="center")
table.column("info", width=200, anchor="center")

table.pack(padx=15, pady=10, fill="both", expand=True)

root.mainloop()