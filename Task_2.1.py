import random

lst_colors = ['green', 'yellow', 'red', 'black', 'white']
random_color = random.choice(lst_colors)

print("Color list: green, yellow, red, black, white")
color_selection = str(input("Guess the name of one of the listed colors: "))

while color_selection != random_color:
    if random_color == 'green':
        print("Hint: You can lie down on the grass and enjoy this day!")
        color_selection = str(input("After receiving a hint, try to guess again: "))
    elif random_color == 'yellow':
        print("Hint: In summer, the sun shines brightly in the sky!")
        color_selection = str(input("After receiving a hint, try to guess again: "))
    elif random_color == 'red':
        print("Hint: You can make a wish and blow on a ladybug!")
        color_selection = str(input("After receiving a hint, try to guess again: "))
    elif random_color == 'black':
        print("Hint: The cat ran across the road in front of you!")
        color_selection = str(input("After receiving a hint, try to guess again: "))
    elif random_color == 'white':
        print("Hint: Fluffy clouds float across the sky!")
        color_selection = str(input("After receiving a hint, try to guess again: "))
    else:
        color_selection = str(input("There is no such color, so try again: "))

print("Well done, the correct answer is", random_color)
