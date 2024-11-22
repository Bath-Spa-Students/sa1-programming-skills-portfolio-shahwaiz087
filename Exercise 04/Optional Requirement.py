# For the quiz, a dictionary listing nations and their capitals
# The values are the capitals of the countries, while the keys are their names
quiz_data = {
    "France": "Paris",
    "Pakistan": "Islamabad",
    "UAE": "Abu Dhabi",
    "Saudi Arabia": "Riyadh",
    "Turkey": "Istanbul",
    "Oman": "Muscat",
    "Russia": "Moscow",
    "Iran": "Tehran",
    "Switzerland": "Bern",
    "Greece": "Athens"
}

# Variable to monitor the user's rating
score = 0

# Go through each pair of capitals and countries in the quiz
for country, capital in quiz_data.items():
    # Request the user's current country's capital
    user_answer = input(f"Capital of {country}? ").strip() # .strip() Eliminate unnecessary spaces around input

    # Verify that the response is accurate, disregarding case variations
    if user_answer.lower() == capital.lower():
        # If accurate, note it and raise the score
        print("Correct :).")
        score += 1
    else:
        # If wrong, give the right response
        print(f"Wrong :( , The capital of {country} is {capital}.")

# Encourage the user by displaying their ultimate score
print(f"\nWell done!!! You scored {score} out of {len(quiz_data)}.")
