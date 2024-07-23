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

    def __str__(self):
        """
        This method should return a string representation of the object that is user-friendly
        """
        return f"Expense(Item: {self.item}, category: {self.category}, price: {self.price:.2f} €)"

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

    display_welcome_msg()

    get_user_confirmation()

    user_prompts()

    # Get user input for expenses
    expense = register_expense_items()
    print(expense)

    # Write the file based on the user expenses
    save_expense_to_file()

    # Read the file and sum the expenses
    summarize_spending()


# add error handling function


def register_expense_items():
    """
    Collect user expense items.
    """
    print("Please enter the name of your expense item. ")
    item_name = input("Enter the item name: ")
    item_price = float(input(f"Enter the price for {item_name}: "))
    print(f"You've purchased the item: {item_name} for {item_price} €.")

    cost_categories = [
        "🏠  Housing", 
        "🚗  Transportation", 
        "🍟  Food", 
        "💇  Personal", 
        "👶  Childcare", 
        "🐈  Pet", 
        "🎮  Entertainment"
    ]

    while True:
        print("Select a category by entering corresponding number: ")
        for ind, category_name in enumerate(cost_categories):
            print(f"    {ind + 1}. {category_name}")

        selected_ind = int(input(f"Enter a number [1 - {len(cost_categories)}]: ")) - 1

        if selected_ind in range(len(cost_categories)):
            selected_category = cost_categories[selected_ind]
            new_expense = Expense(item_name, selected_category, item_price)
            return new_expense
        else:
            print("Invalid selection. Please try again! ")


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

def display_welcome_msg():
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

# BGreen="\[\033[1;32m\]"       # Green
# Color_Off="\[\033[0m\]"       # Text Reset
# Purple="\[\033[0;35m\]"       # Purple

def clear_screen():
    """
    Clear the terminal screen to keep it tidy and display a welcome message.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_user_confirmation():
    """
    Get user confirmation to start the game
    """
    while True:
        response = input("\nWould you like to start? (Type 'Y' for Yes, 'N' for No): ")
        if response.lower() == 'y':
            print("\nGreat! Let's get started. ")
            break
        elif response.lower() == 'n':
            print("\nHave a nice day! Feel free to come back anytime.")
            sys.exit()
        else:
            print("\nInvalid input. Please type 'Y' for Yes or 'N' for No.")

def user_prompts():
    """
     Prompts the user for their net salary and saving goals, calculates the spendable amount, and prints it.
    """
    salary = int(input(f"\nPlease enter you Net-salary: "))
    saving_goals = int(input(f"\nPlease enter you saving goals: "))
    spent = salary - saving_goals
    print(f"Your can spent {spent} €")


if __name__ == "__main__":
    main()
