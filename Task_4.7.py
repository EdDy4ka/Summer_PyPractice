import itertools

list_length = int(input("Enter the length of the list of items: "))
list_numbers = []

for i in range(list_length):
    element = int(input("Come up with a list item: "))
    list_numbers.append(element)

print("List of numbers:", list_numbers)

permutations = list(itertools.permutations(list_numbers))
print("ALL permutations of a given list of numbers:")
for i in permutations:
    print(i)
