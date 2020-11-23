'''

Program to play a card game

'''
from random import  random
class Deck(object):
    def __init__(self):
        self.deck = []
        self.dealt = [] #Prevents from dealing the same card

    def PopulateDeck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank in range(2, 15):
                if rank == 11:
                    value = "Jack"
                elif rank == 12:
                    value = "Queen"
                elif rank == 13:
                    value = "King"
                elif rank == 14:
                    value = "Ace"
                else:
                    value = str(rank)

                self.deck.append(Card(value, suit))

    def deal(self):
        #Randomly select card
        remaining_cards = [card for card in self.deck if card not in self.dealt]
        card_index = random.randrange(0, len(remaining_cards)-1)
        card = remaining_cards[card_index]
        self.dealt.append(card)
        return card



    def shuffle(self):
        self.dealt = []

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.card = str(self.rank) + " " + str(self.suit)
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

def play():
    deck = Deck()
    card1 = deck.deal()
    card2 = deck.deal()
    card3 = deck.deal()

#And here you will compare the cards to see if the player wins or not. Not sure 
#what exact criterion you're using.

deck.shuffle() #And leave your deck nicely shuffled for next game

# play()