#4. Reverse a String
#Problem: Reverse a string using a loop.

inp_str = input("Enter The String: ")

reversed_str =""


for char in inp_str:
    reversed_str = char + reversed_str

print("Reversed String is: ", reversed_str)

