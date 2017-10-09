#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

             ██╗  ████████╗███████╗
             ██║  ╚══██╔══╝██╔════╝
             ██║     ██║   █████╗
             ██║     ██║   ██╔══╝
             ███████╗██║   ███████╗
             ╚══════╝╚═╝   ╚══════╝
 +-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+
 |L|i|g|h|t|w|e|i|g|h|t| |T|e|x|t| |E|d|i|t|o|r|
 +-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+


* @name        LTE
* @copyright   Stefano Peris (c) 2017
* @author      Stefano Peris
* @email       lordstephen77@gmail.com
* @github      https://github.com/LordStephen77/LTE
* @license     GPL-3.0 (https://www.gnu.org/licenses/gpl-3.0.en.html)
* @create      dom 08 ott 2017 17:04:24 CEST
* @update      lun 09 ott 2017 11:44:08 CEST

"""

from tkinter import *
from tkinter import Tk, scrolledtext, Menu, filedialog, messagebox

import os, sys, time, datetime, webbrowser, fileinput

from src.menufunc import *
#from src.about import *

# Funzione che restituisce una stringa per i widget non ancora abilitati
def noFunc():
    print("Non succede nulla... per adesso...")

def startFile():
    os.startfile('res/start.txt')

# Root to main window
root = Tk()

root.title("LTE (Lightweight Text Editor)") # imposta il titolo della finestra
root.geometry("640x480") # imposta la risoluzione della finestra
root.resizable(width = True, height = True) # Finestra scalabile (altezza, larghezza)

# Statusbar
statusbar = Label(root, text ="Al momento non fa nulla...", bd = 1, relief = SUNKEN, anchor = W)
statusbar.pack(side = BOTTOM, fill = X)

# Text area editor
textArea = scrolledtext.ScrolledText(root, width = 640, height = 480, font =
("", 14), highlightthickness = 0, bd = 2)
textArea.pack()

# Menubar functions
def new():
    pass
        
def openFile():
    file = filedialog.askopenfile(parent = root, mode = 'rb', title = "Select a text file...")
    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()
                
def saveFile():
    file = filedialog.asksaveasfile(mode = 'w')
    if file != None:
        # Slice off the last character from get, as an extra return (enter) is added
        data = textArea.get('1.0', END + '-1c')
        file.write(data)
        file.close()
        
def copy(self, event=None):
    pass
        
def paste():
    try:
        teext = textArea.selection_get(selection='CLIPBOARD')
        textArea.insert(INSERT, teext)
    except:
        tkMessageBox.showerror("Errore","Gli appunti sono vuoti!")
        
def delete():
    sel = textArea.get(SEL_FIRST, SEL_LAST)
    textArea.delete(SEL_FIRST, SEL_LAST)
        
def selectAll():
    pass
        
def rename():
    pass
    
def line():
    lin = "-" * 60
    textArea.insert(INSERT,lin)

def date():
    # %p = Locale’s equivalent of either AM or PM.
    # %b = Locale’s abbreviated month name.
    # %Z = Time zone name (no characters if no time zone exists).
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")
    textArea.insert(INSERT, data)
        
def about():
    label = messagebox.showinfo("About", "LTE (Lightweight Text Editor\nRealizzato da Stefano Peris (C) 2017\n https://github.com/LordStephen77/LTE\nIl programma è rilasciato sotto licenza GPL")

def web():
    webbrowser.open('https://github.com/LordStephen77/LTE')
            
def exit():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Menu options
menu = Menu(root)
root.config(menu = menu)

fileMenu = Menu(root)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New")
fileMenu.add_command(label = "Open", command = openFile)
fileMenu.add_command(label = "Save", command = saveFile)
fileMenu.add_separator()
fileMenu.add_command(label = "Print")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exit)

editMenu = Menu(root)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Cut")
editMenu.add_command(label = "Copy", command = copy)
editMenu.add_command(label = "Paste", command = paste)
editMenu.add_separator()
editMenu.add_command(label = "Delete")
editMenu.add_command(label = "Rename")
editMenu.add_command(label = "Select All", command = selectAll)
editMenu.add_separator()
editMenu.add_command(label = "Line", command = line)
editMenu.add_command(label = "Date", command = date)

helpMenu = Menu(root)
menu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label = "Github", command = web)
helpMenu.add_command(label = "About", command = about)

# Keep window open
root.mainloop()

#####################################################################

