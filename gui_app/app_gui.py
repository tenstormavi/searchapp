#!/usr/bin/env python
import Tkinter
import os
import sys
import requests
import json 
import time 
import pdb
import collections
from Tkinter import *
from ScrolledText import *
from ipdb import set_trace


class share(Frame):
  
    def __init__(self, parent):

        #root = Tk()
        
        Frame.__init__(self, parent, background = "grey")   
        self.parent = parent
        
        self.parent.title("Search App")
        self.pack()
        self.centerWindow()
        self.cwd = StringVar(self.parent)
        self.dirfm = Frame(self.parent)
        self.label = Label(self.dirfm, text = "")
        self.label.pack()
        self.label = Tkinter.Label(self.dirfm, text = 'Enter the name of the file', font = 'Times -18 bold')
        self.label.pack()
        self.label = Label(self.dirfm, text = "")
        self.label.pack()
        
        self.dirn = Entry(self.dirfm, width = 50, textvariable = self.cwd)
        self.dirn.bind('<Return>', self.search)
        
        self.dirn.pack()
        self.label = Label(self.dirfm, text = "")
        self.label.pack()
    
        #scrollbar = Scrollbar()
        #scrollbar.pack(side=RIGHT, fill=Y)

        #listbox = Listbox()
        #listbox.pack()
        self.dirfm.pack()
        #self.textPad.pack()
        #self.textPad.text(s)
        self.text = Text (width=40,height=20)
        self.text.pack ()

        S = Scrollbar(command=self.text.yview)
        self.text.config(wrap=WORD ,yscrollcommand=S.set)
        #S.pack(side=RIGHT, fill=Y)
    
        S.config(command=self.text.yview)
        
        

        self.label = Label(self.dirfm, text = "")
        self.label.pack()
        self.difrm = Frame(self.parent)
        self.clear = Tkinter.Button(self.difrm, text = 'Clear', command = self.clear, bg = 'blue', fg = 'black', padx = 10)
        self.clear.pack(side = LEFT)
        self.quit = Tkinter.Button(self.difrm, text = 'Exit', command = self.parent.quit, bg = 'green', fg = 'black', padx = 10)
        self.quit.pack(side = LEFT)
        self.difrm.pack(expand = 0.5)

    def  clear1(self):

        self.text.delete ("1.0","50.0")

    def search(self, ev = None):
        symbol = self.cwd.get()
        #print symbol
        #self.label.config(text = "Searching ...")
        #self.label.update()
        #toplevel = Toplevel()
        #toplevel.title('Similar Files And their Paths')
        #toplevel.focus_set()
        pathname = os.path.dirname(sys.argv[0])
        fullpath = os.path.abspath(pathname)
        listof_files = []
        location_list = []
        big_list = collections.defaultdict(list)
        start_time = time.time()
        i=0
        fout = open("test.json",'w')
        for dirname, dirnames, filenames in os.walk('.'):
            for subdirname in dirnames:
                os.path.join(dirname,subdirname)
            for filename in filenames:
                location = os.path.join(dirname,filename)
                location_list.append (location)
                file_name = filename
                s = tuple(file_name)
                r = []
                for size in range(1, len(s)+1):
                    for index in range(len(s)+1-size):
                        x= file_name[index:index+size]
                        big_list[x].append(i)
                i=i+1
        #print big_list.items()
        if symbol in big_list:
            n = big_list[symbol]
            #print n
            #print symbol
            l=0
            p=""
            for v in n:
                l=location_list[v]
                l = l[1:]
                p= p + fullpath + l + "\n"
            result= p
            #self.label.config(text = result)
            #self.label.update()
            #self.textPad.config(text=result)
            #self.textPad.update()
            #print p
            self.text.insert(INSERT,p)    
            

        #listbox.config(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=listbox.yview)

        else:
            self.text.insert(INSERT,"Their is no file exists")
                #self.label.config(text = result)
                #self.label.update()
        
    

    def centerWindow(self):
      
        w = 500
        h = 500

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def clear(self, ev = None):
        self.dirn.delete(0, Tkinter.END)
        self.label.config(text = " ")
        self.label.update()


def main():
    root = Tk()
    app = share(root)
    root.mainloop()  

if __name__ == '__main__':
    main() 