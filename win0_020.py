from tkinter import *
import det

class CSStudents(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        Frame.config(self, width=500,height=500,bg='misty rose')
        Frame.pack(self, side=LEFT)
        self.parent=parent
        labelmain= Label(self,text="CS Students",font=("bold",18),bg='misty rose').place(x=150,y=30)
        
        nextbutton= Button(self,text='Remove Student',width=20,font=("bold",10),bg='floral white',command= lambda: self.Next())
        nextbutton.place(x=180,y=350)
        
        backbutton = Button(self, text="Go back",command= lambda:self.back())
        backbutton.place(x=440, y=10)

        self.var0=IntVar()
        cb0=Checkbutton(self,text=det.listofstudents[0],bg='misty rose',variable=self.var0).place(x=100,y=100)

        self.var1=IntVar()
        cb1=Checkbutton(self,text=det.listofstudents[1],bg='misty rose',variable=self.var1).place(x=100,y=130)

        self.var2=IntVar()
        cb3=Checkbutton(self,text=det.listofstudents[2],bg='misty rose',variable=self.var2).place(x=100,y=160)
            
        self.var3=IntVar()
        cb3=Checkbutton(self,text=det.listofstudents[3],bg='misty rose',variable=self.var3).place(x=100,y=190)    

        self.var4=IntVar()
        cb4=Checkbutton(self,text=det.listofstudents[4],bg='misty rose',variable=self.var4).place(x=100,y=220)  

        self.var5=IntVar()
        cb5=Checkbutton(self,text=det.listofstudents[5],bg='misty rose',variable=self.var5).place(x=100,y=250)

        self.var6=IntVar()
        cb6=Checkbutton(self,text=det.listofstudents[6],bg='misty rose',variable=self.var6).place(x=100,y=280)
            
    def Next(self):
        if self.var0.get()==1 :
            det.listofstudents.remove(det.listofstudents[0])
            print(det.listofstudents[0],'has been removed')
        if self.var1.get()==1 :
            det.listofstudents.remove(det .listofstudents[1])
            print(det.listofstudents[1],'has been removed')
        if self.var2.get()==1 :
            det.listofstudents.remove(det.listofstudents[2])
            print(det.listofstudents[2],'has been removed')
        if self.var3.get()==1 :
            det.listofstudents.remove(det.listofstudents[3])
            print(det.listofstudents[3],'has been removed')
        if self.var4.get()==1 :
            det.listofstudents.remove(det.listofstudents[4])
            print(det.listofstudents[4],'has been removed')
        if self.var5.get()==1 :
            det.listofstudents.remove(det.listofstudents[5])
            print(det.listofstudents[5],'has been removed')
        if self.var6.get()==1 :
            det.listofstudents.remove(det.listofstudents[6])
            print(det.listofstudents[6],'has been removed')
        else:
                pass

    def back(self):
        import win0_02
        self.parent.CurrentPage=win0_02.RemoveStudents(self)
        self.parent.CurrentPage.tkraise()

      
        

