from random import randint

len_number = int(input("Enter the length of the list: "))
list_numbers = []
list_numbers_square = []

for i in range(0, len_number):
    list_numbers.append(randint(1, 20))
    list_numbers_square.append(list_numbers[i]**2)

print("List of generated numbers:", list_numbers)
print("List of squares of numbers:", list_numbers_square)
