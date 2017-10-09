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

import os, sys, time, datetime, webbrowser

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

# Text area editor
textArea = scrolledtext.ScrolledText(root, width = 640, height = 480, font =
("Monospace", 14), highlightthickness = 0, bd = 2)
textArea.pack()

# Call menufunc
menufunc.new()
menufunc.openFile()
menufunc.saveFile()
menufunc.copy()
menufunc.paste()
menufunc.delete()
menufunc.selectAll()
menufunc.rename()
menufunc.about()
menufunc.exit()

# Menu options
menu = Menu(root)
root.config(menu = menu)

fileMenu = Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New")
fileMenu.add_command(label = "Open", command = openFile)
fileMenu.add_command(label = "Save")
fileMenu.add_separator()
fileMenu.add_command(label = "Print")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exit)

editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Cut")
editMenu.add_command(label = "Copy")
editMenu.add_command(label = "Paste")
editMenu.add_separator()
editMenu.add_command(label = "Delete")
editMenu.add_command(label = "Rename")
editMenu.add_command(label = "Select All")

helpMenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label = "About")

# Status bar
statusBar = Label(root, text ="Al momento non fa nulla...", bd = 1, relief = SUNKEN, anchor = W)
statusBar.pack(side = BOTTOM, fill = X)

# Keep window open
root.mainloop()

#####################################################################

