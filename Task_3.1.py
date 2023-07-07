from functools import reduce
from random import randint

len_list = int(input("Enter the length of the list: "))
list_number = []

for i in range(0, len_list):
    list_number.append(randint(0, 10))

print("List of elements:", list_number)
average_value = float(reduce(lambda x, y: x + y, list_number) / len_list)
print("The average value of the list numbers:", round(average_value, 2))
