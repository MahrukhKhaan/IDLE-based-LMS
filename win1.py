from tkinter import *

class RegistrationForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text='Registration Form',width=20,font=("bold",18),bg='misty rose')
        labelmain.place(x=90,y=30)
        
        label0= Label(self,text='Full Name',width=10,font=("bold",10),bg='floral white').place(x=80,y=100)
        self.var0=StringVar()
        entry0= Entry(self,textvariable=self.var0).place(x=240,y=100)
        
        label1= Label(self,text='Roll No',width=10,font=("bold",10),bg='floral white').place(x=80,y=130)
        self.var1=StringVar()
        entry1= Entry(self,textvariable=self.var1,width=5).place(x=240,y=130)
        
        label2= Label(self,text='Gender',width=10,font=("bold",10),bg='floral white').place(x=80,y=160)
        self.var2= IntVar()
        self.var2.set('0')
        btnmale=Radiobutton(self,text='Male',variable=self.var2,value=1,bg='misty rose').place(x=240,y=160)
        btnfemale=Radiobutton(self,text='Female',variable=self.var2,value=2,bg='misty rose').place(x=300,y=160)

        label3= Label(self,text='Email',width=10,font=("bold",10),bg='floral white').place(x=80,y=190)
        self.var3=StringVar()
        entry3= Entry(self,textvariable=self.var3).place(x=240,y=190)
 
        label4= Label(self,text='City',width=10,font=("bold",10),bg='floral white')
        label4.place(x=80,y=240)
        list4=('Karachi', 'Lahore', 'Islamabad');
        self.c=StringVar()
        droplist=OptionMenu(self,self.c,*list4)
        droplist.config(width=20, bg='floral white')
        self.c.set('Select your city')
        droplist.place(x=240,y=235)

        label5=Label(self,text='Department',width=10,font=("bold",10),bg='floral white')
        label5.place(x=80,y=270)
        list5=('CS', 'ME', 'IC');
        self.d=StringVar()
        droplist=OptionMenu(self,self.d,*list5)
        droplist.config(width=20, bg='floral white')
        self.d.set('Select your department')
        droplist.place(x=240,y=265)

        
        submitbutton= Button(self,text='SUBMIT',width=10,font=("bold",10),bg='floral white',fg='black',command=lambda:self.submit())
        submitbutton.place(x=200,y=330)

        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)

        hpbutton = Button(self, text="Homepage",width=10, command= lambda:self.homepage())
        hpbutton.place(x=360, y=10)


    def submit(self):
        if self.var0.get() and self.var1.get() and self.var2.get() and self.var3.get() and self.c.get() and self.d.get():
             import det
             det.fullname.append(str(self.var0.get()))
             det.rollno.append(str(self.var1.get()))
             det.gender.append(str(self.var2.get()))
             det.email.append(str(self.var3.get()))
             det.city.append(str(self.c.get()))
             det.department.append(str(self.d.get()))
             import win1_0
             self.parent.CurrentPage=win1_0.PC(self)
             self.parent.CurrentPage.tkraise()
        else:
             print('Fill the form completely')

    def back(self):
        import win0_1
        self.parent.CurrentPage=win0_1.UserLogin(self)
        self.parent.CurrentPage.tkraise()

    def homepage(self):
        import win0
        self.parent.CurrentPage=win0.LoginPage(self)
        self.parent.CurrentPage.tkraise()       





