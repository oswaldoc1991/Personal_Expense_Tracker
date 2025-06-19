from summary import summary_by_category, summary_by_month
from visualizer import show_spending_chart, show_monthly_trend_chart
from tracker import init_csv, add_expense, view_expenses, summary_by_category
from datetime import datetime
def main():
    init_csv()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expenses")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. View Spending Chart")
        print("5. View Monthly Summary")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        # choosing 1 to 4 for the adding, viewing and all expenses
        if choice == "1":
            date_input = input("Date (MM-DD-YYY) [press Enter for todays date]: ")
            if not date_input:
                date = datetime.today().strftime("%Y-%m-%d")
            else:
                try:
                    datetime.strptime(date_input, "%Y-%m-%d")
                    date = date_input
                except ValueError:
                    print("Invalud date format. use MM-DD-YYY.")
                    continue
                
            # category input
            category = input("Category: ").strip()
            if not category:
                print("Category can not be empty.")
                continue
            
            # amount input
            amount_input = input("Amount: ").strip().replace("$", "")
            try:
                amount = float(amount_input)
                if amount <= 0:
                    print("amount must be grater than 0.")
                    continue
            except ValueError:
                print("Invalid amomunt, please enter a valid number.")
                continue
            
            # discription input 
            description = input("Discription: ").strip()
            if not description:
                print("description cannot be empty.")
                continue
            
            # Valid expenses are saved
            add_expense(date, category, amount, description)
            print("Expense added.")

        # choice 2
        elif choice == "2":
            df = view_expenses()
            print(df)

        # choice 3
        elif choice == "3":
            summary = summary_by_category()
            print("\nSummary by category")
            print(summary)

        #choice 4
        elif choice == "4":
            summary = summary_by_category()
            if summary.empty:
                print("No data to display")
            else:
                show_spending_chart(summary)
        
        # choice 5
        elif choice =="5":
            monthly = summary_by_month()
            if monthly.empty:
                print("no data to summariez.")
            else:
                print("\nMonthly Spending Summary: ")
                print(monthly)

                view_chart = input("would you like to see a monthly trend chart? (y/n)").strip().lower()
                if view_chart == "y":
                    show_monthly_trend_chart(monthly)
            
        elif choice == "6":
            print("Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()