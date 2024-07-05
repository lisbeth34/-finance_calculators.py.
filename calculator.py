import math

def get_user_choice():
    """
    Function to get the user's choice of calculation.
    """
    # Display the menu options to the user
    print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
    print("investment   - to calculate the amount of interest you'll earn on interest")
    print("bond         - to calculate the amount you'll have to pay on a home loan\n")
    # Get the user's choice and convert it to lowercase
    choice = input("Enter your choice: ").lower()
    return choice

def get_investment_details():
    """
    Function to get investment details from the user.
    """
    # Prompt the user for investment details
    print("\nProvide the following investment details:")
    amount = float(input("Enter the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = float(input("Enter the number of years you plan on investing for: "))
    interest = input("Do you want 'simple' or 'compound' interest: ").lower()
    return amount, interest_rate, years, interest

def calculate_investment(amount, interest_rate, years, interest):
    """
    Function to calculate and print the amount after investment based on the interest type.
    """
    # Calculate the total amount based on the interest type
    if interest == 'simple':
        total = amount * (1 + interest_rate / 100 * years)
    elif interest == 'compound':
        total = amount * math.pow((1 + interest_rate / 100), years)
    else:
        # Handle invalid interest type
        print("Invalid interest type. Please enter either 'simple' or 'compound'.")
        return
    # Display the total amount after the specified number of years
    print(f"\nAfter {years} years at an interest rate of {interest_rate}%, you will have: {total}")

def main():
    """
    Main function to execute the finance calculator.
    """
    # Get the user's choice
    choice = get_user_choice()
    # Check if the choice is 'investment' and proceed accordingly
    if choice == 'investment':
        amount, interest_rate, years, interest = get_investment_details()
        calculate_investment(amount, interest_rate, years, interest)
    else:
        # Handle invalid choice
        print("Invalid choice. Please enter either 'investment' or 'bond'.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
