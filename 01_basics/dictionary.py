#dictionary
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types["Masala"])     #output: 'Spicy'
print(chai_types.get("Ginger"))  #output: Zesty

#for loop in dictionary             
for chai in chai_types:
    print(chai, chai_types[chai])


for key, value in chai_types.items():
    print(key,value)

#condition in dictionary
if "Masala" in chai_types:
    print("I have masala chai")     #output: I have masala chai


#Addition of new key in dictionary
chai_types["Early Grey"] = "Citrus"

#Deletion of key in dictionary
chai_types.pop("Ginger")

#delete last key
chai_types.popitem()

#delete from the memory
del chai_types["Green"]

#create a copy of dictionary
chai_types_copy = chai_types.copy()

#create dict in the dict
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
    }

print(tea_shop["chai"])     #output:{'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["chai"]["Ginger"])   #output: 'Zesty'

squared_num = {x: x**2 for x in range(10)}  #output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#clear the dictionary
squared_num.clear()


keys = ["Masala", "Ginger", "Green"]
default_value = "Delicious"
#create dict with default value
new_dict = dict.fromkeys(keys, default_value)

print(new_dict)     #output: {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Green': 'Delicious'}

