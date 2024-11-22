# A function to determine whether a given number is odd or even
def check_even_odd(number):
    # The integer is even if it is evenly divisible by two 
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # Otherwise, it's odd
        return f"{number} is odd."

# The main purpose is to process user input and display the outcome
def main():
    # Request the user to enter a number
    try:
        user_number = int(input("Please enter a number: "))
        # Get the outcome message by calling the check_even_odd function
        result_message = check_even_odd(user_number)
        # Print the message of the result
        print(result_message)
    except ValueError:
        # Show an error message if the user inputs a value that isn't an integer
        print("Invalid input. Enter a value in numbers.")

# Run this script straight alone to execute the main function
if __name__ == "__main__":
    main()
