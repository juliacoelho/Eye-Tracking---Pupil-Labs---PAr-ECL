from tkinter import *


class Label1(Label):
    def __init__(self, parent, texte):
        Label.__init__(self,  parent, text= texte, pady = 45)
        self._first=True

    def getfirst(self):
        return self._first

    def setfirst(self):
        self._first= False