import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt #go to line 51
from tkinter import messagebox, ttk, filedialog
import pandas as pd
from tracker import add_expense, view_expenses, init_csv, reset_csv
from login_window import login_windows

# this will prompt login
username = login_windows()
if not username:
    exit()

#this will initalize user-specific CSV
init_csv(username)

#------------- Global Styling -----------
BG_COLOR = "#f4f4f4"
FONT = ("Segoe UI", 10)
BUTTON_STYLE = {"bg": "#4CAF50", "fg": "white", "font": FONT, "padx": 10, "pady": 5, "relief": "groove"}

# ------------ GUI Function -------------
def add_expense_gui():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    description = description_entry.get()

    print(f"Adding: {date}, {category}, {amount}, {description}")  # Debugging output

    try:
        add_expense(date, category, float(amount), description)
        messagebox.showinfo("Success", "Expense added!")
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
    
    df = view_expenses(username)
    if df.empty:
        return
    
    for _, row in df.iterrows():
        tree.insert("", "end", values=(row["date"], row["category"], row["amount"], row["description"]))

def export_to_cvs():
    df = view_expenses()
    if df.empty:
        messagebox.showwarning("No Data", "There are no expenses to export.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save as")
    
    if file_path:
        try:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Export Successful", f"Expenses exported to {file_path}")
        except Exception as e:
            messagebox.showerror("Export Failed", str(e))

def show_category_chart():
    df= view_expenses()
    if df.empty:
        messagebox.showwarning("No Data", "No data available for chart.")
        return
    
    summary = df.groupby("category")["amount"].sum()
    
    fig, ax = plt.subplots()
    summary.plot.pie(ax=ax, autopct="%1.1f%%", startangle=90)
    ax.set_title("Spending by Category")
    ax.set_ylabel("")
    plt.tight_layout()

    # asking to save graph
    save = messagebox.askyesno("Save Chart", "would you like to save this chart as an image?")
    if save:
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if path:
            fig.savefig(path)
            messagebox.showinfo("Saved", f"Chart saved to:\n{path}")
        plt.show()

def show_monthly_chart():
    df = view_expenses()
    if df.empty:
        messagebox.showwarning("No Data", "No data available for chart.")
        return
    df["date"] = pd.to_datetime(df["date"], format="mixed", errors="coerce")
    df = df.dropna(subset=["date"])  # Remove rows where date couldn't be parsed
    df["month"] = df["date"].dt.to_period("M").astype(str)
    summary = df.groupby("month")["amount"].sum().reset_index()


    fig, ax = plt.subplots()
    ax.bar(summary["month"], summary["amount"])
    ax.set_title("Monthly Spending Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # asked to save 
    save = messagebox.askyesno("Save Chart", "would you like to save this chart as an image?")
    if save:
        path = filedialog.asksaveasfile(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if path:
            fig.savefig(path)
            messagebox.showinfo("Saved", f"Chart saved to:\n{path}")
        plt.show()


#--------- loading current expenses------------
def load_expenses():
    for item in tree.get_children():
        tree.delete(item)
    
    df = view_expenses()

    if df.empty:
        print("NO expenses to lead.") # this will debug the line error of the csv
        return
    
    for _, row in df.iterrows():
        tree.insert("", "end", values=(row["date"], row["category"], row["amount"], row["description"]))
        
# continue here when making the charts for the expense tracker

#--------------Main frame-----------------
# for the main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x500")
root.configure(bg=BG_COLOR)

#--------------input frame-----------------
# input frame 
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill="x")

# for both labels and for entry
tk.Label(input_frame, text="Date (MM-DD-YYYY): ", font=FONT, bg=BG_COLOR).grid(row=0, column=0, sticky="w")
date_entry = tk.Entry(input_frame)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# category section for the gui itself
tk.Label(input_frame, text="category: ").grid(row=1, column=0, sticky="w")
category_entry = tk.Entry(input_frame)
category_entry.grid(row=1, column=1, padx=5, pady=5)

# amount section for the gui
tk.Label(input_frame, text="Amount: ").grid(row=2, column=0, sticky="w")
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Description").grid(row=3, column=0, sticky="w")
description_entry = tk.Entry(input_frame)
description_entry.grid(row=3, column=1, padx=5, pady=5)

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=5)

# buttons for the gui
tk.Button(input_frame, text="Add Expense", command=add_expense_gui).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(input_frame, text="Export to CSV", command=export_to_cvs).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(input_frame, text="Category Chart", command=show_category_chart).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(input_frame, text="Monthly Chart", command=show_monthly_chart).grid(row=7, column=0, columnspan=2, pady=5)

#--------------table frame-----------------
table_frame = tk.Frame(root, padx=10, pady=10)
table_frame.pack(fill="both", expand=True)

# this will show the expenses from table
columns = ("Date", "Category", "Amount", "Description")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", stretch=True)

tree.pack(fill="both", expand=True)


# ----------- loading initial data------------
load_expenses()

#------------ launching app ------------------
root.mainloop()