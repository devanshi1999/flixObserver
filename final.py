#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

def gui(row,result):

	root = Tk()
	root.title(row[2])
	root.configure(background="paleturquoise1")
	root.minsize(1000,600)
	
#----------------------------------------------------------------------------------------------------------------------------------------------------------
	f1 = Frame(root,background="paleturquoise1")
	f1.pack()

	name = Label(f1,text=row[2],font=('Courier',30,'bold'),background="paleturquoise1",pady=10)
	name.pack()

	x = row[6]
	if x=='\N':
		x = row[5]
	else:
		x = row[5]+' - '+row[6]

	year = Label(f1,text=x,font=('Helvetica',25,'bold'),background="paleturquoise1",foreground="brown")
	year.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

	f2 = Frame(root,background="paleturquoise1")
	f2.pack()

	time = Label(f2,text="⌛"+ row[7] +" minutes",font=('Helvetica',20),background="paleturquoise1",foreground="Rosybrown4")
	time.pack(fill=X,padx=40,pady=15,side=LEFT)

	genre = Label(f2,text=row[8],font=('Helvetica',20),background="paleturquoise1",foreground="Rosybrown4")
	genre.pack(fill=X,padx=40,pady=15,side=LEFT)

	typ = Label(f2,text=row[1],font=('Helvetica',20),background="paleturquoise1",foreground="Rosybrown4")
	typ.pack(fill=X,padx=40,pady=15,side=LEFT)

	total = Label(f2,text="✎"+str(result[3])+" reviews",font=('Helvetica',20),background="paleturquoise1",foreground="Rosybrown4")
	total.pack(fill=X,padx=40,pady=15,side=LEFT)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

	f3 = Frame(root,background="paleturquoise1")
	f3.pack()

	if result[3]==0:
		x=0
		y=0
		z=0
	else:
		x=round(result[0]*100.0/result[3])
		y=round(result[1]*100.0/result[3])
		z=round(result[2]*100.0/result[3])

	posp = Label(f3,text="😍"+str(x).split('.')[0]+"% liked",font=('Helvetica',20),background="paleturquoise1",foreground="forest green")
	posp.pack(fill=X,padx=60,pady=15,side=LEFT)

	neup = Label(f3,text="😐"+str(y).split('.')[0]+"% were neutral",font=('Helvetica',20),background="paleturquoise1",foreground="gold4")
	neup.pack(fill=X,padx=60,pady=15,side=LEFT)

	negp = Label(f3,text="😒"+str(z).split('.')[0]+"% disliked",font=('Helvetica',20),background="paleturquoise1",foreground="indianred3")
	negp.pack(fill=X,padx=60,pady=15,side=LEFT)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

	f4 = Frame(root,background="paleturquoise1")
	f4.pack(side=LEFT)

	h1 = Label(f4,text="❤️Positive Responses❤️",font=('Helvetica',25,'bold'),background='paleturquoise1',foreground='purple3')
	h1.pack(fill=X,pady=3)

	pos=open("positive.txt", "r")
	i=0

	content=sorted(pos.readlines(), key=lambda item: int(item.split('⭐️ ')[0]), reverse=True)

	if(len(content)!=0):
		for line in content: 
			s = line.split('⭐️ ')[1]
			l1 = Label(f4,text='\n'.join(s[i:i+50] for i in range(0, len(s), 50)),font=('Helvetica',20),background='paleturquoise1',foreground='purple1')
			l1.pack(fill=X,pady=2)
			i+=1
			if i>=5 or i==len(content):
				break;
	else:
		l1 = Label(f4,text="(empty)",font=('Helvetica',20),background='paleturquoise1',foreground='purple1')
		l1.pack(fill=X,pady=2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

	f5 = Frame(root,background="paleturquoise1")
	f5.pack(side=LEFT)

	h2 = Label(f5,text="💛Neutral Responses",font=('Helvetica',25,'bold'),background='paleturquoise1',foreground='purple3')
	h2.pack(fill=X,pady=3)

	neu=open("neutral.txt", "r")
	i=0

	content=sorted(neu.readlines(), key=lambda item: int(item.split('⭐️ ')[0]))

	if(len(content)!=0):
		for line in content: 
			s = line.split('⭐️ ')[1]
			l1 = Label(f5,text='\n'.join(s[i:i+50] for i in range(0, len(s), 50)),font=('Helvetica',20),background='paleturquoise1',foreground='purple1')
			l1.pack(fill=X,pady=2)
			i+=1
			if i>=5 or i==len(content):
				break;
	else:
		l1 = Label(f5,text="(empty)",font=('Helvetica',20),background='paleturquoise1',foreground='purple1')
		l1.pack(fill=X,pady=2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

	f6 = Frame(root,background="paleturquoise1")
	f6.pack(side=LEFT)

	h3 = Label(f6,text="💔Negative Responses",font=('Helvetica',25,'bold'),background='paleturquoise1',foreground='purple3')
	h3.pack(fill=X,pady=3)

	neg=open("negative.txt", "r")
	i=0

	content=sorted(neg.readlines(), key=lambda item: int(item.split('⭐️ ')[0]))

	if(len(content)!=0):
		for line in content: 
			s = line.split('⭐️ ')[1]
			l1 = Label(f6,text='\n'.join(s[i:i+50] for i in range(0, len(s), 50)),font=('Helvetica',20),background='paleturquoise1',foreground='purple1')
			l1.pack(fill=X,pady=2)
			i+=1
			if i>=5 or i==len(content):
				break;
	else:
		l1 = Label(f6,text="(empty)",font=('Helvetica',20),background='paleturquoise1',foreground='purple1')
		l1.pack(fill=X,pady=2)

	pos.close()
	neg.close()
	neu.close()

	root.mainloop()
