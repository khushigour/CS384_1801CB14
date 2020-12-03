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

global selected
selected= False


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
    global selected
    #check if we use keyboard shortcut
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)



def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected= my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e):
    global selected
    if e:
        selected  = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


def find_text():
    def find():
        word = find_input.get()
        my_text.tag_remove("match", "1.0", END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos= my_text.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                my_text.tag_add("match", start_pos, end_pos)
                matches+=1
                start_pos = end_pos
                my_text.tag_config('match', foreground = 'red', background = 'yellow')

    find_popup = Toplevel()
    find_popup.geometry("450x100")
    find_popup.title("Find Word")
    find_popup.resizable(0,0)

    find_frame= Frame(find_popup)
    find_frame.pack(pady=20)

    text_find= Label(find_frame, text="Find")
    find_input = Entry(find_frame, width=30)
    find_button= Button(find_frame, text="find", command = find)
    text_find.grid(row=0, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    find_button.grid(row=1, column=0, padx=4, pady=4)


def find_and_rplace():
    def find():
        word = find_input.get()
        my_text.tag_remove("match", "1.0", END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos= my_text.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                my_text.tag_add("match", start_pos, end_pos)
                matches+=1
                start_pos = end_pos
                my_text.tag_config('match', foreground = 'red', background = 'yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = my_text.get(1.0, END)
        new_content = content.replace(word, replace_text)
        my_text.delete(1.0, END)
        my_text.insert(1.0,new_content)

    find_popup = Toplevel()
    find_popup.geometry("450x150")
    find_popup.title("Find and Replace Word")
    find_popup.resizable(0,0)

    find_frame= Frame(find_popup)
    find_frame.pack(pady=20)

    #Label
    text_find= Label(find_frame, text="Find")
    text_replace = Label(find_frame, text= "Replace")

    #entry box
    find_input = Entry(find_frame, width=30)
    replace_input = Entry(find_frame, width = 30)

    #button
    find_button= Button(find_frame, text="find", command = find)
    replace_button = Button(find_frame, text = "Replace", command = replace)

    #text label grid
    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    #entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    #button grid
    find_button.grid(row=2, column=0, padx=4, pady=4)
    replace_button.grid(row=2, column=1, padx =4, pady=4)


def wordcount_file():
    word = len(my_text.get(1.0,'end-1c').split())
    messagebox.showinfo('word count', 'Number of words: ' + str(word))


def charcount_file():
    char_value = len(my_text.get(1.0,END).replace("\n","").replace(" ",""))
    messagebox.showinfo('char count', 'Number of characters: ' + str(char_value))

def created_time_file():
    c_time = os.path.getctime(open_name) 
    local_time = time.ctime(c_time) 
    messagebox.showinfo('Created Time', "c-time (Local time):" + str(local_time))


def modified_time_file():
    m_time = os.path.getmtime(open_name) 
    local_time = time.ctime(m_time) 
    messagebox.showinfo('Modified Time', "m-time (Local time):" + str(local_time))

def bold_it():
    bold_font = font.Font(font = my_text["font"])
    if bold_font.actual()['weight'] == 'normal':
        my_text.configure(font=("Arial", 16, "bold"))
    if bold_font.actual()['weight'] == 'bold':
        my_text.configure(font=("Arial", 16, 'normal'))



def italics():
    it_font = font.Font(font = my_text["font"])
    if it_font.actual()['slant'] == 'roman':
        my_text.configure(font=("Arial", 16, "italic"))
    if it_font.actual()['slant'] == 'italic':
        my_text.configure(font=("Arial", 16, 'roman'))

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