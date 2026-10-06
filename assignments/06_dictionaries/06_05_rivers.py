''''''
# Ciani Mason
# This was a 5/10
# I had to remember the for rivers in rivers.items() part
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Mississippi": "United States"
}

for river, country in rivers.items():
    print("The", river, "runs through", country, "\n")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)