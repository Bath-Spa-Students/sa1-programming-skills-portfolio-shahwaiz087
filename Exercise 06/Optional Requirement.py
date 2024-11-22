# Establish the system's valid password
correct_password = "python123"

# Decide how many password attempts are permitted at most
max_attempts = 5

# Put a counter in place to record the number of attempts
attempts = 0

# Create a loop that keeps going until the right password is entered or all tries have been made
while attempts < max_attempts:
    # Ask the user to input their password while providing a helpful message
    user_password = input("Enter the password: ").strip()
    
    # After every entry, increase the tries counter by one
    attempts += 1

    # Verify that the password you typed is the right one
    if user_password == correct_password:
        # Stop the loop and provide access if the password is correct
        print("Permitted Access. Welcome Back!")
        break
    else:
        # Determine the number of attempts left to notify the user
        remaining_attempts = max_attempts - attempts
        # Inform the user that the password is wrong and show the number of attempts that have been made
        print(f"Incorrect password :( . You have only {remaining_attempts} attempt(s) remaining.")
        
        # Give the user one last warning if they have made all of the permitted tries
        if attempts == max_attempts:
            print("Access is refused, Because of too many unsuccessful attempts, you have been locked out.")
