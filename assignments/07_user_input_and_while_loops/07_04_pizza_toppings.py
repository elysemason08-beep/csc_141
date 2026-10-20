''''''
# Ciani Mason,
# Difficulty level 6/10
# I reqalized I was putting strings of my own when we needed the user to put their own.
# I understand this is purely for the user to have creativity themselves and not choose from a list.

prompt = "Please type in a pizza topping you would like to add to your pizza. Type quit when you are finished: "

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
