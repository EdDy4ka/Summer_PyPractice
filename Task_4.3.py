start_number = int(input("Enter the number of the beginning of the range: "))
finish_number = int(input("Enter the number of the end of the range: "))
list_number = []

for i in range(start_number, finish_number + 1):
    const = 2
    while i % const != 0:
        const += 1
    if const == i:
        list_number.append(i)

print("List of prime numbers:", list_number)
