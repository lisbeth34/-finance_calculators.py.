import math

# Display the options to the user
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("\n")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Get user choice
choice = input("\nEnter your choice: ").lower()

# Check user choice and calculate accordingly
if choice == "investment":
    # Get user input for investment calculation
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan on investing for: "))
    interest = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculate and print the total amount based on the type of interest
    if interest == "simple":
        A = P * (1 + r * t)
        print(f"\nThe total amount after {t} years with simple interest is: {A}")
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        print(f"\nThe total amount after {t} years with compound interest is: {A}")
    else:
        print("\nError: Invalid interest type. Please enter 'simple' or 'compound'.")

elif choice == "bond":
    # Get user input for bond calculation
    P = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    n = int(input("Enter the number of months you plan to take to repay the bond: "))

    # Calculate the monthly interest rate
    i = annual_rate / 12

    # Calculate and print the monthly repayment amount
    repayment = (i * P) / (1 - (1 + i) ** -n)
    print(f"\nThe monthly repayment amount is: {repayment}")

else:
    print("\nError: Invalid selection. Please enter 'investment' or 'bond'.")
