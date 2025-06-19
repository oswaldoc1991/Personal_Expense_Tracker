from tracker import view_expenses
import pandas as pd

#summary by category
def summary_by_category():
    df = view_expenses()
    if df.empty:
        return pd.DataFrame(columns=["category", "amount"])
    return df.groupby("category")["amount"].sum().reset_index()

# monthly breakdown
def summary_by_month():
    df = view_expenses()
    if df.empty:
        return pd.DataFrame(columns=["month", "amount"])
    
    # converting the date column to datetime    
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # droping any rows where date couldnt be parsed
    df = df.dropna(subset=["date"])
    
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df.groupby("month")["amount"].sum().reset_index()