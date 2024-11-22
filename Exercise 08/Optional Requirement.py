# A pre-made list of names to look through
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Request that the user type a name they wish to search for, eliminating any excess spaces
search_term = input("Type the name you're trying to find: ").strip()

# Utilizing a case-insensitive search, determine whether the entered name is present in the list
if search_term.lower() in [name.lower() for name in names]:
    # Upon locating the name, send a kind success message
    print(f"welldone! '{search_term}' is in the list :) .")
else:
    # Let the user know politely if the name cannot be located
    print(f"'{search_term}' isn't in the list :( .")
