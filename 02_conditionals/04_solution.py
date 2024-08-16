#Fruit Ripeness Checker
#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("\nEnter the Fruit Name: ").lower()

if fruit == "banana":
    color = input("\nEnter the Color of Fruit: ").lower()
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("\nPlease Enter the right Color")
        exit()
else:
    print("\nThis fruit is not available or write a fruit name only!\n")
    exit()