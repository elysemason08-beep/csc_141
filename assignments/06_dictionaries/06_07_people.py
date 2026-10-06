''''''
# 6/10 
# The first part was easy but this was teidious and
# somtimes i forget the right synatx for the loop at the end
# because it changes with the data type.
person_information = {
    "first_name": "Ciani",
    "last_name": "Mason",
    "age": 18,
    "city": "Philadelphia"
}

person_2 = {
    "first_name": "Amber",
    "last_name": "Smith",
    "age": 19,
    "city": "Philadelphia"
}

person_3 = {
    "first_name": "Jasmine",
    "last_name": "Brown",
    "age": 18,
    "city": "Darby"
}

people = [person_information, person_2, person_3]
for person in people:
    for key, value in person.items():
        print(key, ":", value)