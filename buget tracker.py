import tkinter as tk
from tkinter import ttk

class PersonalBudgetTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Tracker")

        # Initialize data structures to store income, expenses, and savings goals
        self.income_sources = []
        self.expenses = []
        self.savings_goals = []

        # Main window elements
        self.label_welcome = tk.Label(root, text="Welcome to Personal Budget Tracker", font=("Arial", 16))
        self.label_welcome.pack(pady=10)

        self.button_income_tracker = tk.Button(root, text="Income Tracker", command=self.open_income_tracker)
        self.button_income_tracker.pack()

        self.button_expense_tracker = tk.Button(root, text="Expense Tracker", command=self.open_expense_tracker)
        self.button_expense_tracker.pack()

        self.button_savings_goals = tk.Button(root, text="Savings Goals", command=self.open_savings_goals)
        self.button_savings_goals.pack()

        self.button_reports = tk.Button(root, text="Reports", command=self.open_reports)
        self.button_reports.pack()

        self.button_exit = tk.Button(root, text="Exit", command=root.quit)
        self.button_exit.pack()

    def open_income_tracker(self):
        income_window = tk.Toplevel(self.root)
        income_window.title("Income Tracker")

        # Income Tracker elements
        tk.Label(income_window, text="Income Source:").pack()
        self.entry_income_source = tk.Entry(income_window)
        self.entry_income_source.pack()

        tk.Label(income_window, text="Amount:").pack()
        self.entry_income_amount = tk.Entry(income_window)
        self.entry_income_amount.pack()

        self.button_add_income = tk.Button(income_window, text="Add Income", command=self.add_income)
        self.button_add_income.pack()

    def add_income(self):
        # Add income data to the list and clear the entry fields
        income_source = self.entry_income_source.get()
        income_amount = float(self.entry_income_amount.get())
        self.income_sources.append((income_source, income_amount))

        # Clear entry fields
        self.entry_income_source.delete(0, tk.END)
        self.entry_income_amount.delete(0, tk.END)

    def open_expense_tracker(self):
        expense_window = tk.Toplevel(self.root)
        expense_window.title("Expense Tracker")

        # Expense Tracker elements
        categories = ["Groceries", "Utilities", "Entertainment", "Transportation", "Other"]
        self.selected_category = tk.StringVar()
        self.selected_category.set(categories[0])  # Default category
        self.dropdown_category = ttk.Combobox(expense_window, textvariable=self.selected_category, values=categories)
        self.dropdown_category.pack()

        tk.Label(expense_window, text="Amount:").pack()
        self.entry_expense_amount = tk.Entry(expense_window)
        self.entry_expense_amount.pack()

        self.button_add_expense = tk.Button(expense_window, text="Add Expense", command=self.add_expense)
        self.button_add_expense.pack()

    def add_expense(self):
        # Add expense data to the list and clear the entry fields
        expense_category = self.selected_category.get()
        expense_amount = float(self.entry_expense_amount.get())
        self.expenses.append((expense_category, expense_amount))

        # Clear entry fields
        self.entry_expense_amount.delete(0, tk.END)

    def open_savings_goals(self):
        savings_window = tk.Toplevel(self.root)
        savings_window.title("Savings Goals")

        # Savings Goals elements
        tk.Label(savings_window, text="Savings Goal:").pack()
        self.entry_savings_goal = tk.Entry(savings_window)
        self.entry_savings_goal.pack()

        tk.Label(savings_window, text="Target Amount:").pack()
        self.entry_target_amount = tk.Entry(savings_window)
        self.entry_target_amount.pack()

        tk.Label(savings_window, text="Deadline:").pack()
        self.entry_deadline = tk.Entry(savings_window)
        self.entry_deadline.pack()

        self.button_set_goal = tk.Button(savings_window, text="Set Goal", command=self.set_savings_goal)
        self.button_set_goal.pack()

    def set_savings_goal(self):
        # Add savings goal data to the list and clear the entry fields
        savings_goal = self.entry_savings_goal.get()
        target_amount = float(self.entry_target_amount.get())
        deadline = self.entry_deadline.get()
        self.savings_goals.append((savings_goal, target_amount, deadline))

        # Clear entry fields
        self.entry_savings_goal.delete(0, tk.END)
        self.entry_target_amount.delete(0, tk.END)
        self.entry_deadline.delete(0, tk.END)

    def open_reports(self):
        # Reports window elements
        reports_window = tk.Toplevel(self.root)
        reports_window.title("Reports")

        # Display summary of income sources
        tk.Label(reports_window, text="Income Sources Summary", font=("Arial", 14, "bold")).pack()
        for source, amount in self.income_sources:
            tk.Label(reports_window, text=f"{source}: ${amount:.2f}").pack()

        # Display summary of expenses
        tk.Label(reports_window, text="Expenses Summary", font=("Arial", 14, "bold")).pack()
        for category, amount in self.expenses:
            tk.Label(reports_window, text=f"{category}: ${amount:.2f}").pack()

        # Display savings goals
        tk.Label(reports_window, text="Savings Goals", font=("Arial", 14, "bold")).pack()
        for goal, target, deadline in self.savings_goals:
            tk.Label(reports_window, text=f"{goal}: Target - ${target:.2f}, Deadline - {deadline}").pack()

def main():
    root = tk.Tk()
    app = PersonalBudgetTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

