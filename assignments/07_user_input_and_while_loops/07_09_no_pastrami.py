''''''
# Ciani Mason,
# Difficulty level 7/10

sandwich_orders = ["pastrami", "tuna", "pastrami", "turkey", "pastrami", "ham"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
