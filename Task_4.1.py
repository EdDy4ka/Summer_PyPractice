number = ''.join(str(input("Enter a number: ")))
len_number = len(number)
list_number = []
list_max_number = []

for i in range(len_number):
    list_number.append(number[i])

for i in range(len_number):
    list_max_number.append(max(list_number))
    list_number.remove(list_max_number[i])

print("All combinations of numbers:", ''.join(list_max_number))
