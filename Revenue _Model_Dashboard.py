"""
PSEUDOCODE

Start

Create variables for:
    Total revenue
    Highest revenue
    Lowest revenue

For each month

    Input revenue

    Add to total

    Check for highest revenue

    Check for lowest revenue

End For

Calculate average revenue

Display summary

End
"""

months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

total_revenue = 0

highest_revenue = None
lowest_revenue = None

highest_month = ""
lowest_month = ""

for month in months:

    revenue = float(input(f"Enter revenue for {month}: R"))

    total_revenue += revenue

    if highest_revenue is None or revenue > highest_revenue:
        highest_revenue = revenue
        highest_month = month

    if lowest_revenue is None or revenue < lowest_revenue:
        lowest_revenue = revenue
        lowest_month = month

average_revenue = total_revenue / 12

print("\n----- REVENUE DASHBOARD -----")

print(f"Total Revenue: R{total_revenue:,.2f}")
print(f"Average Revenue: R{average_revenue:,.2f}")

print(f"\nHighest Month:")
print(f"{highest_month} - R{highest_revenue:,.2f}")

print(f"\nLowest Month:")
print(f"{lowest_month} - R{lowest_revenue:,.2f}")

if highest_revenue > average_revenue:
    print("\nRevenue Trend: Growing")
else:
    print("\nRevenue Trend: Stable")