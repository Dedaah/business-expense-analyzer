expenses = [
    {"category": "Rent", "amount":2000},
    {"category": "Salaries", "amount":4500},
    {"category": "Marketing", "amount":1200},
    {"category": "Transport", "amount":600},
    {"category": "Utilities", "amount":450},
    {"category": "Software", "amount":750}
]

def calculate_total(expenses):
    total_expenses = 0
    for expense in expenses:
        total_expenses = total_expenses + expense["amount"]
    return total_expenses
total = calculate_total(expenses)

def calculate_average(expenses):
    count = 0
    for expense in expenses:
        count = count + 1
    average = calculate_total(expenses)/count
    return average
average = calculate_average(expenses)

def find_largest_expense(expenses):
    largest_expense_category = ""
    largest_expense_amount = 0
    for expense in expenses:
        if expense["amount"] > largest_expense_amount:
            largest_expense_amount = expense["amount"]
            largest_expense_category = expense["category"]
    return largest_expense_category,largest_expense_amount
largest_expense_category,largest_expense_amount = find_largest_expense(expenses)

def expenses_above_threshold(expenses,threshold):
    count = 0
    for expense in expenses:
        if expense["amount"] > threshold:
            count = count + 1
    return count
expenses_above_1000 = expenses_above_threshold(expenses,1000)

def analyze_expenses(expenses):
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    largest_expense_category,largest_expense_amount = find_largest_expense(expenses)
    expenses_above_1000 = expenses_above_threshold(expenses,1000)
    return total,average,largest_expense_category,largest_expense_amount,expenses_above_1000
total,average,largest_expense_category,largest_expense_amount,expenses_above_1000 = analyze_expenses(expenses)

print("BUSINESS EXPENSE ANALYZER")
print()
print("EXPENSES")
print("-------------------------")
for expense in expenses:
    print(f"{expense['category']:<20}: GHS {expense['amount']:,.2f}")
print()
print("SUMMARY")
print("-------------------------")
print(f"{'Total expenses:':<25} GHS {total:,.2f}")
print(f"{'Average expense:':<25} GHS {average:,.2f}")
print(f"{'Largest expense:':<25} {largest_expense_category}")
print(f"{'Largest amount:':<25} GHS {largest_expense_amount:,.2f}")
print(f"{'Expenses above GHS 1000:':<25} {expenses_above_1000}")
