from tkinter import *

class MainMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent

        labelmain= Label(self,text='MAIN MENU',width=20,font=("bold",18),bg='misty rose').place(x=90,y=30)

        button1= Button(self,text="1.Remove Books",font=("bold",10),command= lambda: self.RemoveBooks())
        button1.place(x=120,y=100)

        button2= Button(self,text="2.Remove Students",font=("bold",10),command= lambda: self.RemoveStudents())
        button2.place(x=120,y=140)

        button3= Button(self,text="3.Add Books",font=("bold",10),command= lambda: self.AddBooks())
        button3.place(x=120,y=180)

        backbutton = Button(self, text="LOG OUT",command= lambda: self.back())
        backbutton.place(x=430, y=10)


    def back(self):
        import win0 
        self.parent.CurrentPage=win0.LoginPage(self)
        self.parent.CurrentPage.tkraise()

    def RemoveBooks(self):
        import win0_01
        self.parent.CurrentPage=win0_01.RemoveBooks(self)
        self.parent.CurrentPage.tkraise()
        
    def RemoveStudents(self):
        import win0_02
        self.parent.CurrentPage=win0_02.RemoveStudents(self)
        self.parent.CurrentPage.tkraise()
        
    def AddBooks(self):
        import win0_03
        self.parent.CurrentPage=win0_03.AddBooks(self)
        self.parent.CurrentPage.tkraise()
        
