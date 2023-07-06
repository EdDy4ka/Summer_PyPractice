points_football = int(input("How many points did the team get: "))
if points_football == 0:
    print("The team lost")
elif points_football == 1:
    print("The team earned a draw")
elif points_football == 3:
    print("The team won!")
else:
    print("Such a number of points cannot be scored")
