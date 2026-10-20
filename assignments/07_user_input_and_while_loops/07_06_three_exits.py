''''''
# Ciani Mason,
# Difficulty level 3/10 
 
prompt = "what age is your family member Type quit when finished: "
age = ""

while age != "quit":
    age = input(prompt)

    if age != "quit":
        age = int(age)

        if age < 53:
            print("Your insurance is free!")
        elif age <= 12:
            print("Your insurance costs $10.")
        else:
            print("Your insurance costs $15.")
