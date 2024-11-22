# A dictionary to keep track of each month's days
# Month numbers are represented by keys (1 for January, 2 for February, etc.), while the days of each month are represented by values
days_in_month = {
    1: 31,   # January
    2: 28,   # February (considering a non-leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Gently prompt the user to enter the month number
try:
    month_number = int(input("Please enter a month number (1-12): ").strip()) # .strip() eliminates unnecessary spaces around input

    # Verify that the month number falls inside a suitable range
    if month_number in days_in_month:
        # Show the number of days in the month that was entered
        print(f"The number of days in month {month_number} is {days_in_month[month_number]}.")
    else:
        # If the input is outside of the range of 1–12, let the user know
        print("Oops! That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
    # Use a message to handle non-integer input
    print("Invalid input. Please enter a numerical value between 1 and 12.")
