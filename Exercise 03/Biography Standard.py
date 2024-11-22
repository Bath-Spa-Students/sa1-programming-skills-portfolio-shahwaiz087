# Give personal information variables
name = "Shahwaiz"  # Name in a string
hometown = "Pakistan"    # The string "hometown"
age = 18                 # An integer "age"

# Use descriptive keys to keep material organized in a dictionary
info = {
    "Name": name,        # The value of "Name" in the key
    "Hometown": hometown, # "Hometown" as a key with hometown value
    "Age": age            # The value of "Age" in the key
}

# Every piece of information should be printed on a separate line
print(f"{info['Name']}\n{info['Hometown']}\n{info['Age']}")
