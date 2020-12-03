from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import os
import time

root = Tk()
root.title('Notepad Project')

def new_file():
	pass

def open_file():
	pass

def save_as_file():
	pass

def save_file():
	pass

def exit():
	pass

def cut_text(e):
	pass

def copy_text(e):
	pass

def paste_text(e):
	pass

def find_text():
	pass

def find_and_rplace():
	pass

def wordcount_file():
	pass

def charcount_file():
	pass

def created_time_file():
	pass

def modified_time_file():
	pass

def bold_it():
	pass


def italics():
	pass

#create the frame
my_frame = Frame(root)
my_frame.pack(pady=10)


#Creat our Scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)


#Create Text Box
my_text = Text(my_frame,font=("Arial", 16), selectbackground="yellow",selectforeground = "black", undo= True, yscrollcommand = text_scroll.set)
my_text.focus_set()
my_text.pack()

#Configure our scrollbar
text_scroll.config(command = my_text.yview)


my_menu= Menu(root)
root.config(menu= my_menu)

file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label="New", command = new_file)
file_menu.add_command(label="Open",command = open_file)
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="Save As", command= save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = exit)

edit_menu= Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut    Ctrl+X",command = lambda : cut_text(False))
edit_menu.add_command(label="Copy   Ctrl+C",command = lambda : copy_text(False))
edit_menu.add_command(label="Paste  Ctrl+V",command = lambda : paste_text(False))
edit_menu.add_command(label="Find", command= find_text)
edit_menu.add_command(label="Find and Replace", command= find_and_rplace)

stats_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Stats", menu=stats_menu)
stats_menu.add_command(label="Word Count", command = wordcount_file)
stats_menu.add_command(label="Char Count", command = charcount_file)
stats_menu.add_command(label="Created Time",command = created_time_file)
stats_menu.add_command(label="Modified Time", command = modified_time_file)

root.mainloop()