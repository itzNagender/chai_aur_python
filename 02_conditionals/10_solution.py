#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species = input("\nEnter The Pet Species: ").lower()
pet_age = int(input("Enter The age of your Pet: "))

if pet_species == "cat":
    if pet_age > 5:
        print("AI Suggest Puppy Food For Your Pet!")
    else:
        print()
        

