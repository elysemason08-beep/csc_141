''''''
# Ciani Mason
#  This was easy to and just fun
# All I had to do was add a few more cities and facts.
# diffciulty 3/10 just tedious, enjoyment 9/10
city_1 = {
    "first_city": "Baltimore",
    "population": "569997",
    "County": "United States",
    "fact": "Has a lot of crabs",
    "state": "Maryland",
    "nickname": "Charm City"
}

city_2 = {
    "first_city": "East Orange",
    "population": "148200",
    "County": "New Jersey",
    "fact": "Has a lot of trees",
    "state": "New Jersey",
    "nickname": "The Gateway to New Jersey"
}

city_3 = {
    "first_city": "Atlanta",
    "population": "498000",
    "County": "Georgia",
    "fact": "Has a lot of parks",
    "state": "Georgia",
    "nickname": "The ATL"
}

cities = [city_1, city_2, city_3]

for city in cities:
    for key, value in city.items():
        print(key, ":", value)
    print()