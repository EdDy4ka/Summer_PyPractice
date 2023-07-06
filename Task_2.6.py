number_kilometers = int(input("How many kilometers do you want to drive by car: "))
liters_kilometers = int(input("How many liters of fuel does a car consume per 100 kilometers: "))
liters_tank = int(input("How many liters of fuel are in your tank: "))

overcoming_route = number_kilometers - (liters_kilometers*100 + liters_tank)
if overcoming_route <= 0:
    print("The car will drive along the specified route!")
else:
    print("The car will not drive along the specified route!")
