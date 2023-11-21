#!/bin/python
# 1. poker.py
# Implement a class, PlayingCard, to represent a playing card. Your program will ask the user
# how many cards they would like to generate, and then generate that many random cards
# based on the user’s input. The program will print out each card in the format of “Rank of
# Suits”, e.g. “King of Hearts”, “5 of Diamonds”, “Ace of Clubs”, and etc. It will also print out
# the corresponding Blackjack value of each card generated.
# Your class should have the following methods:
#  __init__ (self, rank, suit)
# rank is an integer in the range 1 to 13 indicating the ranks Ace to King.
# suit is a single character &quot;D &quot; &quot;C &quot; &quot;H &quot; or &quot;S&quot; indicating the suit (Diamonds, Clubs,
# Hearts, or Spades);
#  get_rank(self) returns the rank of the card;
#  get_suit (self) returns the suit of the card;
#  get_value(self) returns the Blackjack value of a card.
# For example, Ace counts as 1, 2, counts as 2, and face cards count as 10.
#  __str__ (self) returns a string of the name of a card. For example, &quot;Ace of Spades&quot;.
# Note: The __str__ method is a special method in Python. If asked to convert an object
# into a string, Python uses this method, if it is present.
# For example, crad_one = Card(1,&quot;s&quot;), print(card_one) will print &#39;Ace of Spades&#39;.

import random

class PlayingCard:
    rank=0
    suit=""

    def __init__(self, rank, suit):
        if rank<1 or rank>13:
            raise Exception
        self.rank = rank
        self.suit = suit
    def get_rank(self):
        return self.rank
    def get_suit (self):
        if self.suit=='c':
            return "Clubs"
        elif self.suit=='h':
            return "Hearts"
        elif self.suit=='s':
            return "Spades"
        elif self.suit=='d':
            return "Diamonds"
        
        return "UNKNOWN SUIT"
    def get_value(self):
        if self.get_rank()>9:
            return 10
        return self.get_rank()
    def __str__ (self):
        ret=""
        if self.get_rank()==1:
            ret="Ace"
        elif self.get_rank()==11:
            ret="Jack"
        elif self.get_rank()==12:
            ret="Queen"
        elif self.get_rank()==13:
            ret="King"
        else:
            ret=str(self.get_rank())
        ret+=" of "+self.get_suit()
        return ret




deck=[]
for r in range(1,13):
    for s in ['c','h','d','s']:
        card=PlayingCard(r,s)
        deck.append(card)
#good card players know 7 shuffles are required for a deck to be 'random'
for r in range(7):
    random.shuffle(deck)

print("Deck is built and shuffled!")

howmany=input("How many cards would you like?(non number to exit)\nEnter Number:")
try:
    howmanyi=int(howmany)
except ValueError:
    exit(0)

if howmanyi<0 or howmanyi>52:
    print("invalid number")
    exit(0)

for x in range(howmanyi):
    card=deck.pop()
    print(card," Worth:",card.get_value())
