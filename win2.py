from tkinter import *

class MainMenu(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text="MAIN MENU",font=("bold",18),bg='misty rose')
        labelmain.place(x=150,y=30)

        button1= Button(self,text="1.Borrow Books",font=("bold",10),command= lambda: self.BorrowBooks())
        button1.place(x=120,y=100)
        
        button2= Button(self,text="2.Available Books",font=("bold",10),command= lambda: self.AvailableBooks())
        button2.place(x=120,y=140)

        button3= Button(self,text="3.Return Books",font=("bold",10),command= lambda: self.ReturnBooks())
        button3.place(x=120,y=180)

        backbutton = Button(self, text="LOG OUT",command= lambda: self.back())
        backbutton.place(x=430, y=10)

        nextbutton= Button(self,text='NEXT',width=20,font=("bold",10),bg='floral white')
        nextbutton.place(x=180,y=280)


    def back(self):
        import win0_1
        self.parent.CurrentPage=win0_1.UserLogin(self)
        self.parent.CurrentPage.tkraise()
        
    def BorrowBooks(self):
        import win2_0
        self.parent.CurrentPage=win2_0.BorrowBooks(self)
        self.parent.CurrentPage.tkraise()

    def AvailableBooks(self):
        import win2_1
        self.parent.CurrentPage=win2_1.AvailableBooks(self)
        self.parent.CurrentPage.tkraise()

    def ReturnBooks(self):
        import win2_2
        self.parent.CurrentPage=win2_2.ReturnBooks(self)
        self.parent.CurrentPage.tkraise()





        

