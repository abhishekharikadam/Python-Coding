# Program to shuffle deck of cards

import random, itertools

deck = list(itertools.product (range (1, 14), ["Spade", "Club", "heart", "Diamond"]))

# print(deck)

random.shuffle(deck)

print(deck)

num = int(input("Enter the number:- "))

for i in range(num):
    print(deck[i][0], 'is', deck[i][1])