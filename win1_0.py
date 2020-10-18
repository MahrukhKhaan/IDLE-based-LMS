from tkinter import *

class PC(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text='Password Confirmation',width=20,font=("bold",18),bg='misty rose')
        labelmain.place(x=90,y=30)
        
        label0= Label(self,text='Enter Password:',width=20,font=("bold",10),bg='misty rose').place(x=80,y=100)
        self.var0=StringVar()
        entry0= Entry(self,textvariable=self.var0).place(x=200,y=120)
        
        label1= Label(self,text='Confirm Password:',width=20,font=("bold",10),bg='misty rose').place(x=80,y=200)
        self.var1=StringVar()
        entry1= Entry(self,textvariable=self.var1).place(x=200,y=220)

        nextbutton= Button(self,text='SUBMIT',width=10,font=("bold",10),bg='floral white',fg='black',command=lambda:self.next())
        nextbutton.place(x=200,y=330)

        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)



    def next(self):
        if self.var0.get() and self.var1.get():
            if str(self.var0.get())==str(self.var1.get()):
                import det
                det.password.append(str(self.var0.get()))
                import win0_1     
                self.parent.CurrentPage=win0_1.UserLogin(self)
                self.parent.CurrentPage.tkraise()
            else:
                print('Password does not match')
        else:
            print('PLEASE FILL')

    def back(self):
        import win1
        self.parent.CurrentPage=win1.RegistrationForm(self)
        self.parent.CurrentPage.tkraise()




