#test about ktinker

import tkinter as tk

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
		
		self.gamePot = tk.Label(self.master, text = "100")
		self.gamePot.grid(row = 1, column = 1)

		# Your card hand
		self.label2 = tk.Label(self.master,text = "Your card hand:")
		self.label2.grid(row = 2, column = 0)

		self.humanHand = tk.Label(self.master, 
			font = "Verdana 10 bold", text = "No Card Yet")
		self.humanHand.grid(row = 2, column = 1)

		#Computer's hand
		self.label3 = tk.Label(self.master,text = "Computer hand:")
		self.label3.grid(row = 3, column = 0)

		self.compHand = tk.Label(self.master, 
			font = "Verdana 10 bold", text = "No Card Yet")
		self.compHand.grid(row = 3, column = 1)

		#Game result
		self.label4 = tk.Label(self.master,text = "Game Result:")
		self.label4.grid(row = 4, column = 0)

		self.gameResult = tk.Label(self.master, 
			font = "Verdana 10 bold", fg = "red", text = "No Game Yet")
		self.gameResult.grid(row = 4, column = 1)

		#build play button
		self.bPlay = tk.Button(self.master) #bAdd is a button
		self.bPlay["text"] = "PlayGame"
		self.bPlay.grid(row = 5, columnspan = 2, sticky = 'E')
		#build quit button
		self.bQuit = tk.Button(self.master, text = "QUIT", fg = "blue",
			command = self.master.destroy) # close app
		self.bQuit.grid(column = 2, row = 5)

root = tk.Tk()
root.title("Card War Game Demo")
app = Application(master = root)
root.mainloop()