#2. Sum of Even Numbers
#Problem: Calculate the sum of even numbers up to a given number n.

num = int(input("Enter The Number: "))

sum_even = 0
for n in range(1, num+1):
    if n % 2 == 0:
        sum_even += n

print("Sum of Even number till", num, "is:", sum)