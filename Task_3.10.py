line = str(input("Enter a word or sentence in English: "))
dict_letters = {}

for i in range(len(line)):
    if line[i] != ' ':
        if line[i] not in dict_letters:
            dict_letters[line[i]] = 1
        else:
            dict_letters[line[i]] += 1

print("Dictionary output:", dict_letters)
