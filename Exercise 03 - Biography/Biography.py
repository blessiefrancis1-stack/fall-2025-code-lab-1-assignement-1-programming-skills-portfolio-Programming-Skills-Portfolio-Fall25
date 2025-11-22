name=input("Enter your full name: ")
hometown=input("Enter your hometown: ")

#Safely convert age to an integer
while True:
    age_input=input("Enter your age: ")
    if age_input.isdigit():
        age=int(age_input)
        break
    else:
        print("Please enter a valid age.")

bio={
    "name": name,
    "hometown": hometown,
    "age": age
}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")



