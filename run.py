import os
import sys
import random
from time import sleep

class Expense:
    """
    Represents an expense.

    Attributes:
        item (str): Description of the expense item (e.g., cat food, milk...).
        category (int): Category of the expense (e.g., 1 for Housing, 2 for Transportation...).
        price (float): Amount of money spent on the expense.
    """

    def __init__(self, item, category, price):
        self.item = item
        self.category = category
        self.price = price

def main():
    """
    Start the program and run the main functions.

    Steps:
    1. Show a welcome message.
    2. Collect user expenses.
    3. Save expenses to a (CSV) file.
    4. Read the expenses data from the file.
    """
    clear_screen()

    # Get user input for expenses
    register_expense_items()

    # Write the file based on the user expenses
    save_expense_to_file()

    # Read the file and sum the expenses
    summarize_spending()

def register_expense_items():
    """
    Collect user expense items.
    """
    print("Collect user expense")

def save_expense_to_file():
    """
    Save user expense items to a file.
    """
    print("Save user expense")

def summarize_spending():
    """
    Summarize user spending from the saved file.
    """
    print("Summarize user expense")

def clear_screen():
    """
    Clear the terminal screen to keep it tidy and display a welcome message.
    """
    os.system("cls" if os.name == "nt" else "clear")

    print()
    print("********************************************")
    print("*                                          *")
    print("*          Welcome to Budget Buddy!        *")
    print("*                                          *")
    print("*    🏠 Calculate your income & expenses   *")
    print("*      on a monthly basis. Print results   *")
    print("*               to the screen.             *")
    print("*                                          *")
    print("*      📈 Please enter whole numbers       *")
    print("*       only. No decimals, please!         *")
    print("*                                          *")
    print("********************************************")
    print()
    print("Let's see if you are a Richie Rich 💷 or a Brokey Broke 😲 after this month!")
    print("Prepare for a fun ride through your finances! 🚀🤑＄＄")
    print()
    sleep(3)

    print("\nLet's calculate your monthly budget based on your income and expenses.")
    print("\nYou'll see how much you've spent and how much you have left until next salary on the first of the month.")

if __name__ == "__main__":
    main()
