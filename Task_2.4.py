a = int(input("Enter a number 'a': "))
b = int(input("Enter a number 'b': "))
c = int(input("Enter a number 'c': "))
D = b**2 - 4*a*c
print("The discriminant is equal to:", D)
if D < 0:
    print("The equation has no roots")
elif D == 0:
    print("The equation has one root: x = ", -b / (2*a))
else:
    print("The equation has two roots: x(1) = ", (-b + D**0.5) / (2 * a), ", x(2) = ", (-b - D**0.5) / (2 * a), sep="")
