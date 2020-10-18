from tkinter import *

class RemoveStudents(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent

        labelmain= Label(self,text="Remove Students",font=("bold",18),bg='misty rose')
        labelmain.place(x=150,y=30)

        label0=Label(self,text='Department:',width=10,font=("bold",10),bg='floral white').place(x=80,y=100)
        self.list0=('CS', 'ME', 'IC');
        self.d=StringVar()
        droplist=OptionMenu(self,self.d,*self.list0)
        droplist.config(width=20, bg='floral white')
        self.d.set('Select department')
        droplist.place(x=240,y=100)

        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)

        nextbutton= Button(self,text='Next',width=20,font=("bold",10),bg='floral white',command= lambda: self.Next())
        nextbutton.place(x=180,y=350)

    def Next(self):
        if str(self.d.get())==self.list0[0]:
            import win0_020
            self.parent.CurrentPage=win0_020.CSStudents(self)
            self.parent.CurrentPage.tkraise()
        
        if str(self.d.get())==self.list0[1]:
            import win0_021
            self.parent.CurrentPage=win0_021.MEStudents(self)
            self.parent.CurrentPage.tkraise()
        if str(self.d.get())==self.list0[2]:
            import win0_022
            self.parent.CurrentPage=win0_022.EEStudents(self)
            self.parent.CurrentPage.tkraise()

    def back(self):
        import win0_00
        self.parent.CurrentPage=win0_00.MainMenu(self)
        self.parent.CurrentPage.tkraise()
