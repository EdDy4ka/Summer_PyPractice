armstrong_number = input("Enter a number to check if it is an Armstrong number: ")
list_number = list(armstrong_number)
summa_number = 0
for i in range(len(list_number)):
    summa_number += int(list_number[i])**len(list_number)
if int(armstrong_number) == int(summa_number):
    print("This number is an Armstrong number")
else:
    print("This number is not an Armstrong number")
