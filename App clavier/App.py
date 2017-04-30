from tkinter import *
from HoverCanvas import HoverCanvas
from HoverCanvas2 import HoverCanvas2
from HoverCanvasEffacer import HoverCanvasEffacer
from HoverCanvasToutEffacer import HoverCanvasToutEffacer
from Label1 import Label1
from PIL import Image, ImageTk


class Interface(Tk):
    
    def __init__(self):
        Tk.__init__(self)        
        self.geometry("1300x900")
        self.title('Affichage des formes')
        self._first=True


        frame_text = Frame(self)
        frame_text.pack(side=TOP)

        frame_predict = Frame(self)
        frame_predict.pack(side=TOP)

        frame = Frame(self, pady=10)
        frame.pack(side=TOP)

        frame2 = Frame(self, pady=10)
        frame2.pack(side=TOP)
        
        frame3 = Frame(self, pady=10)
        frame3.pack(side=TOP)
        
        frame4 = Frame(self)
        frame4.pack(side=TOP, pady=10)

        image1 = Image.open("Pasted Graphic 4.tiff.tiff")
        photo1 = ImageTk.PhotoImage(image1)

        label1 = Label(self, image=photo1)
        label1.image = photo1
        label1.place(x=0, y=0)

        image2 = Image.open("Pasted Graphic 5.tiff.tiff")
        photo2 = ImageTk.PhotoImage(image2)

        label2 = Label(self, image=photo2)
        label2.image = photo2
        label2.place(relx=0.42 , rely=0)


        image3 = Image.open("Pasted Graphic 6.tiff.tiff")
        photo3 = ImageTk.PhotoImage(image3)

        label3 = Label(self, image=photo3)
        label3.image = photo3
        label3.place(relx=1, rely=0, anchor=NE)

        image4 = Image.open("Pasted Graphic 7.tiff.tiff")
        photo4 = ImageTk.PhotoImage(image4)

        label4 = Label(self, image=photo4)
        label4.image = photo4
        label4.place(relx=0, rely=1, anchor=SW)

        image5 = Image.open("Pasted Graphic 8.tiff.tiff")
        photo5 = ImageTk.PhotoImage(image5)

        label5 = Label(self, image=photo5)
        label5.image = photo5
        label5.place(relx=0.42, rely=1, anchor=SW)

        image6 = Image.open("Pasted Graphic 9.tiff.tiff")
        photo6 = ImageTk.PhotoImage(image6)

        label6 = Label(self, image=photo6)
        label6.image = photo6
        label6.place(relx=1, rely=1, anchor=SE)



        dummy_label = Label(frame_text, text="                                                         ")
        dummy_label.pack(side=LEFT)

        label_text = Label1(frame_text, "Regarder les lettres pour écrire")
        label_text.pack(side=LEFT)



        predict1=HoverCanvas2(frame_predict, label_text)
        predict1.pack(side=LEFT)
        predict2=HoverCanvas2(frame_predict, label_text)
        predict2.pack(side=LEFT)
        predict3=HoverCanvas2(frame_predict, label_text)
        predict3.pack(side=LEFT)

        HoverCanvas(frame, "Q", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50,width=5).pack(side=LEFT)
        HoverCanvas(frame, "W", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50,width=5).pack(side=LEFT)
        HoverCanvas(frame, "E", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50,width=5).pack(side=LEFT)
        HoverCanvas(frame, "R", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame, "T", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame, "Y", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame, "U", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame, "I", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame, "O", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame, "P", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame, height=50, width=5).pack(side=LEFT)
        HoverCanvasEffacer(frame, "CC", label_text, predict1, predict2, predict3).pack( side = LEFT)
        HoverCanvas(frame2, "A", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "S", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "D", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "F", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "G", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "H", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "J", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "K", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "L", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame2, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame2, "Ç", label_text, predict1, predict2, predict3).pack( side = LEFT)
        HoverCanvas(frame3, "Z", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, "X", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, "C", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, "V", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, "B", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, "N", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, "M", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, ",", label_text, predict1, predict2, predict3).pack( side = LEFT)
        Canvas(frame3, height=50, width=5).pack(side=LEFT)
        HoverCanvas(frame3, ".", label_text, predict1, predict2, predict3).pack( side = LEFT)

        HoverCanvas(frame4, "_", label_text, predict1, predict2, predict3).pack( side = LEFT)
        HoverCanvasToutEffacer(frame4, "Effacer", label_text, predict1, predict2, predict3).pack( side = LEFT)


    def getfirst(self):
        return self._first




application = Interface()
mainloop()


