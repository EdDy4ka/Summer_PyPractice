line = str(input("Enter a word or sentence in English: "))
check_list = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'E', 'I', 'O', 'U', 'Y'}
dict_letter = {}

for i in range(len(line)):
    if line[i] != ' ':
        if line[i] in check_list:
            dict_letter[line[i]] = "True"
        else:
            dict_letter[line[i]] = "False"

print("Dictionary output:", dict_letter)
