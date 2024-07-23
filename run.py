import os
import sys
import random
from time import sleep

class Expense:
    """
    Represents an expense

    Attributes:
        item (str): Description of the expense item (e.g., cat food, milk...).
        category (int): Category of the expense (e.g., 1 for Housing, 2 for Transportation...)
        price (float): Amount of money spent on the expense.
    """

    def __init__(self, item, category, price):
        self.item = item
        self.category = category
        self.price = price

def main():
    """
    # Get user input for expenses

    # Write the file based on the user expenses

    # Read the file and sum the expenses
    """
    print("Something")



def clear_screen():
    """
    This function clears the terminal screen to keep it tidy and clean
    """
    os.system("cls" if os.name == "nt" else "clear")

    print()
    print("********************************************")
    print("*                                          *")
    print("*          Welcome to Budget Buddy !       *")
    print("*                                          *")
    print("*    🏠 Calculate your income & expenses   *")
    print("*      on a monthly basis. Print results   *")
    print("*               to the screen.             *")
    print("*                                          *")
    print("*      📈 Please enter whole numbers       *")
    print("*       only. No decimals, Please !!       *")
    print("*                                          *")
    print("********************************************")
    print()
    print("Let's see if you are a Richie Rich 💷 or a Brokey Broke 😲 after this month! ")
    print("Prepare for a fun ride through your finances! 🚀🤑＄＄")
    print()
    sleep(3)

    print("\nLet's calculate your monthly budget based on your income and expenses.")
    print("\nYou'll see how much you've spent and how you have left until next salary on the first of the month.")

if __name__ == "__main__":
    clear_screen()
    expense = Expense("food", 2, 5)
    print("--")

    main()

        # response = input("\nWould you like to start? (Type 'Y' for yes, 'N' for No.):")

        # if response.upper() == 'Y':
        #     print("\nGreat!  Let's get started.")
        # elif response.upper() == 'N':
        #     print("\nNo problem! Feel free to come back anytime.")
        # else:
        #     print("\nInvalid input. Please type 'Y' for Yes or 'N' for No. ")
