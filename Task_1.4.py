rand_number = int(input("Enter a number from 10 to 20: "))
while (rand_number < 10) or (rand_number > 20):
    if rand_number < 10:
        print("Число меньше требуемого диапазона")
    if rand_number > 20:
        print("Число больше требуемого диапазона")
    rand_number = int(input("Try entering the number again: "))
print("Спасибо")
