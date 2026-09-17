''''''
cubes = [number ** 3 for number in range(1, 11)]

print(cubes)
print(cubes[3:6])
print(cubes[6:9])
print(cubes[9:12])
print("The first three items in the list are:")
print(cubes[0:3])
print("Three items from the middle of the list are:")
print(cubes[3:6])
print("The last three items in the list are:")
print(cubes[9:12])
print(f"My favorite cubes are {cubes[0:3]}")