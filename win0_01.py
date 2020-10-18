from tkinter import *
import det

class RemoveBooks(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent

        labelmain= Label(self,text="Remove Books",font=("bold",18),bg='misty rose')
        labelmain.place(x=150,y=30)

        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)

        nextbutton= Button(self,text='NEXT',width=20,font=("bold",10),bg='floral white',command= lambda: self.Next())
        nextbutton.place(x=180,y=350)

        self.var0=IntVar()
        cb0=Checkbutton(self,text=det.listofbooks[0],bg='misty rose',variable=self.var0).place(x=100,y=100)

        self.var1=IntVar()
        cb1=Checkbutton(self,text=det.listofbooks[1],bg='misty rose',variable=self.var1).place(x=100,y=130)

        self.var2=IntVar()
        cb3=Checkbutton(self,text=det.listofbooks[2],bg='misty rose',variable=self.var2).place(x=100,y=160)
        
        self.var3=IntVar()
        cb3=Checkbutton(self,text=det.listofbooks[3],bg='misty rose',variable=self.var3).place(x=100,y=190)    

        self.var4=IntVar()
        cb4=Checkbutton(self,text=det.listofbooks[4],bg='misty rose',variable=self.var4).place(x=100,y=220)  

        self.var5=IntVar()
        cb5=Checkbutton(self,text=det.listofbooks[5],bg='misty rose',variable=self.var5).place(x=100,y=250)

        self.var6=IntVar()
        cb6=Checkbutton(self,text=det.listofbooks[6],bg='misty rose',variable=self.var6).place(x=100,y=280)
        
    def Next(self):
        if self.var0.get()==1 :
            if det.listofbooks[0] in det.listofbooks:
                print(det.listofbooks[0],'has been removed')
                det.listofbooks.remove(det.listofbooks[0])
            else:
                print(det.listofbooks[0],'has already been removed')
        if self.var1.get()==1 :
            if det.listofbooks[1] in det.listofbooks:
                print(det.listofbooks[1],'has been removed')
                det.listofbooks.remove(det.listofbooks[1])
            else:
                print(det.listofbooks[1],'has already been removed')
        if self.var2.get()==1 :
            if det.listofbooks[2] in det.listofbooks:
                print(det.listofbooks[2],'has been removed')
                det.listofbooks.remove(det.listofbooks[2])
            else:
                print(det.listofbooks[2],'has already been removed')
        if self.var3.get()==1 :
            if det.listofbooks[3] in det.listofbooks:
                print(det.listofbooks[3],'has been removed')
                det.listofbooks.remove(det.listofbooks[3])
            else:
                print(det.listofbooks[3],'has already been removed')
        if self.var4.get()==1 :
            if det.listofbooks[4] in det.listofbooks:
                print(det.listofbooks[4],'has been removed')
                det.listofbooks.remove(det.listofbooks[4])
            else:
                print(det.listofbooks[4],'has already been removed')
        if self.var5.get()==1 :
            if det.listofbooks[5] in det.listofbooks:
                print(det.listofbooks[5],'has been removed')
                det.listofbooks.remove(det.listofbooks[5])
            else:
                print(det.listofbooks[5],'has already been removed')
        if self.var6.get()==1 :
            if det.listofbooks[6] in det.listofbooks:
                print(det.listofbooks[6],'has been removed')
                det.listofbooks.remove(det.listofbooks[6])
            else:
                print(det.listofbooks[6],'has already been removed')
        else:
            pass
        
    def back(self):
  
        import win0_00
        self.parent.CurrentPage=win0_00.MainMenu(self)
        self.parent.CurrentPage.tkraise()
