from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import os
import time

root = Tk()
root.title('Notepad Project')

global open_name
open_name = False


def new_file():
    my_text.delete("1.0", END)
    root.title('New Fie - TextPad!')
    global open_name
    open_name = False


def open_file():
    my_text.delete("1.0", END)
    path = os.getcwd()
    text_file = filedialog.askopenfilename(initialdir = path, filetypes=[("Text Documents","*.txt"), ("HTML Files","*.html"), ("Python Files","*.py"),("All Files","*.*")])
    if text_file:
        global open_name
        open_name = text_file
    name = text_file
    name= name.replace(path,"")
    root.title(f'{name} - TextPad!')

    text_file = open(text_file,'r')
    stuff = text_file.read()
    my_text.insert(END,stuff)
    text_file.close()



def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension = ".txt", initialdir = os.getcwd(), title = "Save File", filetypes = [("Text Files", "*.txt"),("HTML Files","*.html"), ("Python Files","*.py"), ("All Files", "*.*")])
    if text_file:
        name = text_file
        name = name.replace(os.getcwd(),"")
        root.title(f'{name} -NotePad!')

        text_file = open(text_file,'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()


def save_file():
    global open_name
    if open_name:
        text_file = open(open_name,'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
    else:
        save_as_file()

def exit():
    root.destroy()

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


#Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

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


#Create Button
bold_button = Button(toolbar_frame, text = "Bold", command = bold_it)
bold_button.grid(row = 0, column = 0, sticky =W, padx=5)

italics_button = Button(toolbar_frame, text = "Italics", command = italics)
italics_button.grid(row = 0, column = 1, padx=5)

undo_button = Button(toolbar_frame, text = "Undo", command = my_text.edit_undo)
undo_button.grid(row = 0, column = 2, padx=5)

redo_button = Button(toolbar_frame, text = "Redo", command = my_text.edit_redo)
redo_button.grid(row = 0, column = 3, padx= 5)

root.mainloop()