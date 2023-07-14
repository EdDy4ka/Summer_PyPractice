initial_word = str(input("Write a simple word or sentence without CAPS: "))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
secret_message = ''
ROT13 = 13

for letter in initial_word:
    new_letter = alphabet[(alphabet.find(letter) + ROT13) % 26]
    secret_message += new_letter

print("Secret message:", secret_message)
