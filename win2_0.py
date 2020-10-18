from tkinter import *
import det

class BorrowBooks(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        
        labelmain= Label(self,text="Borrow Books",font=("bold",18),bg='misty rose')
        labelmain.place(x=150,y=30)

        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)

        hpbutton = Button(self, text="Homepage",width=10, command= lambda:self.homepage())
        hpbutton.place(x=360, y=10)

        nextbutton= Button(self,text='Borrow Books',width=20,font=("bold",10),bg='floral white',command= lambda: self.Next())
        nextbutton.place(x=180,y=350)

        authorofbooks=['a','b','c','d','e','f','g']

        self.var0=IntVar()
        cb0=Checkbutton(self,text=det.listofbooks[0]+'\t'+'\t'+'\t'+authorofbooks[0],bg='misty rose',variable=self.var0).place(x=100,y=100)

        self.var1=IntVar()
        cb1=Checkbutton(self,text=det.listofbooks[1]+'\t'+'\t'+'\t'+authorofbooks[1],bg='misty rose',variable=self.var1).place(x=100,y=130)

        self.var2=IntVar()
        cb3=Checkbutton(self,text=det.listofbooks[2]+'\t'+'\t'+'\t'+authorofbooks[2],bg='misty rose',variable=self.var2).place(x=100,y=160)
        
        self.var3=IntVar()
        cb3=Checkbutton(self,text=det.listofbooks[3]+'\t'+'\t'+'\t'+authorofbooks[3],bg='misty rose',variable=self.var3).place(x=100,y=190)    

        self.var4=IntVar()
        cb4=Checkbutton(self,text=det.listofbooks[4]+'\t'+'\t'+'\t'+authorofbooks[4],bg='misty rose',variable=self.var4).place(x=100,y=220)  

        self.var5=IntVar()
        cb5=Checkbutton(self,text=det.listofbooks[5]+'\t'+'\t'+'\t'+authorofbooks[5],bg='misty rose',variable=self.var5).place(x=100,y=250)

        self.var6=IntVar()
        cb6=Checkbutton(self,text=det.listofbooks[6]+'\t'+'\t'+'\t'+authorofbooks[6],bg='misty rose',variable=self.var6).place(x=100,y=280)
        
    def Next(self):
        if self.var0.get()==1 :
            if det.listofbooks[0] in det.borrowedbooks:
                print('Sorry,',det.listofbooks[0],' has already been borrowed')
            else:
                det.borrowedbooks.append(det.listofbooks[0])
                print(det.listofbooks[0],'has been borrowed')
        if self.var1.get()==1 :
            if det.listofbooks[1] in det.borrowedbooks:
                print('Sorry,',det.listofbooks[1],' has already been borrowed')
            else:
                det.borrowedbooks.append(det.listofbooks[1])
                print(det.listofbooks[1],'has been borrowed')
        if self.var2.get()==1 :
            if det.listofbooks[2] in det.borrowedbooks:
                print('Sorry,',det.listofbooks[2],' has already been borrowed')
            else:            
                det.borrowedbooks.append(det.listofbooks[2])
                print(det.listofbooks[2],'has been borrowed')
        if self.var3.get()==1 :
            if det.listofbooks[3] in det.borrowedbooks:
                print('Sorry,',det.listofbooks[3],' has already been borrowed')
            else:
                det.borrowedbooks.append(det.listofbooks[3])
                print(det.listofbooks[3],'has been borrowed')
        if self.var4.get()==1 :
            if det.listofbooks[4] in det.borrowedbooks:
                print('Sorry,',det.listofbooks[4],' has already been borrowed')
            else:
                det.borrowedbooks.append(det.listofbooks[4])
                print(det.listofbooks[4],'has been borrowed')
        if self.var5.get()==1 :
            if det.listofbooks[5] in det.borrowedbooks:
                print('Sorry,',self.listofbooks[5],' has already been borrowed')
            else:
                det.borrowedbooks.append(det.listofbooks[5])
                print(det.listofbooks[5],'has been borrowed')
        if self.var6.get()==1 :
            if det.listofbooks[6] in det.borrowedbooks:
                print('Sorry,',det.listofbooks[6],' has already been borrowed')
            else:
                det.borrowedbooks.append(det.listofbooks[6])
                print(det.listofbooks[6],'has been borrowed')
        else:
            pass


    def back(self):
        import win2
        self.parent.CurrentPage=win2.MainMenu(self)
        self.parent.CurrentPage.tkraise()

    def homepage(self):
        import win0
        self.parent.CurrentPage=win0.LoginPage(self)
        self.parent.CurrentPage.tkraise()
        
