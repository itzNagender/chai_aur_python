#6. Transportation Mode Selection
#Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)

dist = int(input("\nEnter the Total Distance in KM: "))

if dist > 15:
    print("Choose Car!\n")
elif dist > 3:
    print("Choose Bike!\n")
elif dist >= 0:
    print("Walk!")
else:
    print("Please Enter a valid Input. Try Again!")
    exit()