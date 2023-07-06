start_number = int(input("Enter the beginning of the interval 'a': "))
finish_number = int(input("Enter the end of the interval 'b': "))
summa_number = 0

while finish_number <= start_number:
    print("The final number 'b' must be greater than the number 'a'")
    finish_number = int(input("Enter the number 'b' again:"))

for i in range(start_number, finish_number+1):
    summa_number += i

print("The sum of the series is equal to: ", summa_number)
