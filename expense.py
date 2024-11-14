import calendar
import datetime

class Expense:
    def __init__(self, name, amt, cat):
        self.name = name
        self.amount = amt
        self.category = cat

def main():
    print("Running Expense Tracker...")
    
    expense_file_path = "expenses.csv"
    budget = 150000
    expense_chk = check_expense()
    
    save_file(expense_chk, expense_file_path)
    summarize_expense(expense_file_path, budget)

def check_expense():
    expense_name = input("Where did you spend the money?: ")
    expense_amount = eval(input("How much money did you spend?: "))
    expense_category = ["Food", "Travel", "Fun", "Work", "Misc"]
    
    while True:
        print('In which Category did you spend the money?')
        for i, category_name in enumerate(expense_category):
            print(f'{i+1}. {category_name}')
        
        value_range = f"[1 - {len(expense_category)}]"
        try:
            select_index = int(input(f'Please select the category: {value_range}: ')) - 1
            if select_index in range(len(expense_category)):
                selected_category = expense_category[select_index]
                print(f'Selected Category: {selected_category}')
                
                new_expense = Expense(name=expense_name, amt=expense_amount, cat=selected_category)
                return new_expense
            else:
                print('Invalid category selected.')
        except ValueError:
            print("Invalid input. Please enter a valid category number.")

def save_file(expense_chk: Expense, expense_file_path: str):
    print("Saving the expense to file...")
    with open(expense_file_path, 'a', encoding='utf-8') as f:
        f.write(f'{expense_chk.name},{expense_chk.amount},{expense_chk.category}\n')

def summarize_expense(expense_file_path: str, budget: float):
    expenses = []
    
    # Read the expenses from the file
    with open(expense_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(f'{expense_name} spent Rs.{expense_amount} in {expense_category}')
            
            # Create expense object from the data
            line_expense = Expense(name=expense_name, amt=float(expense_amount), cat=expense_category)
            expenses.append(line_expense)
    
    # Calculate total expense by category
    amount_by_category = {}
    for e in expenses:
        key = e.category
        if key in amount_by_category:
            amount_by_category[key] += e.amount
        else:
            amount_by_category[key] = e.amount
    
    print("\nCategory-wise Expenses:")
    for key, amount in amount_by_category.items():
        print(f'{key}: Rs.{amount:.2f}')
    
    # Calculate total expense
    total_expense = sum([x.amount for x in expenses])
    print(f'\nTotal Expense: Rs {total_expense:.2f}')
    
    # Calculate remaining budget
    remaining_amount = budget - total_expense
    print(f'Remaining Budget: Rs {remaining_amount:.2f}')
    
    # Calculate daily budget
    now = datetime.datetime.now()
    day_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = day_in_month - now.day
    if remaining_days > 0:
        daily_budget = remaining_amount / remaining_days
        print(f'Daily Budget: Rs {daily_budget:.2f}')
    else:
        print("No days remaining in the month.")

if __name__ == "__main__":
    main()
