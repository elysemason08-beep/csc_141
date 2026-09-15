""""""
guests = ['Miracle', 'Peyton', 'Amber']

for guest in guests:
    if guest == 'Amber':
        print("Amber, you seem so genuine as my newest friend. You get French fries. Happy return aboard!")
    elif guest == 'Miracle':
        print("Miracle, you are like my sister. Therefore, you get a diamond-level badge; here's your lobster mac and cheese. Welcome aboard!")
    elif guest == 'Peyton':
        print("Peyton, you are my sister! Step or not, you earned the diamond-level badge; here's your lobster and shrimp; you're already aboard!")
print("Sad news: Amber cannot make it to dinner tonight; she's sick.")
guests[2] = 'Keke'
print(f"Keke, welcome to dinner! You get French fries. Welcome aboard!")
print("Great news! I was given a bigger table, so now I can invite more guests to dinner!")
guests.insert(0, 'Siani')
guests.insert(2, 'Lilly')
guests.append('Jasmine')
guests.append('shawn')

print("Here is the updated guest list:")
for guest in guests:
    if guest == 'Amber':
        print("Amber, you seem so genuine as my newest friend. You get French fries. Happy return aboard!")
    elif guest == 'Miracle':
        print("Miracle, you are like my sister. Therefore, you get a diamond-level badge; here's your lobster mac and cheese. Welcome aboard!")
    elif guest == 'Peyton':
        print("Peyton, you are my sister! Step or not, you earned the diamond-level badge; here's your lobster and shrimp; you're already aboard!")
    elif guest == 'Keke':
        print(f"Keke, welcome to dinner! You get French fries. Welcome aboard!")
    elif guest == 'Siani':
        print(f"Siani, welcome to dinner! You get French fries. Welcome aboard!")
    elif guest == 'Lilly':
        print(f"Lilly, welcome to dinner! You get French fries. Welcome aboard!")
    elif guest == 'Jasmine':
        print(f"Jasmine, welcome to dinner! You get French fries. Welcome aboard!")
    elif guest == 'shawn':
        print(f"shawn, welcome to dinner! You get French fries. Welcome aboard!")
print("bad news: My new dinner table won't arrive in time, so I can only invite two people for dinner im crushed.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print(f"{guests[0]}, you're still invited to dinner!")

print(f"{guests[1]}, you're still invited to dinner!")

del guests[1]
del guests[0]

print(guests)