''''''
# Ciani Mason,
# Difficulty level 6/10
# I had to re write this to many times i got frsutrated. 

 
number = input("Enter a number: ")
number = int(number)

remainder = number % 10

if remainder == 0:
    print(f"{number} is a multiple of 10.")
    print("It divides evenly by 10.")
else:
    print(f"{number} is not a multiple of 10.")
    print(f"The remainder is {remainder}.")
