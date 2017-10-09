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
* @create      dom 09 ott 2017 11:43:37 CEST
* @update      none

"""

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
    pass
        
def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
        
def paste():
    try:
        teext = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, teext)
    except:
        tkMessageBox.showerror("Errore","Gli appunti sono vuoti!")
        
def delete():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)
        
def selectAll():
    pass
        
def rename():
    pass
    
def line():
    lin = "_" * 60
    text.insert(INSERT,lin)

def date():
    data = datetime.date.today()
    text.insert(INSERT,data)
        
def about():
    ab = Toplevel(root)

    txt = "LTE (Lightweight Text Editor\nRealizzato da Stefano Peris (C)\n https://github.com/LordStephen77/LTE\nIl programma è rilasciato sotto licensa GPL"
    la = Label(ab, text = txt, foreground = 'blue')
    la.pack()
            
def exit():
    root.destroy()
