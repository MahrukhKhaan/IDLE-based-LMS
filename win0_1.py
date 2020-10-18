from tkinter import *

class UserLogin(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text='USER LOGIN',width=20,font=("bold",18),bg='misty rose').place(x=90,y=30)
       
        labelacc= Label(self,text='Roll No',width=10,font=("bold",10),bg='floral white').place(x=80,y=130)
        self.varacc=StringVar()
        entryacc= Entry(self,textvariable=self.varacc).place(x=240,y=130)

        labelpass= Label(self,text='Password',width=10,font=("bold",10),bg='floral white').place(x=80,y=180)
        self.varpass=StringVar()
        entrypass= Entry(self,textvariable=self.varpass).place(x=240,y=180)
        
        labellogin= Label(self, text="Don't have an account yet?", width=25,font=("bold",10),bg='misty rose')
        labellogin.place(x=80,y=250)

        nextbutton = Button(self, text="Next", width=10, command= lambda: self.win2())
        nextbutton.place(x=350,y=210)

        backbutton = Button(self, text="Back", width=10, command= lambda: self.back())
        backbutton.place(x=400,y=10)
        
        buttonrf= Button(self,text='REGISTER NOW',width=20,font=("bold",10),bg='floral white',command= lambda: self.win1())
        buttonrf.place(x=180,y=280)
        
    def win1(self):
        import win1
        self.parent.CurrentPage=win1.RegistrationForm(self)
        self.parent.CurrentPage.tkraise()
    
    def win2(self):
        if self.varacc and self.varpass:
            import det
            if str(self.varacc.get()) in det.rollno:
                if str(self.varpass.get()) in det.password:
                    import win2
                    self.parent.CurrentPage=win2.MainMenu(self)
                    self.parent.CurrentPage.tkraise()
                else:
                    print('Incorrect Password')
            else:
                print('Register first')
            
        else:
            print('FILL THE ENTRIES')

    def back(self):
        import win0
        self.parent.CurrentPage=win0.LoginPage(self)
        self.parent.CurrentPage.tkraise()
