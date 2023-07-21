natural_number = input("Enter a natural number with different digits: ")
list_natural_number = list(natural_number)
max_number = max(list_natural_number)

for i in range(len(list_natural_number)):
    if list_natural_number[i] == max_number:
        print(i + 1)

for i in range(len(list_natural_number) - 1, -1, -1):
    if list_natural_number[i] == max_number:
        print(i + 1)
