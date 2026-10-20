''''''
# Ciani Mason,
# Difficulty level 

dream_vacations = {}

active = True

while active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    dream_vacations[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == "no":
        active = False

print("\n--- Dream Vacation Poll Results ---")

for name, place in dream_vacations.items():
    print(f"{name} would like to visit {place}.")
