import itertools

list_length = int(input("Enter the length of the list of items: "))
list_numbers = []

for i in range(list_length):
    element = int(input("Come up with a list item: "))
    list_numbers.append(element)

print("List of numbers:", list_numbers)

target = int(input("Enter the sum for the number combinations: "))
list_final = []

for i in range(len(list_numbers), 1, -1):
    for j in itertools.combinations(list_numbers, i):
        if sum(j) == target:
            list_final.append(j)

for i in range(len(list_numbers)):
    if list_numbers[i] == target:
        list_final.append(list_numbers[i])

print("List of number combinations:", list_final)
