import random

count_loss, count_win = 0, 0
print("The game of the eagle! Heads - 0, tails - 1")
print("The game will end after three defeats!\n")

while count_loss != 3:
    coin_toss = random.randint(0, 1)
    print("The coin is tossed...")
    heads_tails = int(input("Try to guess: heads or tails (enter a number): "))
    if heads_tails == 1:
        print("You guessed right!\n")
        count_win += 1
    elif heads_tails == 0:
        print("You didn't guess!\n")
        count_loss += 1
    else:
        print("The game is suspended due to incorrect input...\n")
        break

print("Game Results: victories = ", count_win, " defeats = ", count_loss, sep="")
