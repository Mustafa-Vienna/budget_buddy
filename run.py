import os
import sys
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
    
# Utility functions
def clear_screen():
    """
    Clear the terminal screen to keep it tidy and display a welcome message.
    """
    os.system("cls" if os.name == "nt" else "clear")

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
    sleep(0.5)
    print(f"\n{BGreen}Let's calculate your monthly budget based on your income and expenses.{Color_Off}")
    print(f"\n{BGreen}You'll see how much you've spent and how much you have left until next salary on the first of the month.{Color_Off}")


def get_user_confirmation():
    """
    Get user confirmation to start the game
    """
    while True:
        response = input(f"\n{Cyan}Would you like to start? (Type 'y' for Yes, 'n' for No): {Color_Off}")
        if response.lower().strip() == 'y':
            print(f"\n{BGreen}Great! Let's get started.{Color_Off}")
            break
        elif response.lower().strip() == 'n':
            print(f"\n{BYellow}Have a nice day! Feel free to come back anytime.{Color_Off}\n")
            sys.exit()
        else:
            print(f"\n{BRed}Invalid input. Please type 'Y' for Yes or 'N' for No.{Color_Off}")

# Input validation functions
def get_validated_input(prompt, validation_function, *args):
    """
    Validate user input using the specified validation function
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(f"\n{On_Purple}Please enter a value, this field cannot be empty!{Color_Off}")
            continue
        if validation_function(user_input, *args):
            return float(user_input) if validation_function in [check_number, check_salary, check_saving_goals, check_item_price] else user_input

def check_number(value):
    """
    Validate that the input is a positive number.
    """
    try:
        value = float(value)
        if value <= 0:
            print(f"\n{Red}Invalid input. Please enter positive numbers only!{Color_Off}")
            return False
        return True
    except ValueError:
        print(f"\n{Red}Invalid input. Please enter a valid number!{Color_Off}")
        return False

def check_salary(value):
    """
    Validate that the salary input is a number and at least 1000 €.
    Because Austrian minimum wage in 2024 is €1,766.92 per month before taxes for full-time work
    """
    try:
        value = float(value)
        if value < 1000:
            raise ValueError(f"\n{BRed}Invalid salary.{Color_Off} {Red}Salary must be at least 1000 €!{Color_Off}")
            return False
        return True
    except ValueError:
        print(f"\n{Red}Invalid input. Please enter a valid number!{Color_Off}")
        return False

def check_saving_goals(value, salary):
    """
    Validate that the saving goals input is a positive number less than the salary
    """
    try:
        value = float(value)
        if value <= 0 or value >= salary:
            raise ValueError(f"{BRed}Invalid input.{Color_Off} {Red}Saving goals must be positive and less than the salary {salary} €!{Color_Off}")
            return False
        return True
    except ValueError:
        print(f"\n{Red}Invalid input. Please enter a valid number!{Color_Off}")
        return False


def check_item_price(value, remaining_budget):
    """
    Validate that the item price is a positive number less than the remaining budget
    """
    try:
        value = float(value)
        if value <= 0 or value > remaining_budget:
            print(f"{BRed}Invalid input.{Color_Off} {Red}Item price must be positive and less than the remaining budget {remaining_budget:.2f} €!{Color_Off}")
            return False
        return True
    except ValueError:
        print(f"\n{Red}Invalid input. Please enter a valid number!{Color_Off}")
        return False

def check_alphabets(value):
    """
    Validate that the input consists only of alphabets.
    """
    if not value.isalpha():
        print(f"\n{Red}Please enter letters only!{Color_Off}")
        return False
    return True


def register_expense_items(remaining_budget):
    """
    Collect user expense items.
    """
    print(f"\n{BYellow}Please enter the name of your expense item.{Color_Off}")
    item_name = get_validated_input(f"\nEnter the item name {Red}(letters only!){Color_Off}: ", check_alphabets)
    item_price = get_validated_input(f"\nEnter the price for {item_name} {Red}(positive numbers only!){Color_Off}: ", check_item_price, remaining_budget)
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
        for index, category_name in enumerate(cost_categories):
            print(f"\n    {index + 1}. {category_name}")

        selected_index = int(get_validated_input(f"\n{BYellow}Please enter a number from the available options{Color_Off}[1 - {len(cost_categories)}]: ", check_number)) - 1

        if selected_index in range(len(cost_categories)):
            selected_category = cost_categories[selected_index]
            return Expense(item_name, selected_category, item_price)
        else:
            print(f"\n{BRed}Invalid selection. Please try again!{Color_Off}")

def print_registered_exp(expenses):
    print(f"\n{BPurple}Here are your registered expenses:{Color_Off}")
    for exp in expenses:
        print(exp)


def add_new_expenses(expenses):
    """
    This function Ask user to add more expenses
    """

    while True:
        response = input(f"\n{Cyan}Would you like to add another item? (Type 'y' for Yes, 'n' for No) : {Color_Off}")
        if response.lower().strip() == 'y':
            print(f"\n{BGreen}Great! Let's get continue.{Color_Off}")
            return True
        elif response.lower().strip() == 'n':
            print_registered_exp(expenses)
            print(f"\n{BYellow}Have a nice day! Feel free to come back anytime.{Color_Off}\n")
            return False
        else:
            print(f"{BRed}Invalid input. Please type 'Y' for Yes or 'N' for No.{Color_Off}")


def main():
    """
    Start the program and run the main functions.
    """
    clear_screen()
    display_welcome_msg()
    get_user_confirmation()

    # Initialize variables
    salary = get_validated_input(f"\nPlease input your monthly net salary {Red}(minimum 1000 €){Color_Off}: ", check_salary)
    saving_goals = get_validated_input(f"\nPlease enter your saving goals {Red}(must be positive and less than your salary {salary:.2f} €){Color_Off}: ", check_saving_goals, salary)
    available_budget = salary - saving_goals
    expenses = []

    def print_remaining_budget():
        print(f"\n{BGreen}Remaining budget: {available_budget:.2f} €{Color_Off}")

    while True:
        print(f"\n{BYellow}You have {available_budget:.2f} € remaining in your budget.{Color_Off}")
        expense = register_expense_items(available_budget)
        expenses.append(expense)
        available_budget -= expense.price # Deduct the price from the available budget

        print_remaining_budget()
        if available_budget <= 0:
            print(f"\n{BRed}No more budget left!{Color_Off}")
            print_registered_exp(expenses)
            break
        if not add_new_expenses(expenses):
            break
        print_registered_exp(expenses)
        print_remaining_budget()


# run the app only when we run it directly instead of importing it
if __name__ == "__main__":
    main()