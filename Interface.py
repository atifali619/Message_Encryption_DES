# import tkinter module 
from tkinter import *
import pydes

# import other necessery modules 
import random 
import time 
import datetime 

# creating root object 
root = Tk() 

# defining size of window 
root.geometry("1200x6000") 

# setting up the title of window 
root.title("Message Encryption and Decryption") 

Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 

f1 = Frame(root, width = 800, height = 700, 
							relief = SUNKEN) 
f1.pack(side = LEFT) 

# ============================================== 
#				 TIME 
# ============================================== 
localtime = time.asctime(time.localtime(time.time())) 

lblInfo = Label(Tops, font = ('brixtonln-regular', 50, 'bold'),
		text = "Message Encryptor & Decryptor \n DES",
					fg = "Black", bd = 10, anchor='w') 
					
lblInfo.grid(row = 0, column = 0) 

lblInfo = Label(Tops, font=('digital-7', 20, 'bold'),
			text = localtime, fg = "Blue",
						bd = 10, anchor = 'w') 
						
lblInfo.grid(row = 1, column = 0) 

rand = StringVar() 
Msg = StringVar() 
key = StringVar() 
mode = StringVar()
Result = StringVar()
Dec = StringVar()

# exit function 
def qExit(): 
	root.destroy() 

# Function to reset the window 
def Reset(): 
	rand.set("") 
	Msg.set("") 
	key.set("")
	mode.set("")
	Result.set("")
	Dec.set("")


# reference 
lblReference = Label(f1, font = ('Intro Rust G Base 2 Line', 16, 'bold'),
				text = "Sender's Name", bd = 16, anchor = "w")
				
lblReference.grid(row = 0, column = 0) 

txtReference = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = rand, bd = 10, insertwidth = 4, 
						bg = "powder blue", justify = 'right') 
						
txtReference.grid(row = 0, column = 1) 

# labels 
lblMsg = Label(f1, font = ('Intro Rust G Base 2 Line', 16, 'bold'),
		text = "MESSAGE", bd = 16, anchor = "w") 
		
lblMsg.grid(row = 1, column = 0) 

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = Msg, bd = 10, insertwidth = 4, 
				bg = "powder blue", justify = 'right') 
				
txtMsg.grid(row = 1, column = 1) 

lblkey = Label(f1, font = ('Intro Rust G Base 2 Line', 16, 'bold'),
			text = "KEY", bd = 16, anchor = "w") 
			
lblkey.grid(row = 2, column = 0) 

txtkey = Entry(f1, font = ('arial', 16, 'bold'), 
		textvariable = key, bd = 10, insertwidth = 4, 
				bg = "powder blue", justify = 'right') 
				
txtkey.grid(row = 2, column = 1) 

lblmode = Label(f1, font = ('Intro Rust G Base 2 Line', 16, 'bold'),
		text = "Recipent's Name",bd = 16, anchor = "w")

lblmode.grid(row = 3, column = 0)

txtmode = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = mode, bd = 10, insertwidth = 4,
				bg = "powder blue", justify = 'right')

txtmode.grid(row = 3, column = 1)

lblService = Label(f1, font = ('Intro Rust G Base 2 Line', 16, 'bold'),
			text = "Encrypted Text", bd = 16, anchor = "w")
decSerLabel = Label(f1, font = ('Intro Rust G Base 2 Line', 16, 'bold'),
			text = "Decrypted Text", bd = 16, anchor = "w") 
			
lblService.grid(row = 1, column = 2)
decSerLabel.grid(row = 2, column = 2)

txtService = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = Result, bd = 10, insertwidth = 2, 
					bg = "powder blue", justify = 'right') 
						


decService = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = Dec, bd = 10, insertwidth = 4, 
					bg = "powder blue", justify = 'right')

txtService.grid(row = 1, column = 3)
decService.grid(row=2, column = 3)

import base64 


# Function to encode 
def encode(key, clear): 
	return pydes.encrypt(key, clear)

# Function to decode 
def decode(key, enc): 
	return pydes.decrypt(key, enc)


def Ref(): 
	print("Message= ", (Msg.get())) 

	clear = Msg.get() 
	k = key.get() 
	m = mode.get()
	x = encode(k, clear)
	d = decode(k, x)
	Result.set(x)
	Dec.set(d)

# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
						font = ('Intro Rust G Base 2 Line', 16, 'bold'), width = 10,
					text = "Show Message", bg = "#9acd32",
						command = Ref).grid(row = 7, column = 1) 

# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('Intro Rust G Base 2 Line', 16, 'bold'),
					width = 10, text = "Reset", bg = "#fda50f",
				command = Reset).grid(row = 7, column = 2) 

# Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('Intro Rust G Base 2 Line', 16, 'bold'),
					width = 10, text = "Exit", bg = "red", 
				command = qExit).grid(row = 7, column = 3) 

# keeps window alive 
root.mainloop()
