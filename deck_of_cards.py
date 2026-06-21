import random

#displays heading
def heading():
     print("WELCOME TO THE CARD DEALER")
     print("\nI have shuffled a deck of 52 cards.")

#creates class
class Deck:
    def __init__(self):
        self.card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        self.cards = []
        

        for s in self.suits:
            for v in self.card_values:
                self.cards.append(f"{v} of {s}")

    #creates method to shuffle cards
    def shuffle(self):
        random.shuffle(self.cards)


    #creates method to deal cards
    def deal(self, num_cards):
        
        dealt_cards = []
        
        for i in range(num_cards):
            card = self.cards.pop()
            dealt_cards.append(card)
        return dealt_cards    
    

    #creates method to count remaining cards 
    def count_cards(self):
        return len(self.cards)
        
#main function, calls all methods from the class and drives the program   
def main():
    heading()

    deck = Deck()   
    deck.shuffle()
    

    num_cards = int(input("\nHow many cards would you like?: "))
    
    hand = deck.deal(num_cards)

    print("\nHere are your cards:")
    for card in hand:
        print(card)

    cardsLeft = deck.count_cards()
    print(f"\nThere are {cardsLeft} cards left in the deck.")
    print("\nGood Luck!")

    
if __name__ == "__main__":
    main()


     
