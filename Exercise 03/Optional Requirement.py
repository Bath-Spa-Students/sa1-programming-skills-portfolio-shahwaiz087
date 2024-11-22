# Remove any unnecessary whitespace and ask the user to provide their hometown
user_hometown = input("Enter your hometown: ").strip() # .strip() Eliminates unnecessary gaps surrounding the input

# In order to guarantee accurate information, repeatedly ask the user for their age
while True:
    try:
        # Convert the input into an integer
        user_age = int(input("Enter your age: "))
        break  # If conversion is successful, end the loop
    except ValueError:
        # If an invalid integer is entered, display an error
        print("Invalid input. Enter a numerical value for your age.")

# Show the collected data
print("\nUser Information:")
print(f"Name: {user_name}")
print(f"Hometown: {user_hometown}")
print(f"Age: {user_age}")
