from tracker import init_csv, add_expense, view_expenses, summary_by_category
from datetime import datetime
def main():
    init_csv()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expenses")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. exit")
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
        elif choice == "2":
            df = view_expenses()
            print(df)
        elif choice == "3":
            summary = summary_by_category()
            print("\nSummary by category")
            print(summary)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()