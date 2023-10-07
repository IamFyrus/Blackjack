
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def hit(self, card):
        self.cards.append(card)


        self.value += card.getValue()
        if card.rank == "A":
            self.aces+=1

        self.if_ace()
        
        return card.__str__()


    def if_ace(self):
        if self.value > 21 and self.aces >= 1:
            self.value -= 10*self.aces
            self.aces =0


    def check_bj(self):
        if self.value == 21:
            return 2
        else:
            return 1

        