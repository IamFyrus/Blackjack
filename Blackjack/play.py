from hand import Hand
from deck import Deck



        




 

class Play:
    def play(self):
        wins = 0
        losses = 0
        games_played = 0
        cont = True

        print("\n---------------------------------------------------------------------------------\n")
        print("\n                           Welcome to Blackjack!                                 \n")
        print("\n---------------------------------------------------------------------------------\n")

        while(cont):
            games_played+=1
            deck = Deck()
            deck.shuffle()

            player = Hand()
            dealer = Hand()

            print("\nPlayer is dealt: ")            
            print(player.hit(deck.deal()))
            dealer.hit(deck.deal())
            print("\nPlayer is dealt: ")
            print(player.hit(deck.deal()))
            print("\nDealer is dealt: ")
            print(dealer.hit(deck.deal()))

            print("\nPlayer's hand: ", player.cards[0], player.cards[1])
            print("\nPlayer's hand   value: ", player.value)
            if player.check_bj() == 2:
                if self.check_win(player, dealer) == 1:
                    wins +=1
                
            else:
                print("\nDealer's hand: ", dealer.cards[1], " *hidden card*\n")

                self.make_choice(deck, player)
                if player.value > 21:
                    self.bust(player)
                    losses += 1
                else:
                    if(dealer.value >= 17):
                        result = self.check_win(player, dealer)
                        if result == 1:
                            wins +=1
                        elif result == 2:
                            losses += 1
                    else:
                        print("\nPlayer value = ", player.value)
                        print("\nDealer's hand: ", dealer.cards[0], dealer.cards[1])
                        while(dealer.value < 17):
                            print("\nDealer value = ", dealer.value)
                            print("\nDealer is dealt: ")
                            print(dealer.hit(deck.deal()))
   
                        result = self.check_win(player, dealer)
                        if result == 1:
                            wins +=1
                        elif result == 2:
                            losses += 1

            print("\n Total Wins: ", wins)
            print("\n Total Losses: ", losses)
            print("\n Total Games Played: ", games_played)
            good = True
            while good:
                again = input("\nPlay Again? (Enter Y/N): ")
                if again.upper() == "N":
                    cont = False
                    good = False
                elif again.upper() == "Y":
                    cont = True
                    good = False
                else:
                    good = True
                    print("\nPlease input either Y for Yes or N for No.")
    
    
    def make_choice(self, deck, hand):
        valid = True
        while(valid):
            choice = input("\nWould you like to hit or stand? (Enter H to hit, S to stand): ")
            if choice.upper() == "H":
                print("\nPlayer is dealt: ") 
                print(hand.hit(deck.deal()))
                if hand.value >= 21:
                    valid = False
                else:
                    print("\nPlayer value = ", hand.value)
            elif choice.upper() == "S":
                valid = False
            else:
                print("\nPlease input either H for Hit or S for Stand.")

        



    def check_win(self, player, dealer):
        print("\nPlayer value = ", player.value)
        print("\nDealer value = ", dealer.value)
        if player.value > dealer.value:
            print("\nPlayer wins!!!")
            return 1
        elif player.value == dealer.value:  
            print("\nThey are equal! It's a push!") 
            return 3
        elif dealer.value > 21:
            print("\nDealer Busted! Player Wins!")
            return 1
        else:
            print("Oh No! Dealer Wins!")
            return 2

    def bust(self, player):
        print("\n Player value: ", player.value)
        print("\n You Busted! Unlucky!")

        


            
                    

  









