negative_numbers = -1
summa_number = 0

while negative_numbers < 0:
    negative_numbers = int(input("Enter a negative number: "))

    if negative_numbers < 0:
        summa_number += negative_numbers
        print("Sum of negative numbers = ", summa_number, "\n")
    else:
        print("Error due to entering a non-negative number!")
        break
