from tkinter import *

class AdminLogin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent

        labelmain= Label(self,text='Admin Login',width=20,font=("bold",18),bg='misty rose').place(x=90,y=30)

        labelpass= Label(self,text='Password',width=10,font=("bold",10),bg='floral white').place(x=80,y=180)
        self.varpass=StringVar()
        entrypass= Entry(self,textvariable=self.varpass).place(x=240,y=180)

        backbutton = Button(self, text="Back",command= lambda: self.back())
        backbutton.place(x=430, y=10)

        Nextbutton = Button(self, text="Next",command= lambda: self.Next(), width=10)
        Nextbutton.place(x=340, y=220)
        
    def back(self):
        import win0 
        self.parent.CurrentPage=win0.LoginPage(self)
        self.parent.CurrentPage.tkraise()

    def Next(self):
        if str(self.varpass.get())=='CISD':
            import win0_00
            self.parent.CurrentPage=win0_00.MainMenu(self)
            self.parent.CurrentPage.tkraise()
        else:
            print('Incorrect Password')
