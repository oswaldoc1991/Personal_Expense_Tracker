import matplotlib.pyplot as plt

# spending chats
def show_spending_chart(summary_df):
    if summary_df.empty:
        print("No data to visualize.")
        return
    
    plt.figure(figsize=(8, 5))
    plt.bar(summary_df["category"], summary_df["amount"])
    plt.title("Spending by Category")
    plt.xlabel("category")
    plt.ylabel("Amount Spent ($)")
    plt.tight_layout()
    plt.show()

# line chart for montly spending
def show_monthly_trend_chart(monthly_df):
    if monthly_df.empty:
        print("No data to visualize.")
        return
    
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_df["month"], monthly_df["amount"], marker="o")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Spending ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()