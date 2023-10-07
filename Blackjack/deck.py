import random
from card import Card



class Deck:
    def __init__(self):
        self.deck = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        ranks = {
    "2", 
    "3", 
    "4", 
    "5", 
    "6",
    "7", 
    "8", 
    "9", 
    "10", 
    "J", 
    "Q", 
    "K", 
    "A", 
        }
      
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        top_card = self.deck.pop()
        return top_card
            
