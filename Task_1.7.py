sentence = str(input("Enter a sentence: "))
sentence = list(sentence)
for i in range(len(sentence)):
    if (sentence[i] >= 'a') and (sentence[i] <= 'z'):
        sentence[i] = chr(ord(sentence[i]) - 32)
    elif (sentence[i] >= 'A') and (sentence[i] <= 'Z'):
        sentence[i] = chr(ord(sentence[i]) + 32)
print("Your sentence:", "".join(sentence))
