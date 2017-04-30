from tkinter import *
from HoverCanvas import HoverCanvas
from HoverCanvasOn import HoverCanvasOn
from HoverCanvasOff import HoverCanvasOff

class Interface(Tk):
    
    def __init__(self):
        Tk.__init__(self)        
        self.geometry("500x500+100+100")     
        self.title('Affichage des formes')
        
        frame = Frame(self)
        frame.pack(side=TOP)
        

        HoverCanvasOn(frame, "On").pack( side = LEFT)
        HoverCanvasOff(frame, "Off").pack( side = LEFT)



application = Interface()
mainloop()





