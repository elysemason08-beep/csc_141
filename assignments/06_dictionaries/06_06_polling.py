''''''
# Ciani Mason
# This was A 7/10
# side note I like this, this is cute.
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

people_to_poll = ["jen", "sarah", "mike", "ciani"]

for person in people_to_poll:
    if person in favorite_languages:
        print("Thank you for responding,", person + "!")
    else:
        print(person + ", please take our favorite languages poll.")