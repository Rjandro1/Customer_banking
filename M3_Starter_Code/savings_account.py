"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    


    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    instance_of_account_Class = Account(100, .10)
    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = (100 * (10/100 * 12/12))
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = instance_of_account_Class.get_balance() + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    instance_of_account_class.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    instance_of_account_class.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
        updated_balance = instance_of_account_class.get_balance()
        interest_rate = instance_of_account_class.get_interest()

        (updated_balance, interest_rate)