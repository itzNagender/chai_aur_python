#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species = input("\nEnter The Pet Species: ").lower()
pet_age = int(input("Enter The age of your Pet: "))

if pet_species == "cat":
    if pet_age > 5:
        print("AI Suggest Senior Food For Your Cat!")
    elif pet_age > 0:
        print("AI Suggest Puppy Food For Your Cat!")
    else:
        print("Invalid Input")
        exit()
elif pet_species == "dog":
    if pet_age > 2:
        print("AI Suggest Senior Food For Your Dog!")
    elif pet_age > 0:
        print("AI Suggest Puppy Food For Your Dog!")
    else:
        print("Invalid Input")
        exit()
else:
    print("Invalid Input")
    exit()
        

