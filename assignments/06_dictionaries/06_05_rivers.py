''''''
# Ciani Mason
#
#
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