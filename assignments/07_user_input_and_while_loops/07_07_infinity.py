''''''
# Ciani Mason,
# Difficulty level 6/10


print("Welcome to the Unlimited Money Machine!")

while True:
    age = input("Enter your age to claim unlimited money: ")

    if age.isdigit() and int(age) > 0:
        print(f"You are {age} years old!")
        print("Congratulations! You qualify for UNLIMITED MONEY! 💰")
    else:
        print("Please enter a valid age above 0.")

    print("The Unlimited Money Machine is still running!")
    print("------------------------------------------------")
