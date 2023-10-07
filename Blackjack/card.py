#card.py

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getValue(self):
        match self.rank:
            case "2" : 
                return 2
            case "3" : 
                return 3
            case "4" :
                return 4
            case "5" :
                return 5
            case "6" :
                return 6
            case "7" : 
                return 7
            case "8" : 
                return 8
            case "9" : 
                return 9
            case "10" : 
                return 10
            case "J" : 
                return 10
            case "Q" : 
                return 10
            case "K" : 
                return 10
            case "A" : 
                return 11
            case _ : 
                return 0
             

    def __str__(self):
        return f"{self.rank} of {self.suit}"
        


