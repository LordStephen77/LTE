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
        pass
        
    def paste():
        pass
        
    def delete():
        pass
        
    def selectAll():
        pass
        
    def rename():
        pass
        
    def about():
        pass
            
    def exit():
        root.destroy()
