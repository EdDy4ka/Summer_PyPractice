the_first_number = input("Enter the first number: ")
the_second_number = input("Enter the second number: ")
the_third_number = input("Enter the third number: ")

print("The largest number:", max([the_first_number, the_second_number, the_third_number]))

if the_first_number < the_second_number:
    the_first_number, the_second_number = the_second_number, the_first_number
if the_second_number < the_third_number:
    the_second_number, the_third_number = the_third_number, the_second_number
if the_first_number < the_second_number:
    the_first_number, the_second_number = the_second_number, the_first_number
print(the_first_number, the_second_number, the_third_number)
