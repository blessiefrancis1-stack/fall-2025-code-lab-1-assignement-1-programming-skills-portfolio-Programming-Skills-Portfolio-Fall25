correct_password="12345"
password=input("Enter the password")
while password !=correct_password:
    print("Incorrect password. Try again.")
    password=input("Enter the password:")
print("Access granted! Password is correct.")
