# Ask the user the question
answer=input("What is the capital of France? ")

# Check the answer (case-insensitive)
if answer.strip().lower()=="paris":
    print("Correct! Paris is the capital of France.")
else:
    print("Wrong answer. The correct answer is Paris.")

# Dictionary of European countries and their capitals
Quiz={
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Bruseels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Greece": "Athens"
}

print("Europeans Capital Quiz!\n")

#Loop through the dictionary and ask each question
for country, capital in Quiz.items():
    answer=input(f"What is the capital of {country}? ")

    #Case insensitive check
    if answer.strip().lower()==capital.lower():
        print("Correct!\n")
    else:
        print(f"Wrong. The capital of {country} is {capital}.\n")

