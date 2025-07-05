import csv
import os
from datetime import datetime
import pandas as pd
from tkinter import messagebox

CSV_FILE ="expenses.csv"
FIELDS = ["date", "category", "amount", "description"]

def get_user_csv(username):
    return f"express_{username}.csv"

def add_expense(username, date, category, amount, description):
    csv_file = get_user_csv(username) 
    csv_file = get_user_csv(date)
    csv_file = get_user_csv(category)
    csv_file = get_user_csv(amount)
    csv_file = get_user_csv(description)


def view_expenses(username):
    csv_file = get_user_csv(username)

def init_csv():
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()

def add_expense(date, category, amount, description):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })

def view_expenses():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame(columns=FIELDS)

    try:
        df = pd.read_csv(CSV_FILE, parse_dates=["date"])
        return df
    except pd.errors.ParserError:
        # Try cleaning corrupted lines
        cleaned_lines = []
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            header = f.readline()
            cleaned_lines.append(header)
            for line in f:
                if line.count(",") == 3:
                    cleaned_lines.append(line)

        # Overwrite with cleaned content
        with open(CSV_FILE, "w", encoding="utf-8") as f:
            f.writelines(cleaned_lines)

        try:
            df = pd.read_csv(CSV_FILE, parse_dates=["date"])
            from tkinter import messagebox
            messagebox.showwarning("Warning", "Some corrupted lines were removed from the CSV.")
            return df
        except Exception as e:
            messagebox.showerror("Error", f"Still failed to read cleaned CSV:\n{e}")
            return pd.DataFrame(columns=FIELDS)

def summary_by_category():
    df =view_expenses()
    if df.empty:
        return pd.DataFrame(columns=["category", "amount"])
    return df.groupby("category")["amount"].sum().reset_index()

def reset_csv():
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()