list_showing = ['Improvisation', 'Field of Miracles', 'Fort Boyard', 'Voice']
print('\n'.join(list_showing))
TV_hobby = str(input("Enter a new gear to your taste: "))
list_position = int(input("Enter the position (from 1 to 5) of the program in the list: "))
list_position -= 1
while list_position < 0 or list_position > 4:
    list_position = int(input("Enter the line number in the gap of the list: "))
list_showing[list_position:list_position] = [TV_hobby]
print('\n'.join(list_showing))
