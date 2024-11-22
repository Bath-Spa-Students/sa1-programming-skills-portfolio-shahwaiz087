# A dictionary that associates the number of days in a non-leap year with each month number (1–12)
days_in_month = {
    1: 31,   # January has 31 days
    2: 28,   # February has 28 days (A non-leap year)
    3: 31,   # March has 31 days
    4: 30,   # April has 30 days
    5: 31,   # May has 31 days
    6: 30,   # June has 30 days
    7: 31,   # July has 31 days
    8: 31,   # August has 31 days
    9: 30,   # September has 30 days
    10: 31,  # October has 31 days
    11: 30,  # November has 30 days
    12: 31   # December has 31 days
}

# Request a month number from 1 to 12 from the user
try:
    month_number = int(input("Enter the number of month (from 1-12): ").strip())  # Eliminates any unnecessary spaces around input

    # Verify that the month number falls inside a suitable range
    if 1 <= month_number <= 12:
        
        # Incase for February (month 2), we need to check for a leap year
        if month_number == 2:
            # Ask the user if it's a leap year
            is_leap = input("Is it a leap year? (yes or no): ").strip().lower()
            # If it's a leap year, there will be 29 days in February; or else there will be 28 days
            days = 29 if is_leap == "yes" else 28
        else:
            # Simply check the dictionary for the number of days in each of the other months
            days = days_in_month[month_number]
        
        # Output the total number of days in the chosen month
        print(f"Number of days in a month {month_number} is {days}.")
    else:
        # If the month number is invalid (not between 1 and 12), let the user know
        print("That's a invalid number of the month. Enter a number from 1 to 12.")

except ValueError:
    # Deal with situations where the user enters words or something other than a number
    print("That's an invalid input. Please enter a number from 1 to 12.")
