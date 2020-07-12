chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

money = int(input())

if money >= sheep:
    animals = money // sheep
    print(f"{animals} sheep" if animals > 1 else f"{animals} sheep")
elif money >= cow:
    animals = money // cow
    print(f"{animals} cows" if animals > 1 else f"{animals} cow")
elif money >= pig:
    animals = money // pig
    print(f"{animals} pigs" if animals > 1 else f"{animals} pig")
elif money >= goat:
    animals = money // goat
    print(f"{animals} goats" if animals > 1 else f"{animals} goat")
elif money >= chicken:
    animals = money // chicken
    print(f"{animals} chickens" if animals > 1 else f"{animals} chicken")
else:
    print("None")
