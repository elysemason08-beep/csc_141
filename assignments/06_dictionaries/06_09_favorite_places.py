''''''
# Ciani Mason
# This was some actual fun 3/10
favorite_places = {"Ciani": ["New York", "Los Angeles", "Baltimore", "Philadelphia"],
                    "Peyton": ["Miami", "Dallas", "Seattle", " Chicago"],
                    "Ricky": ["Houston", "Denver", "Boston", " Maine"]}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("- " + place.title())

