import os
import sys
import random
from time import sleep
from colors import *

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
        return f"\nExpense({Cyan}Item:{Color_Off} {self.item}, {Yellow}category:{Color_Off} {self.category}, {Blue}price:{Color_Off} {self.price:.2f} €)"

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

def register_expense_items():
    """
    Collect user expense items.
    """
    print(f"\n{BYellow}Please enter the name of your expense item.{Color_Off}")
    item_name = get_validated_input(f"\nEnter the item name {Red}(letters only!){Color_Off}: ", "alphabets")
    item_price = float(get_validated_input(f"\nEnter the price for {item_name} {Red}(positive numbers only!){Color_Off}: ", "number"))
    print(f"\n{BGreen}You've purchased the item: {item_name} for {item_price:.2f} €.{Color_Off}.")

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
        print(f"\n{BPurple}Select a category by entering corresponding number: {Color_Off}")
        for ind, category_name in enumerate(cost_categories):
            print(f"\n    {ind + 1}. {category_name}")

        selected_ind = int(get_validated_input(f"\n{BYellow}Please enter a number from the available options{Color_Off}[1 - {len(cost_categories)}]: ", "number")) - 1

        if selected_ind in range(len(cost_categories)):
            selected_category = cost_categories[selected_ind]
            new_expense = Expense(item_name, selected_category, item_price)
            return new_expense
        else:
            print(f"\n{BRed}Invalid selection. Please try again!{Color_Off}")


def save_expense_to_file():
    """
    Save user expense items to a file.
    """
    print("\nSave user expense")

def summarize_spending():
    """
    Summarize user spending from the saved file.
    """
    print("\nSummarize user expense\n")

def display_welcome_msg():
    print()
    print(f"{Yellow}********************************************")
    print("*                                          *")
    print("*         Welcome to Budget Buddy!         *")
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
    print(f"\n{BPurple}Let's see if you are a Richie Rich 💷 or a Brokey Broke 😲 after this month!{Color_Off}")
    print(f"\n{BPurple}Prepare for a fun ride through your finances! 🚀🤑＄＄{Color_Off}")
    print()
    sleep(3)

    print(f"\n{BGreen}Let's calculate your monthly budget based on your income and expenses.{Color_Off}")
    print(f"\n{BGreen}You'll see how much you've spent and how much you have left until next salary on the first of the month.{Color_Off}")


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
        response = input(f"\n{Cyan}Would you like to start? (Type 'Y' for Yes, 'N' for No): {Color_Off}")
        if response.lower() == 'y':
            print(f"\n{BGreen}Great! Let's get started.{Color_Off}")
            break
        elif response.lower() == 'n':
            print(f"\n{BYellow}Have a nice day! Feel free to come back anytime.{Color_Off}\n")
            sys.exit()
        else:
            print(f"\n{BRed}Invalid input. Please type 'Y' for Yes or 'N' for No.{Color_Off}")


def get_validated_input(prompt, input_type, salary=None):
    """
    Validate user input based on the specified input type
    """

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print(f"\n{On_Purple}Please enter a value, this field cannot be empty!{Color_Off}")
            continue

        try:
            if input_type == 'number':
                value = float(user_input)
                if value <= 0:
                    print(f"\n{Red}Invalid input. Please enter positive numbers only!{Color_Off}")
                    continue

            elif input_type == 'salary':
                value = float(user_input)
                if value < 1000:
                    print(f"\n{BRed}Invalid salary.{Color_Off} {Red}Salary must be at least 1000 €!{Color_Off}")
                    continue

            elif input_type == 'saving_goals':
                value = float(user_input)
                if value <= 0 or (salary is not None and value >= salary):
                    print(f"{BRed}Invalid input.{Color_Off} {Red}Saving goals must be positive and less than the salary {salary} €!{Color_Off}")
                    continue

            elif input_type == 'alphabets':
                if not user_input.isalpha():
                    print(f"\n{Red}Please enter letters only!{Color_Off}")
                    continue

            else:
                print(f"\n{BRed}Invalid type specified. Please enter a valid input type.{Color_Off}")
                continue

            return user_input

        except ValueError:
            print(f"\n{Red}Invalid input. Please enter a valid number!{Color_Off}")
            continue

def user_prompts():
    """
     Prompts the user for their net salary and saving goals, calculates the spendable amount, and prints it.
    """
    salary = float(get_validated_input(f"\nPlease enter your net salary {Red}(minimum 1000 €){Color_Off}: ", "salary"))
    saving_goals = float(get_validated_input(f"\nPlease enter your saving goals {Red}(must be positive and less than your salary {salary:.2f} €){Color_Off}: ", "saving_goals", salary))
    spent = salary - saving_goals
    print(f"\n{On_Green}Your can spent {spent:.2f} €{Color_Off}")


if __name__ == "__main__":
    main()
