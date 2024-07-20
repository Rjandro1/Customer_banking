# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest_rate = float(input("Enter the savings account interest rate: "))
    savings_months = int(input("Enter the number of months for the savings account: "))
    # Call the create_savings_account function and pass the variables from the user.
    create_savings_account = create_savings_account(savings_balance, savings_interest_rate, savings_months)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    savings_interest_earned = savings_account.get_interest() * savings_balance
    savings_updated_balance = savings_account.get_balance()
    print(f"Savings Account: Interest Earned: {savings_interest_earned}, Updated Balance: {savings_updated_balance}")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest_rate = float(input("Enter the CD account interest rate: "))
    cd_months = int(input("Enter the number of months for the CD account: "))


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    cd_account = create_cd_account(cd_balance, cd_interest_rate, cd_months)


    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    cd_interest_earned = cd_account.get_interest() * cd_balance
    cd_updated_balance = cd_account.get_balance()
    print(f"CD Account: Interest Earned: {cd_interest_earned}, Updated Balance: {cd_updated_balance}")
    # Call the main function.
main()
