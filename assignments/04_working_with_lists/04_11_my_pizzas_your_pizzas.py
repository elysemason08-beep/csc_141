''''''
pizzas = ['pepperoni', 'bacon', 'cheese', 'sausage']

friend_pizzas = pizzas.copy()

pizzas.append('mushroom')
friend_pizzas.append('pineapple')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)