import random

# the shuffle module shuffles the list in question, in place
# shuffle the cards and then use a for loop to print each card
cards = ["queen", "king", "heart"]
random.shuffle(cards)
for card in cards:
    print(card)
