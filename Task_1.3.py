first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
third_number = input("Enter the third number: ")

print("The largest number:", max([first_number, second_number, third_number]))

if first_number < second_number:
    first_number, second_number = second_number, first_number
if second_number < third_number:
    second_number, third_number = third_number, second_number
if first_number < second_number:
    first_number, second_number = second_number, first_number

print(first_number, second_number, third_number)
