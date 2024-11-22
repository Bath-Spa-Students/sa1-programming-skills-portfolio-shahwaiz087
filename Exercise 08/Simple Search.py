# A list of names to look up
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Request that the user type a name they wish to search for, eliminating any excess spaces
search_name = input("Type the name you're trying to find: ").strip()

# Use the Flag to monitor if the name is discovered during the search
found = False

# Check if the user's input matches each name in the list by looping over them
for name in names:
    # To make sure the search is case-insensitive, change both names to lowercase
    if name.lower() == search_name.lower():
        # Set 'found' to True and notify the user if a match is discovered
        found = True
        print(f"Welldone! '{search_name}' is in the list :) .")
        break  # Since we discovered the name, get out of the loop early

# Inform the user if the loop ends and the name was not found
if not found:
    print(f"'{search_name}' is not in the list :( .")
