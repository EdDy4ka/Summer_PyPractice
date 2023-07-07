len_fib = int(input("Enter the length of the Fibonacci series: "))
fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
list_fib = list(map(fib, range(0, len_fib)))
print("List of Fibonacci numbers up to a given number:", list_fib)
