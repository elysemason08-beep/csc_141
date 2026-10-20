''''''
# Ciani Mason,
# Difficulty level 5/10

sandwich_orders = ["tuna", "ham", "turkey", "cheese"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches have been made!")

for sandwich in finished_sandwiches:
    print(sandwich)
