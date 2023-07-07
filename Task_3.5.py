from math import sqrt

len_numbers = int(input("Enter the length of the list of numbers: "))
counting, count = 0, 0
list_numbers = []

while counting != len_numbers:
    prime_number = int(input("Enter numbers that are not prime: "))
    for i in range(2, int(sqrt(prime_number) + 1)):
        if prime_number % i == 0:
            count += 1
    if count != 0:
        list_numbers.append(prime_number)
        counting += 1
    count = 0

print("List of numbers that are not prime:", list_numbers)
