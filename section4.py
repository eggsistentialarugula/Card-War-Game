#test about ktinker

import tkinter as tk
from tkinter import Label
import random

balance = 100

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

class Application(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		self.create_widgets()

	def create_widgets(self):
		#description
		self.desc = tk.Label(self.master, text = 
			"This is a 2-card war game  between you and the computer")
		self.desc.grid(row = 0, column = 0)

		# game pot, start with 100
		self.label1 = tk.Label(self.master, text = "Your game pot:")
		self.label1.grid(row = 1, column = 0)
		
		self.mRes = tk.StringVar(value = "100")
		self.gamePot = tk.Label(self.master, textvariable = self.mRes)
		self.gamePot.grid(row = 1, column = 1)

		# Your card hand
		self.label2 = tk.Label(self.master,text = "Your card hand:")
		self.label2.grid(row = 2, column = 0)

		self.hhRes = tk.StringVar(value = "No Card Yet")
		self.humanHand = tk.Label(self.master, 
			font = "Verdana 10 bold", textvariable = self.hhRes)
		self.humanHand.grid(row = 2, column = 1)

		#Computer's hand
		self.label3 = tk.Label(self.master,text = "Computer hand:")
		self.label3.grid(row = 3, column = 0)

		self.chRes = tk.StringVar(value = "No Card Yet")
		self.compHand = tk.Label(self.master, 
			font = "Verdana 10 bold", textvariable = self.chRes)
		self.compHand.grid(row = 3, column = 1)

		#Game result
		self.label4 = tk.Label(self.master,text = "Game Result:")
		self.label4.grid(row = 4, column = 0)

		self.gRes = tk.StringVar(value = "No Game Yet")
		self.gameResult = tk.Label(self.master, 
			font = "Verdana 10 bold", fg = "red", textvariable = self.gRes)
		self.gameResult.grid(row = 4, column = 1)

		#build play button
		self.bPlay = tk.Button(self.master) #bAdd is a button
		self.bPlay["text"] = "PlayGame"
		self.bPlay.grid(row = 5, columnspan = 2, sticky = 'E')
		#execute playGame method
		self.bPlay["command"] = self.playGame #execute playGame method
		#build quit button
		self.bQuit = tk.Button(self.master, text = "QUIT", fg = "blue",
			command = self.master.destroy) # close app
		self.bQuit.grid(column = 2, row = 5)

	def playGame(self):
		ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		play = 'y'
		global balance
		aDeck = Deck()
		#shuffle the deck
		aDeck.shuffle()

		#deal a card to the player
		playerCard1 = aDeck.deal()
		playerCard2 = aDeck.deal()
		#using printCard doesn't make the output show up in GUI, 
		#it only shows in console, so I didn't use printCard().
		pC1R = playerCard1.showRank() + ' of '
		pC1S = playerCard1.showSuit()

		pC2R = playerCard2.showRank() + ' of '
		pC2S = playerCard2.showSuit()
		#put result in hhRes
		self.hhRes.set(pC1R + pC1S + ' and ' + pC2R + pC2S)
		#deal a card to the computer
		compCard1 = aDeck.deal()
		compCard2 = aDeck.deal()

		cC1R = compCard1.showRank() + ' of '
		cC1S = compCard1.showSuit()

		cC2R = compCard2.showRank() + ' of '
		cC2S = compCard2.showSuit()
		#put result in chRes
		self.chRes.set(cC1R + cC1S + ' and ' + cC2R + cC2S)

		playerCard1Rank = ranks.index(playerCard1.showRank()) + 1
		playerCard2Rank = ranks.index(playerCard2.showRank()) + 1
		playerPTS = playerCard1Rank + playerCard2Rank #player points
		# self.gRes.set(str(playerPTS))

		compCard1Rank = ranks.index(compCard1.showRank()) + 1
		compCard2Rank = ranks.index(compCard2.showRank()) + 1
		compPTS = compCard1Rank + compCard2Rank #computer points

		if(playerPTS > compPTS):
			self.gRes.set("Player won!!!")
			r = 1
		elif(playerPTS == compPTS):
			self.gRes.set("Tie!!!")
			r = 0
		else:
			self.gRes.set("Computer won!!!")
			r = -1

		balance = balance + r * 10

		if(balance < 0):
			quit()

		self.mRes.set(str(balance))



# we shuffle the deck
# aDeck.shuffle()

# card1 = aDeck.deal()
# card1.printCard()

# card2 = aDeck.deal()
# card2.printCard()

root = tk.Tk()
root.title("Card War Game Demo")
app = Application(master = root)
root.mainloop()