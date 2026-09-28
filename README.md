# Business Expense Analyzer

A reusable Python program that loads business expense data from a CSV file, analyzes key spending metrics, and generates a formatted summary report.

## Overview

The Business Expense Analyzer is a Python program designed to analyze structured business expense data and generate a summary of key spending metrics.

The program loads expense records from a CSV file using Python's built-in `csv` module and `DictReader`. The records are converted into a list of dictionaries so they can be processed by reusable analysis functions.

The user can also enter a spending threshold when running the program. The threshold is validated to ensure that it is a positive number before the analysis is performed.

The program calculates:

* Total expenses
* Average expense
* Largest expense and its category
* Number of expenses above a user-defined threshold

This project demonstrates how data can move from a structured external file into a Python analysis workflow while keeping the analysis functions reusable.

## Features

* Loads business expense data from a CSV file.
* Uses `csv.DictReader` to read structured records.
* Converts CSV values from strings into appropriate Python data types.
* Stores expense records using a list of dictionaries.
* Calculates total business expenses.
* Calculates the average expense.
* Identifies the largest expense amount and its category.
* Allows the user to enter a custom spending threshold.
* Validates the threshold to ensure it is greater than zero.
* Handles invalid numeric input using `try`/`except`.
* Counts the number of expenses above the selected threshold.
* Displays expense records in a formatted report.
* Generates a summary containing the key spending metrics.

## What I Learned

Through this project, I practiced and strengthened the following Python concepts:

* Using `for` and `while` loops to process data and repeat operations.
* Working with lists and dictionaries.
* Creating and working with lists of dictionaries to represent structured business data.
* Accessing dictionary values using keys.
* Defining functions and using parameters to make code reusable.
* Using `return` to send calculated results from functions.
* Combining multiple functions to build a larger analysis program.
* Using accumulators to calculate totals.
* Using counters to count records that meet specific conditions.
* Using conditional statements to apply business rules.
* Using `try`/`except` to handle invalid numeric input.
* Using Boolean variables to track validation state.
* Working with CSV files using Python's built-in `csv` module.
* Using `csv.DictReader` to read CSV data using column names.
* Converting CSV values from strings into numeric data types using `float()`.
* Separating data loading from data analysis.
* Protecting calculations from division-by-zero errors.
* Using formatted strings (`f-strings`) to present numerical results clearly.
* Formatting output using field width, alignment, and number formatting.
* Using Git and GitHub to track and document project development.

## How It Works

1. The program opens `expenses.csv` and uses `csv.DictReader` to read the expense records.

2. Each CSV row is converted into a Python dictionary containing a `category` and an `amount`.

3. The dictionaries are stored in an `expenses` list.

4. The program asks the user to enter an expense threshold.

5. The threshold is converted to a `float` and validated. The program rejects non-numeric values and thresholds that are zero or negative.

6. The `calculate_total()` function loops through the expense records and adds the amounts together.

7. The `calculate_average()` function counts the expense records and calculates the average expense. It also handles the case where there are no expense records.

8. The `find_largest_expense()` function compares expense amounts and identifies both the largest amount and its category.

9. The `expenses_above_threshold()` function compares each expense against the user-defined threshold and counts the expenses whose amounts are greater than it.

10. The `analyze_expenses()` function brings the individual analysis functions together and returns the key results.

11. Formatted `print()` statements display the expense records and calculated results in a structured summary report.

## Example Output

```text
Enter expense threshold: 500
Thank You!

BUSINESS EXPENSE ANALYZER

EXPENSES
-------------------------
Rent                : GHS 2,000.00
Salaries            : GHS 4,500.00
Marketing           : GHS 1,200.00
Transport           : GHS 600.00
Utilities           : GHS 450.00
Software            : GHS 750.00

SUMMARY
-------------------------
Total expenses:           GHS 9,500.00
Average expense:          GHS 1,583.33
Largest expense:          Salaries
Largest amount:           GHS 4,500.00
Expenses above GHS 500.00: 5
```

## Technologies Used

* Python 3
* Python `csv` module
* Python IDLE
* Git
* GitHub

## Project Structure

```text
business_expense_analyzer/
│
├── business_expense_analyzer.py
├── expenses.csv
└── README.md
```

### `business_expense_analyzer.py`

Contains the Python program used to load, analyze, validate, and report business expense data.

### `expenses.csv`

Contains the business expense records used by the analyzer.

### `README.md`

Contains the project documentation, including the project overview, features, concepts learned, workflow, example output, and future improvements.

## Future Improvements

Possible improvements for future versions include:

* Allowing users to enter new expense records directly through the program.
* Adding percentage calculations to show how much each category contributes to total expenses.
* Adding more detailed expense categories and analysis.
* Adding charts and visualizations to make spending patterns easier to understand.
* Using pandas for more advanced data analysis.
* Adding additional business spending metrics.
* Improving the user interface and report presentation.

## Project Evolution

This project was developed incrementally as I progressed through my Python learning journey. Each major stage was committed to Git so the development process can be reviewed through the repository's commit history.

### Version 1 — Initial Analyzer

- Stored expenses directly in Python using a list of dictionaries.
- Added reusable functions for total, average, largest expense, and threshold analysis.
- Generated a formatted console report.

### Version 2 — CSV Data & Validation

- Moved expense data into a CSV file.
- Added CSV loading using `csv.DictReader`.
- Added user-defined expense thresholds.
- Added input validation using `try`/`except`.
- Added protection against calculating an average from an empty dataset.

The Git history contains the commits showing how the project evolved from the initial analyzer to the current version.

## Project Status

**Current version:** CSV-based business expense analysis with configurable threshold validation.

The project has evolved from a hard-coded Python expense analyzer into a program that separates data loading, validation, analysis, and reporting.

## Disclaimer

This project is a Python learning project designed to demonstrate data loading, validation, analysis, and reporting techniques. The results are based solely on the data contained in the project and should not be considered professional financial or accounting advice.
