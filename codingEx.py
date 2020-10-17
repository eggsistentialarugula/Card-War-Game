import random

class Card: 
    #__init__ is a function that runs when an object is created
    # we will store a number between 0 to 51 to represent a card
    def __init__(self, value=0):
        self.val = value
        # 'â™¥â™¦â™£â™ '[suit-1]
    # this method shows the suit of the card
    def showSuit(self):
        suit_symbols = ['♠', '♦', '♥', '♣']
        return suit_symbols[self.val % 4]
        
    # the method shows the rank of the card
    def showRank(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return ranks[self.val % 13]
    # this method print card in form of King of Spade
    def printCard(self):
        outS = self.showRank() + ' of '
        
        print(outS + '{}'.format(self.showSuit()) )
        
class Deck: 
    #- init will create 52 cards for each deck object
    def __init__(self):
        self.deck = []
        i =0
        self.top = 52 # top points to top of the deck
        while (i<52):
            self.deck.append(Card(i))
            i+=1
    #- this method randomize the cards using random
    def shuffle(self):
        random.shuffle(self.deck)
    #- this method deal 1 card to player
    def deal(self):
        if self.top >=1:
            self.top -=1
        return self.deck[self.top]
    
aDeck = Deck()
# we shuffle the deck
aDeck.shuffle()

card1 = aDeck.deal()
card1.printCard()

card2 = aDeck.deal()
card2.printCard()