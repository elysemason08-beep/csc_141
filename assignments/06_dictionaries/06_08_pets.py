''''''
# Ciani Mason
# I loved this one it was much easier 
pet_information = {"breed": "german shepherd",
                    "name": "Zero", "age": 3,
                    "owner": "Ciani Mason"}


pet_2 = {"breed": "golden retriever",
            "name": "Max", "age": 2,
            "owner": "Amber Smith"}

pet_3 = {"breed": "beagle",
            "name": "manman", "age": 4,
            "owner": " Ricky Mason"}

pets = [pet_information, pet_2, pet_3]
for pet in pets:
    for key, value in pet.items():
        print(key, ":", value)