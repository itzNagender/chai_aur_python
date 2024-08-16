#7. Coffee Customization
#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
order_size = input("\nChoose the size of Coffee:-\n Small, Medium, Large: ").lower()

extra_shot = input("\nWould you like to add Extra shot of Espreso? (Yes/No): ").lower()

if extra_shot == "yes":
    extra_shot = True
elif extra_shot == "no":
    extra_shot == False
else:
    print("Please Enter Yes or No")
    exit()

if extra_shot == True:
    coffee = order_size + " Coffee with extra shot of espresso"
else:
    coffee = order_size + " Coffee."

print(coffee)