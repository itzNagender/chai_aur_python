#6. Factorial Calculator
#Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter The Number: "))
factorial = 1

while number > 0:
    factorial = factorial * number
    number -= 1

print("Foctorial of Given No is: ", factorial)
