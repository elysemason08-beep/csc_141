''''''
# Ciani Mason
# I also liked this one and it's easier now for me,
# I just build off older ones ad it becomes easier to udnertsand.

city_1 ={
         "first_city ":"Baltimore",
         "population":"569997",
         "County":"United states",
         "fact":"Has a lot of crabs"
         }

 # East Orange, New Jersey, Atlanta, Georgia

city_2 = { "first_city ":"East Orange",
           "population":"148200",
           "County":"New Jersey",
           "fact":"Has a lot of trees"
         }

city_3 = { "first_city ":"Atlanta",
           "population":"498000",
           "County":"Georgia",
           "fact":"Has a lot of parks"
         }


cities = [city_1, city_2, city_3]
for city in cities:
    for key, value in city.items():
        print(key, ":", value)