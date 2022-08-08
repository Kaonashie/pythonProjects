import sys
import tkinter
from tkinter import *
from tkinter import filedialog
root = Tk("Text Editor")
text = Text(root)
text.grid()

def saveAs():
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()
button = Button(root, text="Save", command = saveAs)
button.grid() 

def FontHelvetica():
    global text
    text.config(font = "Helvetica")
def FontCourrier():
    global text
    text.config(font = "Courier")
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_radiobutton(label = "Courier", variable = courier, command = FontCourrier)
font.menu.add_radiobutton(label = "Helvetica", variable = helvetica, command = FontHelvetica)




root.mainloop()