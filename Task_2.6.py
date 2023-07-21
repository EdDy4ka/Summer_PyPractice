number_kilometers = int(input("How many kilometers do you need to drive: "))
liters_kilometers = int(input("How many liters goes for 100 kilometers: "))
liters_tank = int(input("How many liters of fuel are in your tank: "))

overcoming_route = number_kilometers - (liters_kilometers * 100 + liters_tank)

if overcoming_route <= 0:
    print("The car will drive along the specified route!")
else:
    print("The car will not drive along the specified route!")
