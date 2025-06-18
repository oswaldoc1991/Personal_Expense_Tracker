from tracker import view_expenses
import pandas as pd

#summary by category
def summary_by_category():
    df = view_expenses()
    if df.empty:
        return pd.DataFrame(columns=["category", "amount"])
    return df.groupby("category")["amount"].sum().reset_index()