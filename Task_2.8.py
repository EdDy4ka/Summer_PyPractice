import math

n = int(input("Enter a number 'n': "))
natural_number = math.ceil(math.sqrt(n))

if n == natural_number**2:
    natural_number += 1

print("Given number by task:", natural_number)
