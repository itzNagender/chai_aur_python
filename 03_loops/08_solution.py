# Prime Number Checker
#Problem: Check if a number is prime.

number = int(input("Enter The Number: "))

#Approach 1:
counter = 0
for n in range(1, number+1):
    if number % n == 0:
        counter += 1


if counter == 2:
    print("The Given Number is a Prime Number!")
else:
    print("The Given Number is not a Prime Number")


#Approach 2:
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break


print(is_prime)


