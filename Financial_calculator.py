# Import the math module so that mathematical functions can be used.
import math

# Display a menu with the options investment and bond.
print("""
Investment - to calculate the amount of interest you'll earn on your investment.
Bond - to calculate the amount you'll have to pay on a home loan.
""")

# Ask the user to choose either investment or bond.
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Check whether the user selected investment.
if choice == "investment":

    # Ask the user to enter the deposit amount.
    deposit = float(input("Enter the amount of money you are depositing: "))

    # Ask the user to enter the interest rate.
    interest_rate = float(input("Enter the interest rate (%): "))

    # Ask the user to enter the number of years.
    years = int(input("Enter the number of years you plan to invest: "))

    # Ask the user to choose simple or compound interest.
    interest = input("Enter 'simple' or 'compound' interest: ").lower()

    # Convert the interest rate from a percentage to a decimal.
    r = interest_rate / 100

    # If the user selected simple interest, calculate the final amount.
    if interest == "simple":
        amount = deposit * (1 + r * years)
        print(f"The total amount after {years} years is: R{amount:.2f}")

    # If the user selected compound interest, calculate the final amount.
    elif interest == "compound":
        amount = deposit * math.pow((1 + r), years)
        print(f"The total amount after {years} years is: R{amount:.2f}")

    # Display an error message if the interest type is invalid.
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

# Check whether the user selected bond.
elif choice == "bond":

    # Ask the user to enter the present value of the house.
    present_value = float(input("Enter the present value of the house: "))

    # Ask the user to enter the annual interest rate.
    interest_rate = float(input("Enter the annual interest rate (%): "))

    # Ask the user to enter the repayment period in months.
    months = int(input("Enter the number of months to repay the bond: "))

    # Convert the annual interest rate to a monthly decimal rate.
    i = (interest_rate / 100) / 12

    # Calculate the monthly bond repayment.
    repayment = (i * present_value) / (1 - (1 + i) ** (-months))

    # Display the monthly repayment amount.
    print(f"Your monthly bond repayment is: R{repayment:.2f}")

# Display an error message if the menu selection is invalid.
else:
    print("Invalid selection. Please enter either 'investment' or 'bond'.")

#if bond then ask, investment? or vise versa OR done to exit the calculator
#Exit text or message eg."thanks for using my calculator"
