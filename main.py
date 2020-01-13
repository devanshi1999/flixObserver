#!/usr/bin/python
# -*- coding: utf-8 -*-
from  Tkinter import *
import titleSearch
import scraper
import tkMessageBox
import final

class GUI:
	def __init__(self,master):

		master.title("Flix Observer")
		master.configure(background='black')
		master.minsize(700, 600)
		master.maxsize(700, 600)

		self.l1 = Label(master, text="Enter movie title: ", font = ('MS Serif',30), padx=20, pady=50)
		self.title = Entry(master, bd =5, highlightbackground='black', justify=CENTER, font = ('Courier', 20), width = 25)
		self.l2 = Label(master, text="Enter release year: ", font = ('MS Serif',30),padx=20, pady=50)
		self.year = Entry(master, bd =5, highlightbackground='black', justify=CENTER, font = ('Courier', 20), width = 10)
		self.submit = Button(master, text ="🔎 check'a flix!",command=self.get_details, highlightbackground='black', justify=CENTER, font = ('Courier', 15))
		
		self.l1.configure(background='black', foreground='grey')
		self.l2.configure(background='black', foreground='grey')
		self.submit.configure(relief=RAISED, pady=4,width = 25, height=5 )
		
		self.l1.grid(row=0,sticky=E)
		self.title.grid(row=0,column=1,ipady=5)
		self.l2.grid(row=1,sticky=E)
		self.year.grid(row=1,column=1,ipady=5,sticky=W)
		self.submit.grid(row=2,columnspan=4)

		self.photo = PhotoImage(file="bg1.gif")
		self.l3 = Label(master, image=self.photo)
		self.l3.grid(row=10,columnspan=10)
		self.l3.configure(background='black')

	def get_details(self):
		title = self.title.get()
		year = self.year.get()
		year = int(year)
		year = str(year)
		if title and year:
			if int(year)<=0:
				tkMessageBox.showinfo('oops!', 'Give a valid year!')
			else:
				row = titleSearch.search(title,year)
				if row==None:
					tkMessageBox.showinfo('oops!', 'Invalid title/year combination.')
				else:
					url = "https://www.imdb.com/title/"+row[0]+"/reviews"
					result = scraper.scrape(url)
					final.gui(row,result)
		else:
			tkMessageBox.showinfo('oops!', 'You need to fill both the fields!')
				

window = Tk()

gui = GUI(window)

window.mainloop()


