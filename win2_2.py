from tkinter import *
import det

class ReturnBooks(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text="Your borrowed books are:",font=("bold",14),bg='misty rose')
        labelmain.place(x=120,y=30)

        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)

        hpbutton = Button(self, text="Homepage",width=10, command= lambda:self.homepage())
        hpbutton.place(x=360, y=10)

        emptylist=[]

        if emptylist == det.borrowedbooks:
            
            labelmain= Label(self,text="You have no borrowed books",font=("bold",14),bg='floral white').place(x=120,y=130)
          
        else:
            poy=100
            for books in det.borrowedbooks:
                labelbb= Label(self,text=books,bg='misty rose').place(x=100,y=poy)
                poy=poy+30
            labelrb = labelmain= Label(self,text="Enter the name of the book you would like to return:",font=("bold",10),bg='misty rose').place(x=80,y=280)
            self.var_rb=StringVar()
            entry_rb=Entry(self,textvariable=self.var_rb).place(x=90,y=310)
            nextbutton = Button(self, text="Return Book",width=10, command= lambda:self.Next()).place(x=360, y=330)

    def Next(self):
        if str(self.var_rb.get()) in det.listofbooks:
            print(str(self.var_rb.get()),' has been returned')
            det.borrowedbooks.remove(str(self.var_rb.get()))
        else:
            print(str(self.var_rb.get()),' has already been removed')


    def back(self):
        import win2
        self.parent.CurrentPage=win2.MainMenu(self)
        self.parent.CurrentPage.tkraise() 

    def homepage(self):
        import win0_1
        self.parent.CurrentPage=win0_1.UserLogin(self)
        self.parent.CurrentPage.tkraise()
        
