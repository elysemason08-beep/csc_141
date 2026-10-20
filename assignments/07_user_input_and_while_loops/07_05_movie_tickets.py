''''''
# Ciani Mason,
# Difficulty level, im really learning on how to break the instructions down
# I sometimes start my code with copying the book and that be wrong so I struggle with 
# have the code structure right
 
prompt = "How old are you? Type quit when finished: "
age = ""

while age != "quit":
    age = input(prompt)

    if age != "quit":
        age = int(age)

        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
