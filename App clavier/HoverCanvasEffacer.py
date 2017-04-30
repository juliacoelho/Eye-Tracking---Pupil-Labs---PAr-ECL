from tkinter import *
from HoverCanvas2 import HoverCanvas2

class HoverCanvasEffacer(Canvas):
    
    def __init__(self, parent, lettre, label, pred1, pred2, pred3):
        Canvas.__init__(self, parent, width = 100, height = 100, bg = 'white',highlightbackground='black')
        self._dans = False
        self._count = 0
        self._tk = parent
        self._lettre = lettre
        self._label = label
        self._pred1 = pred1
        self._pred2 = pred2
        self._pred3 = pred3
        self.bind("<Enter>",self.Display )
        self.bind("<Leave>",self.Remove )
        self.create_text(50, 50, text = self._lettre)
        
    def Display(self, event):
        if not self._dans:
            self._dans = True
            #print (self._count)
            self.compter()
            self._tk.after(700, self.Display2)
    
    def Display2(self):
        if self._dans:
            #print (self._count)
            self.compter()
            self._tk.after(700, self.Display2)
            
    def Remove(self, event):
        if self._dans:
            self._dans=False
            self.notcompter()
            self._tk.after(500, self.Remove2)
    
    def Remove2(self):
        if not self._dans:
            self.notcompter()
            self._tk.after(500, self.Remove2)
                        
    def compter(self):
        if self._count < 2:
            self._count += 1
        else:
            #print ("3")
            print (self._lettre)
            self._label.config(text = self._label.cget("text")[:-1])
            self._count = 0
            txt = self.lastwords()
            a = txt[0][0]
            b = txt[1][0]
            c = txt[2][0]
            self._pred1.delete("all")
            self._pred2.delete("all")
            self._pred3.delete("all")
            self._pred1.create_text(150, 50, text=a)
            self._pred2.create_text(150, 50, text=b)
            self._pred3.create_text(150, 50, text=c)
            self._pred1.settexte(a)
            self._pred2.settexte(b)
            self._pred3.settexte(c)


            
    def notcompter(self):
        if self._count > 0:
            self._count -= 1
        #else:
            #print ("zerou")

    def lastwords(self):
        autocomplete.load()
        if len(self._label.cget("text").split("_")) > 1:
            a = self._label.cget("text").split("_")[-2:]
            return autocomplete.predict(a[0], a[1])
        else: return [("",1),("",1),("",1)]