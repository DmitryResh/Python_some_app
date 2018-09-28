import random

print("Welcome To The My Randomiser \nSet The Range Of Random Number")

enter_max = int(input("Enter maximum edge "))

enter_min = int(input("Enter minimum edge "))

number = int(random.uniform(enter_min, enter_max))
print(number)
