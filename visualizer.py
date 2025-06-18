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
    plt.ylabel("Amount Spent($)")
    plt.tight_layout()
    plt.show()