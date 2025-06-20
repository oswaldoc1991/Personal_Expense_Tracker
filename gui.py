import tkinter as tk
from tkinter import messagebox, ttk
from tracker import add_expense, view_expenses

def add_expense_gui():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    description = description_entry.get()

    try:
        add_expense(date, category, float(amount), description)
        messagebox.showinfo("success", "expense added!")
        clear_entries()
        load_expenses()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entries():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

def load_expenses():
    for item in tree.get_children():
        tree.delete(item)
    
    df = view_expenses()
    for _, row in df.iterrows():
        tree.insert("", "end", values=(row["date"], row["category"], row["amount"], row["description"]))

# for the main window
root = tk.Tk()
root.title("Expense Tracker")

# for both labels and for entry
tk.Label(root, text="Date (MM-DD-YYYY): ").grid(row=0, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

# category section for the gui itself
tk.Label(root, text="category: ").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

# amount section for the gui
tk.Label(root, text="Amount: ").grid(row=2, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

tk.Label(root, text="Description").grid(row=3, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=3, column=1)

# buttons for the gui
tk.Button(root, text="Add Expense", command=add_expense_gui).grid(row=4, column=0, columnspan=2, pady=10)

# this will show the expenses from table
columns = ("Date", "Category", "Amount", "Description")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.grid(row=5, column=0, columnspan=2, pady=10)

# loading data from start up
load_expenses()

root.mainloop()