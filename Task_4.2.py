sentence = "".join(str(input("Just enter a sentence or a word: ")).split())
palindrome_list = []
help_list = []
palindrome_length = 1

while palindrome_length != len(sentence) + 1:
    for i in range(0, len(sentence) - palindrome_length + 1):
        for j in range(i, i + palindrome_length):
            help_list.append(sentence[j])
        if "".join(help_list) == "".join(list(reversed(help_list))):
            if "".join(help_list) not in palindrome_list:
                palindrome_list.append("".join(help_list))
        help_list = []
    palindrome_length += 1

print("The list of palindromes is as follows:", palindrome_list)
