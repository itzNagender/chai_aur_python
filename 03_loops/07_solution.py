#7. Validate Input
#Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter Value Between 1 and 10: "))
    if 0 < number <= 10:
        print("Thanks!")
        break
    else:
        print("Invalid Number! Try Again.")