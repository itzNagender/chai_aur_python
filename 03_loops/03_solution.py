'''
3. Multiplication Table Printer
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
'''
num = int(input("Enter the Number: "))

for n in range(1, 11):
    if n == 5:
        continue
    print(num, "x", n, "=", num*n)
    