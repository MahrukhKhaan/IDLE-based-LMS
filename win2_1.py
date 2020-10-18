from tkinter import *
import det

class AvailableBooks(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent

        labelmain= Label(self,text="Available Books",font=("bold",18),bg='misty rose')
        labelmain.place(x=150,y=30)

        labelbn= Label(self,text="Books",font=("bold",10),bg='misty rose')
        labelbn.place(x=100,y=80)

        labelan= Label(self,text="Authors",font=("bold",10),bg='misty rose')
        labelan.place(x=310,y=80)

        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)

        hpbutton = Button(self, text="Homepage",width=10, command= lambda:self.homepage())
        hpbutton.place(x=360, y=10)


        authorofbooks=['a','b','c','d','e','f','g']

        poy=100
        count=0
        for books in det.listofbooks:
            labelbb= Label(self,text=books+'\t\t\t\t\t'+authorofbooks[count],bg='misty rose').place(x=100,y=poy)
            poy=poy+30
            count=count+1


    def back(self):
        import win2
        self.parent.CurrentPage=win2.MainMenu(self)
        self.parent.CurrentPage.tkraise()

    def homepage(self):
        import win0_1
        self.parent.CurrentPage=win0_1.UserLogin(self)
        self.parent.CurrentPage.tkraise()
        
