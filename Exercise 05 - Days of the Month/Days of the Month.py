# Dictionary mapping month numbers to number of days
days_in_month={
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for a month number
month=input("Enter a month number (1-12): ")

# Validate input
if month.isdigit():
    month=int(month)
    if 1<=month<=12:
        print(f"Number of days: {days_in_month[month]}")
    else:
        print("Error: Please enter a valid month number between 1 and 12.")
else:
    print("Error Invalid input. Please enter a numeric month.")
    
           