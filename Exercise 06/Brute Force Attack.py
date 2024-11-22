# Establish the system's valid password
correct_password = "12345"

# Decide how many password attempts are permitted at most
max_attempts = 4

# Put a counter in place to record the number of attempts
attempts = 0

# Create a loop that keeps going until the right password is entered or all tries have been made
while attempts < max_attempts:
    # Request the user's password
    user_password = input("Enter the password: ").strip()
    
    # For privacy, conceal the entered password with attributes
    masked_password = '*' * len(user_password)
    
    # After every entry, increase the number of attempts by one
    attempts += 1

    # Verify that the password entered corresponds to the one that is stored
    if user_password == correct_password:
        # If so, allow access and close the loop
        print("Permitted Access. Welcome Back!")
        break
    else:
        # If it's wrong, show the masked password and an error message
        print(f"Incorrect password: {masked_password}")
        
        # If this is the user's second-to-last try, give them a clue
        if attempts == max_attempts - 1:
            print("Hint: Numbers Only :)")
        
        # Lock the user out and let them know if they've tried everything
        if attempts == max_attempts:
            print("Access is refused, Because of too many unsuccessful attempts, you have been locked out.")
