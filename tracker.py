import csv
import os
from datetime import datetime
import pandas as pd

CSV_FILE ="expenses.csv"
FIELDS = ["date", "category", "amount", "description"]

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

def add_expense(date, category, amount, description):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })

def view_expenses():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame(columns=FIELDS)
    df = pd.read_csv(CSV_FILE, parse_dates=["date"])
    return df

def summary_by_category():
    df =view_expenses()
    if df.empty:
        return pd.DataFrame(columns=["category", "amount"])
    return df.groupby("category")["amount"].sum().reset_index()