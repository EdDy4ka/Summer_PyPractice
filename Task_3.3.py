number = int(input("Enter any natural integer: "))
result_number = lambda x: f"The number {x} is even" if x % 2 == 0 else f"The number {x} is odd"
print(result_number(number))
