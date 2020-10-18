from tkinter import *

class LMS(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.geometry(self, "500x500")
        Tk.title(self, "Library Management System")

        self.CurrentPage=LoginPage(self)
        self.CurrentPage.tkraise()

class LoginPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text='LOGIN PAGE',width=20,font=("bold",18),bg='misty rose').place(x=90,y=30)

        label0= Label(self,text='Login\tAs :',width=20,font=("bold",14),bg='misty rose').place(x=60,y=130)
    
        button0= Button(self,text='ADMIN',width=10,font=("bold",10),bg='floral white',command= lambda: self.adminlogin()).place(x=100,y=180)
        
        button1= Button(self,text='USER',width=10,font=("bold",10),bg='floral white',command= lambda: self.userlogin()).place(x=200,y=180)

    def adminlogin(self):
        import win0_0
        self.parent.CurrentPage=win0_0.AdminLogin(self)
        self.parent.CurrentPage.tkraise()
        
    def userlogin(self):
        import win0_1
        self.parent.CurrentPage=win0_1.UserLogin(self)
        self.parent.CurrentPage.tkraise()

if __name__=='__main__':
    root=LMS()
    root.mainloop()
