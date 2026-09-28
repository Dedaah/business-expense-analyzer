import csv
with open("expenses.csv","r",newline="") as file:
    reader = csv.DictReader(file)
    expenses = []
    for row in reader:
        expense = {"category":row["Category"],
                   "amount":float(row["Amount"])
                   }
        expenses.append(expense)

valid_threshold = False
while not valid_threshold:
    try:
        threshold = float(input("Enter expense threshold: " ))
        if threshold > 0:
            valid_threshold = True
            print("Thank You!")
        else:
            print("Amount must be more than zero!")
    except ValueError:
        print("Enter a valid number!")

def calculate_total(expenses):
    total_expenses = 0
    for expense in expenses:
        total_expenses = total_expenses + expense["amount"]
    return total_expenses

def calculate_average(expenses):
    count = 0
    for expense in expenses:
        count = count + 1
    if count > 0:
        average = calculate_total(expenses)/count
    else:
        average = 0
    return average

def find_largest_expense(expenses):
    largest_expense_category = ""
    largest_expense_amount = 0
    for expense in expenses:
        if expense["amount"] > largest_expense_amount:
            largest_expense_amount = expense["amount"]
            largest_expense_category = expense["category"]
    return largest_expense_category,largest_expense_amount

def expenses_above_threshold(expenses,threshold):
    count = 0
    for expense in expenses:
        if expense["amount"] > threshold:
            count = count + 1
    return count

def analyze_expenses(expenses,threshold):
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    largest_expense_category,largest_expense_amount = find_largest_expense(expenses)
    above_thresh_count = expenses_above_threshold(expenses,threshold)
    return total,average,largest_expense_category,largest_expense_amount,above_thresh_count
total,average,largest_expense_category,largest_expense_amount,above_thresh_count = analyze_expenses(expenses,threshold)

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
print(f"{f'Expenses above GHS {threshold:,.2f}:':<25} {above_thresh_count}")
