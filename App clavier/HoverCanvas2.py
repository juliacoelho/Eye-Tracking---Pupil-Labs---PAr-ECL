from tkinter import *
from gtts import gTTS
from playsound import playsound
import autocomplete


class HoverCanvas2(Canvas):
    def __init__(self, parent, label):
        Canvas.__init__(self, parent, width=300, height=100, bg='gray', highlightbackground='black')
        self._dans = False
        self._count = 0
        self._tk = parent
        self._texte = ""
        self._label = label
        self.bind("<Enter>", self.Display)
        self.bind("<Leave>", self.Remove)
        self.create_text(150, 50, text=self._texte)

    def Display(self, event):
        if not self._dans:
            self._dans = True
            # print (self._count)
            self.compter()
            self._tk.after(700, self.Display2)

    def Display2(self):
        if self._dans:
            # print (self._count)
            self.compter()
            self._tk.after(700, self.Display2)

    def Remove(self, event):
        if self._dans:
            self._dans = False
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
            #  print ("3")
            tts = gTTS(text=self._texte, lang='fr')
            tts.save("/home/julia"+self._texte+".wav")
            playsound("/home/julia" + self._texte + ".wav")
            self._label.config(
                text=self.changelabel())
            self._count = 0

    def notcompter(self):
        if self._count > 0:
            self._count -= 1
            # else:
            # print ("zerou")

    def changelabel(self):
        a=self._label.cget("text")
        print(a)
        a=a.split("_")
        print(a)
        a=a[:-1]
        print(a)
        a.append(self._texte)
        return "_".join(a)


    def settexte(self,texte):
        self._texte=texte
