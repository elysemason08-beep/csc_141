''''''
#Ciani Mason
# This was way easier now 4/10
# I just realized the n/ is a new line and the loop makes sure
# we dont have to write the print part over and over again.
# It still have it's full functions with a loop instead of a print.
glossary = { "variable": "A name that stores a value.", "list": "A collection of items stored in order.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "Code that repeats a set of instructions.",
    "string": "A sequence of characters."}

for word, meaning in glossary.items():
    print(word, ":", meaning, "\n")