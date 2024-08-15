tea_types =("Black", "Green", "Oolong")

print(tea_types)
print(tea_types[0])
print(tea_types(-1))

tea_types[0] = "Lemon"

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have Green Tea")

more_tea.count("Herbal")

(black, green, Oolong) = tea_types
print(black)

type(tea_types)