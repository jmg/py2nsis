#!/usr/bin/python

# Tkinter interface to the McMillan installer
# (c) 2003 Alan James Salmoni - yes, all this bad code is all mine!!!
# released under the MIT license

import os, os.path
from Tkinter import *
import tkFileDialog
import FileDialog

class McGUI:
    def __init__(self):
        root = Tk()
        fr1 = Frame(root)
        fr1["width"] = 200
        fr1["height"] = 100
        fr1.pack(side="top")
        fr2 = Frame(root)
        fr2["width"] = 200
        fr2["height"] = 300
        fr2["borderwidth"] = 2
        fr2["relief"] = "ridge"
        fr2.pack()
        fr4 = Frame(root)
        fr4["width"]=200
        fr4["height"]=100
        fr4.pack(side="bottom")
        getFileButton = Button(fr1)
        getFileButton["text"] = "Script..."
        getFileButton.bind("<Button>",self.GetFile)
        getFileButton.pack(side="left")
        self.filein = Entry(fr1)
        self.filein.pack(side="right")
        self.filetypecheck = Checkbutton(fr2)
        self.filetypecheck["text"] = "One File Package                 "
        self.filetype = IntVar()
        self.filetypecheck["variable"] = self.filetype
        self.filetypecheck.pack()
        self.tkcheck = Checkbutton(fr2)
        self.tkcheck["text"] = "Include Tcl/Tk                         "
        self.tk = IntVar()
        self.tkcheck["variable"] = self.tk
        self.tkcheck.pack()
        self.asciicheck = Checkbutton(fr2)
        self.asciicheck["text"] = "Do NOT include decodings"
        self.ascii = IntVar()
        self.asciicheck["variable"] = self.ascii
        self.asciicheck.pack()
        self.debugcheck = Checkbutton(fr2)
        self.debugcheck["text"] = "Use debug versions             "
        self.debug = IntVar()
        self.debugcheck["variable"] = self.debug
        self.debugcheck.pack()
        self.noconsolecheck = Checkbutton(fr2)
        self.noconsolecheck["text"] = "No console (Windows only)"
        self.noconsole = IntVar()
        self.noconsolecheck["variable"] = self.noconsole
        self.noconsolecheck.pack()
        okaybutton = Button(fr4)
        okaybutton["text"] = "Okay   "
        okaybutton.bind("<Button>",self.makePackage)
        okaybutton.pack(side="left")
        cancelbutton = Button(fr4)
        cancelbutton["text"] = "Cancel"
        cancelbutton.bind("<Button>",self.killapp)
        cancelbutton.pack(side="right")
        self.fin = ''
        self.fout = ''
        root.mainloop()

    def killapp(self, event):
        sys.exit(0)

    def makePackage(self, event):
        commands = 'python Makespec.py '
        if (self.filetype.get() == 1):
            commands = commands + '--onefile '
        if (self.tk.get() == 1):
            commands = commands + '--tk '
        if (self.ascii.get() == 1):
            commands = commands + '--ascii '
        if (self.debug.get() == 1):
            commands = commands + '--debug '
        if (self.noconsole.get() == 1):
            commands = commands + '--noconsole '
        commands = commands + self.fin
        x = os.path.split(self.fin)
        y = os.path.splitext(x[1])
        os.system(commands)
        commands = 'python Build.py '+str(y[0])+os.sep+str(y[0])+'.spec'
        os.system(commands)
        sys.exit(0)

    def GetFile(self, event):
        self.fin = tkFileDialog.askopenfilename()
        self.filein.insert(0,self.fin)

if __name__ == "__main__":
    app = McGUI()
