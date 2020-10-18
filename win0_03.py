from tkinter import *
import det

class AddBooks(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text='Add Books',width=20,font=("bold",18),bg='misty rose').place(x=90,y=30)

        labelmain= Label(self,text='Enter the book that you want to add:',font=("bold",10),bg='misty rose').place(x=90,y=100)

        self.var0=StringVar()
        entry0= Entry(self,textvariable=self.var0).place(x=160,y=150)
    
        nextbutton= Button(self,text='Add Book',width=10,font=("bold",10),command= lambda:self.Next()).place(x=220,y=190)

        backbutton= Button(self,text='Back',width=10,font=("bold",10),command= lambda:self.back()).place(x=400,y=10)
    
    def Next(self):
        if self.var0.get():
            if str(self.var0.get()) in det.borrowedbooks:
                print(str(self.var0.get()),'is already in the collection')
            else:
                print(str(self.var0.get()),'has been added to the collection')
                det.listofbooks.append(str(self.var0.get()))           
            
    def back(self):
        import win0_00
        self.parent.CurrentPage=win0_00.MainMenu(self)
        self.parent.CurrentPage.tkraise()
